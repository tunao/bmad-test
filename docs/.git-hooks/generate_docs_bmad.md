# Git Hooks Documentation Generator

A Python script that automatically generates and maintains Markdown documentation for repository files using Claude AI through AWS Bedrock. This script is designed to be executed from a git pre-commit hook to ensure documentation stays synchronized with code changes.

## Role in System

This script serves as a bridge between the git workflow and the BMAD (Business Model and Architecture Documentation) agent system. It:

- Monitors staged files in git commits
- Extracts file contents and git diffs 
- Invokes Claude AI to generate or update documentation
- Saves the generated documentation to the `docs/` directory

## Public API

### Main Functions

#### `main(argv: list[str]) -> None`

Entry point that processes a list of repository-relative file paths and generates documentation for each.

**Parameters:**
- `argv`: List of file paths relative to the repository root

**Behavior:**
- Loads BMAD agent configuration
- For each file, extracts content and git diff
- Calls Claude AI to generate/update documentation
- Saves results to corresponding `.md` files in `docs/`

### Configuration Functions

#### `load_agent_yaml() -> dict`

Loads and validates the BMAD agent configuration from `.bmad/custom/agents/repo-docs-documenter.agent.yaml`.

**Returns:**
- Dictionary containing agent configuration

**Raises:**
- `RuntimeError`: If the YAML file is missing the required 'agent' top-level key

#### `build_system_prompt(agent_cfg: dict) -> str`

Constructs the system prompt for Claude AI based on the agent configuration.

**Parameters:**
- `agent_cfg`: Agent configuration dictionary

**Returns:**
- Formatted system prompt string containing role, identity, principles, and critical actions

### Utility Functions

#### `get_staged_diff_for_file(path: Path) -> str`

Retrieves the git diff for staged changes of a specific file.

#### `target_md_path(file_path: Path) -> Path`

Determines the target documentation path by mapping source files to the `docs/` directory structure.

#### `call_claude(system_prompt: str, user_content: str) -> str`

Makes API calls to Claude AI through AWS Bedrock.

#### `build_user_prompt(rel_path: str, code: str, diff: str, existing_md: str | None) -> str`

Constructs the user prompt with file context, code, and diff information.

## Configuration

### Environment Variables

- `AWS_REGION`: AWS region for Bedrock (default: "eu-west-1")
- `AWS_PROFILE`: AWS profile for authentication
- `DOC_BOT_MODEL`: Claude model ID (default: "eu.anthropic.claude-sonnet-4-20250514-v1:0")

### File Paths

- `REPO_ROOT`: Git repository root (auto-detected)
- `DOCS_ROOT`: Documentation directory (`{REPO_ROOT}/docs`)
- `AGENT_CONFIG_PATH`: BMAD agent configuration file

## Important Invariants

1. **Content Limits**: Code content is truncated to 30,000 characters, diffs to 15,000 characters, and existing documentation to 20,000 characters to manage API limits.

2. **File Resolution**: All file paths are resolved to absolute paths to prevent path traversal issues.

3. **Directory Creation**: Target documentation directories are created automatically with `parents=True`.

4. **Error Handling**: Git command failures return empty strings rather than raising exceptions.

5. **Encoding**: All file operations use UTF-8 encoding consistently.

## Usage Examples

### Command Line Usage

```bash
# Document a single file
python .git-hooks/generate_docs_bmad.py src/main.py

# Document multiple files
python .git-hooks/generate_docs_bmad.py src/main.py src/utils.py tests/test_main.py
```

### Git Pre-commit Hook Integration

```bash
#!/bin/bash
# In .git/hooks/pre-commit

# Get list of staged Python files
staged_files=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$')

if [ ! -z "$staged_files" ]; then
    python .git-hooks/generate_docs_bmad.py $staged_files
    
    # Stage the generated documentation
    git add docs/
fi
```
