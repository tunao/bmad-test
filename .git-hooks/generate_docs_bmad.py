#!/usr/bin/env python
import os
import subprocess
import sys
from pathlib import Path

import yaml
from anthropic import AnthropicBedrock

# --------------------------------------------------------------------
# Config
# --------------------------------------------------------------------
REPO_ROOT = Path(
    subprocess.check_output(
        ["git", "rev-parse", "--show-toplevel"], text=True
    ).strip()
)

DOCS_ROOT = REPO_ROOT / "docs"
AGENT_CONFIG_PATH = REPO_ROOT / ".bmad" / "custom" / "agents" / "repo-docs-documenter.agent.yaml"

AWS_REGION = os.getenv("AWS_REGION", "eu-west-1")
MODEL_ID = os.getenv(
    "DOC_BOT_MODEL",
    # Put your actual Bedrock Claude model ID here
    "eu.anthropic.claude-sonnet-4-20250514-v1:0",
)

anthropic_client = AnthropicBedrock(
    aws_region=AWS_REGION,
    aws_profile=os.getenv("AWS_PROFILE"),
)


# --------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------
def load_agent_yaml() -> dict:
    data = yaml.safe_load(AGENT_CONFIG_PATH.read_text(encoding="utf-8"))
    if "agent" not in data:
        raise RuntimeError("Invalid BMAD agent file: missing top-level 'agent'")
    return data["agent"]


def build_system_prompt(agent_cfg: dict) -> str:
    meta = agent_cfg.get("metadata", {})
    persona = agent_cfg.get("persona", {})
    principles = persona.get("principles", [])
    critical = agent_cfg.get("critical_actions", [])

    lines = []
    lines.append(f"You are '{meta.get('name', 'Repo Docs Documenter')}', "
                 f"a BMAD-style repository documentation agent.")
    lines.append("")
    lines.append("ROLE:")
    lines.append(persona.get("role", ""))
    lines.append("")
    lines.append("IDENTITY:")
    lines.append(persona.get("identity", ""))
    lines.append("")
    lines.append("COMMUNICATION STYLE:")
    lines.append(persona.get("communication_style", ""))
    lines.append("")
    if principles:
        lines.append("CORE PRINCIPLES:")
        for p in principles:
            lines.append(f"- {p}")
        lines.append("")
    if critical:
        lines.append("CRITICAL ACTIONS:")
        for c in critical:
            lines.append(f"- {c}")
        lines.append("")
    lines.append(
        "You are invoked from a git pre-commit hook. "
        "When asked to document a file, you must output ONLY the final Markdown "
        "for that file, with no prose explanation or surrounding text."
    )
    return "\n".join(lines)


def get_staged_diff_for_file(path: Path) -> str:
    try:
        return subprocess.check_output(
            ["git", "diff", "--cached", "--", str(path)],
            text=True,
            errors="replace",
        )
    except subprocess.CalledProcessError:
        return ""


def target_md_path(file_path: Path) -> Path:
    rel = file_path.relative_to(REPO_ROOT)
    return DOCS_ROOT / rel.with_suffix(".md")


def call_claude(system_prompt: str, user_content: str) -> str:
    resp = anthropic_client.messages.create(
        model=MODEL_ID,
        max_tokens=4096,
        temperature=0.2,
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )
    parts = []
    for block in resp.content:
        if block.type == "text":
            parts.append(block.text)
    return "".join(parts)


def build_user_prompt(rel_path: str, code: str, diff: str, existing_md: str | None) -> str:
    chunks = [
        f"Repository file: `{rel_path}`",
        "",
        "You are executing the *doc-file command* defined for this BMAD agent.",
        "",
        "Current staged file contents:",
        "```",
        code[:30000],
        "```",
        "",
        "Staged git diff for this file:",
        "```diff",
        diff[:15000],
        "```",
    ]

    if existing_md:
        chunks.append("")
        chunks.append("Existing Markdown documentation for this file:")
        chunks.append("```markdown")
        chunks.append(existing_md[:20000])
        chunks.append("```")
        chunks.append(
            "\nUpdate the existing documentation in-place so it matches the "
            "current code and diff. Preserve structure and headings where possible."
        )
    else:
        chunks.append(
            "\nThere is currently no Markdown doc for this file. "
            "Create a new one that explains:\n"
            "- What this file does and its role in the system\n"
            "- Its public API (functions/classes/types)\n"
            "- Important invariants and edge cases\n"
            "- 1–2 example usages in code blocks\n"
        )

    chunks.append(
        "\nReturn ONLY the final Markdown for the documentation file. "
        "Do not wrap it in backticks or add commentary."
    )

    return "\n".join(chunks)


# --------------------------------------------------------------------
# Main
# --------------------------------------------------------------------
def main(argv: list[str]) -> None:
    if not argv:
        print("[bmad-doc] No files provided", file=sys.stderr)
        return

    agent_cfg = load_agent_yaml()
    system_prompt = build_system_prompt(agent_cfg)

    for rel in argv:
        file_path = (REPO_ROOT / rel).resolve()
        if not file_path.exists():
            print(f"[bmad-doc] Skipping non-existent file: {rel}")
            continue

        code = file_path.read_text(encoding="utf-8")
        diff = get_staged_diff_for_file(file_path)
        md_path = target_md_path(file_path)

        existing_md = None
        if md_path.exists():
            existing_md = md_path.read_text(encoding="utf-8")

        print(f"[bmad-doc] {rel} -> {md_path.relative_to(REPO_ROOT)}")

        user_prompt = build_user_prompt(
            rel_path=str(file_path.relative_to(REPO_ROOT)),
            code=code,
            diff=diff,
            existing_md=existing_md,
        )

        md_content = call_claude(system_prompt, user_prompt)

        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(md_content, encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])
