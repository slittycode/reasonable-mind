# Copilot Instructions for Reasonable Mind

These are concise, actionable instructions intended for AI-assisted edits and human contributors. Follow the "Critical pre-PR checklist" on every change and treat the `/.github/instructions/codacy.instructions.md` rules as mandatory.

## 1. Quick project orientation
- Purpose: Neuro-symbolic reasoning framework (8X architecture) combining logic engines + LLM-driven extended thinking.
- Key code areas:
	- `agents/` — core agent logic, tools, and tests
	- `agents/core_logic/`, `agents/logic/` — deterministic logic engines and grounding
	- `agents/tools/` — tool implementations (native + MCP)
	- `data/` — reference data (argument_forms.json, fallacies.json)
	- `trainer/`, `financial-data-analyst/` — UI/demo code (frontend Node/TS)

## 2. Critical pre-PR checklist (MUST run before opening a PR)
Run these in order locally; include results in the PR description.

1. Format and lint

```bash
ruff format .
ruff check .
```

2. Type check

```bash
pyright || echo 'pyright not installed; skip locally but CI will run type checks.'
```

3. Unit tests (run full test suite or focused tests you changed)

```bash
pytest agents/tests/ -v
# or a focused test
pytest agents/tests/test_logic_orchestrator.py -q
```

4. Codacy analysis (MANDATORY after edits)

- The repository enforces Codacy MCP rules in `/.github/instructions/codacy.instructions.md`. After editing any file you MUST run the Codacy analysis tool used by your org (e.g., `codacy_cli_analyze`) for each edited file with `rootPath` set to the workspace path. If you added dependencies, run the Codacy trivy scan per that file.
- If the Codacy CLI is not available locally, follow the guidance in `/.github/instructions/codacy.instructions.md` (ask for install or open an issue / notify maintainers). Do NOT merge without Codacy verification for changed files.

5. Security on dependencies

 - If you change `requirements.txt`, `pyproject.toml`, or `package.json`, run the repository's vulnerability check (Codacy `trivy`) and address any critical findings before opening a PR.

If any step fails, fix the issue locally and re-run. Do not open a PR until all steps are green or you have a documented rationale in the PR body explaining temporary exceptions.

## 3. Environment & secrets (must not commit secrets)
- Create or update a `.env.example` listing environment variables used by the project (see `.env.example` in repo root). Never commit real keys. Use GitHub Actions Secrets for CI.
- Typical variables (placeholders): `ANTHROPIC_API_KEY`, `CLAUDE_API_KEY`, `OTHER_API_KEY`.
- Tests that call external APIs should be mocked in unit tests; if integration tests require keys, mark them and run separately.

## 4. Files that require manual review or special handling
- Notebooks (`*.ipynb`) and demo scripts (`*_demo.py`, files under `trainer/`) have relaxed lint rules and often include example credentials or environment-specific code. Changes to these require human review and a clear test plan in the PR.
- `/.github/instructions/*` files are policy-critical. Do not modify without maintainers' approval.

## 5. CI / PR expectations
- PRs should target `main` via topic branches (use a descriptive prefix, e.g., `fix/`, `feat/`, `ci/`). Do not push directly to `main`.
- Required checks (CI will enforce): formatting (ruff), linter, type-checks, unit tests, Codacy analysis, and security scan for dependency edits. Include test results and a short summary in the PR description.
- PR description template: summary, affected modules, tests added/updated, how to run locally, Codacy/trivy results.

## 6. Contributor & AI-agent rules
- Agents (automated commits or Copilot-style agents) MUST:
	- Run the full pre-PR checklist locally before opening a PR.
	- Never push directly to `main`; always open a PR and set reviewers.
	- Not modify files in `/.github/instructions/` without human approval.
	- Include a complete PR description and the results of local runs (format/lint/tests/Codacy).
- For small edits (typo fixes, docs) agents may propose PRs but still run the checks above.

## 7. Dependency & security workflow
- Add dependency: Update manifest (`requirements.txt` / `pyproject.toml` / `package.json`) -> run tests -> run Codacy `trivy` scan -> fix vulnerabilities -> open PR. Document changes in PR.

## 8. Architecture & documentation updates
- If your change affects reasoning, logic engines, or the 8X architecture, update `agents/ARCHITECTURE_AUDIT.md` and add a short note in `CHANGELOG.md` explaining the rationale and potential impact on other layers.

## 9. Quick commands (copy-paste)

```bash
# Format + lint
ruff format . && ruff check .

# Type-check
pyright

# Run tests (full or selective)
pytest agents/tests/ -v
pytest agents/tests/test_logic_orchestrator.py -q
```

## 10. References
- `README.md`, `CLAUDE.md`, `agents/README.md`, `agents/ARCHITECTURE_AUDIT.md`, `/.github/instructions/codacy.instructions.md`, `ruff.toml`.

---
If anything above is unclear or you'd like me to apply enforcement (pre-commit hooks, CI step changes, or an `.env.example`), say which one and I will implement it. Thank you!
