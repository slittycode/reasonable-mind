# PR Notes — chore(gov): stabilize governance modules and ensure test compatibility

This PR stabilizes several governance modules and applies formatting/lint fixes across the repo.

Summary
-------
- Replaced a corrupted `agents/governance/plan_validator.py` with a single, clean implementation.
- Updated `agents/governance/execution_proxy.py` to:
  - Add `message` field and sensible defaults to `ExecutionResult` for tests.
  - Implement MOCK behavior (registered mocks, message -> stdout fallback).
  - Implement DRY_RUN behavior with annotated stdout.
  - Prefix denylist reasons with `denylist:` to match tests and observability.
  - Add `get_friction_report()` for friction counters used in tests.
- Cleaned `agents/governance/process_gate.py` and `agents/governance/__init__.py` earlier in the session.
- Ran `ruff format` across the repository and fixed lint findings.

Why
---
The repository had corrupted fragments and duplicate definitions in governance files which caused linting and test failures. This PR restores consistent implementations and normalizes formatting so tests and CI can run reliably.

Files changed (high level)
--------------------------
- agents/governance/plan_validator.py — replaced with a clean implementation
- agents/governance/execution_proxy.py — behavior/API fixes for tests
- agents/governance/process_gate.py — cleaned
- agents/governance/__init__.py — cleaned re-exports
- Many files reformatted (rufff) — formatting-only changes

Testing performed
-----------------
- Installed requirements in the project virtualenv and ran full test suite.
- Test result (local): 591 passed, 0 failed
- Coverage (local): ~95.03% overall; governance modules >89%

Codacy / policy
---------------
Per the repository policy, Codacy analysis must be run for any edited file. This environment cannot reliably run Codacy (Docker/CLI not available). Please run Codacy via CI by adding a `CODACY_TOKEN` secret and re-running the `pre-pr-checks` workflow, or run the Codacy CLI/Docker commands locally. See the repo instructions in `/.github/instructions/codacy.instructions.md`.

Suggested PR title
------------------
chore(gov): stabilize governance modules and ensure test compatibility

Suggested PR description (copy/paste)
------------------------------------
What: Replaced a corrupted `agents/governance/plan_validator.py` with a clean implementation; updated `agents/governance/execution_proxy.py` to support test-friendly ExecutionResult behavior (mock/DRY_RUN), and cleaned `process_gate.py` and `__init__`. Ran `ruff format` and fixed lint issues.

Why: Tests and CI were failing due to corrupted fragments in governance files; this restores deterministic behavior and makes ExecutionProxy mock behavior explicit for tests.

Test: Full test suite run locally — 591 passed, coverage 95.03%.

CI & policy: Add `CODACY_TOKEN` to repository secrets to enable Codacy analysis in CI. Do not merge until pre-PR checks and Codacy are green.

Merge checklist (must be satisfied before merging)
-----------------------------------------------
- [ ] All GitHub Actions checks pass (format, lint, tests, coverage)
- [ ] Codacy analysis runs and reports no blocking issues for edited files
- [ ] Required reviewers have approved the PR
- [ ] No critical dependency vulnerabilities (Trivy) if dependencies changed (not applicable here)

Next steps if CI/Codacy finds issues
-----------------------------------
1. Fix reported issues locally and run `ruff format` and tests.
2. Commit and push updates to this branch.
3. Re-run the pre-PR workflow and verify Codacy is green.

Requested reviewers
-------------------
- @maintainer-1
- @security-team
- @gov-arch-review

Contact
-------
If you want me to run Codacy locally (native CLI or Docker) I can provide exact copy/paste commands. If you prefer CI, add `CODACY_TOKEN` to secrets and re-run the `pre-pr-checks` workflow.

-- automated PR notes by Copilot agent
