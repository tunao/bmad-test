<!-- .github/copilot-instructions.md - guidance for AI coding agents -->
# Copilot / AI agent instructions — bmad-test

This repository is currently minimal (only a README). These instructions describe how an AI coding agent should work productively here and what to check before making changes.

1. Repo snapshot
- **Key file:** `README.md` — the only source of repository-level information at this time.

2. Immediate goals for agents
- Inspect the repository tree (`ls -la`) and open `README.md` first.
- If you cannot find build, test, or CI configuration files, do not assume defaults — ask the user before adding tooling.

3. Discovery steps (mandatory)
- Run a workspace search for common files: `package.json`, `pyproject.toml`, `Makefile`, `Dockerfile`, `tests/`, `.github/workflows/`.
- If none are present, report back to the user and propose one small, explicit change at a time (for example: add a README section describing the project's purpose).

4. Editing and merge guidance
- Keep changes minimal and focused. When adding files, include a short rationale in the commit message.
- If you add new tooling (build/test/CI), include a short README section explaining how to run it and any platform assumptions.

5. Examples and patterns (from this repo)
- The repo currently has no source code. Example action: update [README.md](README.md) to document goals or add a `CONTRIBUTING.md` first — confirm with the user before creating larger scaffolding.

6. Communication with the user
- When uncertain about architecture, dependencies, or expected languages, ask one targeted question (e.g., "Which language or framework should I scaffold for this project?").
- After any change that adds files or tooling, provide runnable verification steps and any commands needed to reproduce locally.

7. Safety and scope
- Do not make opinionated choices about language, package manager, or CI provider without explicit user confirmation.

If this guidance is missing anything you expect, tell me which specific areas to expand (build, test, CI, language detection, scaffolding examples).
