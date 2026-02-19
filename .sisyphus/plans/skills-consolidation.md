# Skills Consolidation — Codex as Canonical Source

## TL;DR

> **Quick Summary**: Delete 6 empty skill directories, port all 49 codex skills to opencode (`~/.agents/skills/`) via symlinks, and replace 52 duplicate skill copies across 5 agent homes with symlinks pointing to `~/.codex/skills/`.
> 
> **Deliverables**:
> - 6 empty skill directories removed
> - 49 codex skills symlinked into `~/.agents/skills/` (opencode/ohmycode)
> - 52 duplicate skills across 5 homes replaced with symlinks to codex
> - All unique skills in non-codex homes preserved untouched
> 
> **Estimated Effort**: Quick
> **Parallel Execution**: YES — 7 tasks in Wave 1, 1 verification in Wave 2
> **Critical Path**: All Wave 1 tasks are independent → Wave 2 verification

---

## Context

### Original Request
Consolidate skills across `~/` home directory. Delete empty skill directories, port codex skills to opencode, and fix duplication using codex as the canonical base.

### Interview Summary
**Key Decisions**:
- **Port method**: Symlink `~/.agents/skills/{name}` → `~/.codex/skills/{name}` (single source of truth)
- **Duplicate handling**: Replace copies in other homes with symlinks to codex
- **Unique skills**: Keep unique skills in their respective homes; only touch codex duplicates

### Duplicate Mapping (verified via `comm`)

**Codex skills (49 total — canonical source: `~/.codex/skills/`)**:
algorithmic-art, brainstorming, brand-guidelines, canvas-design, codex-cli-context, codex-code-review, codex-review-workflow, create-plan, dispatching-parallel-agents, doc, doc-coauthoring, docx, executing-plans, finishing-a-development-branch, frontend-design, gh-address-comments, gh-fix-ci, internal-comms, mcp-builder, openai-docs, pdf, playwright, pptx, pro-writing-drafter, pro-writing-researcher, pro-writing-reviewer, receiving-code-review, requesting-code-review, skill-creator, slack-gif-creator, speech, spreadsheet, subagent-driven-development, systematic-debugging, test-driven-development, theme-factory, transcribe, using-git-worktrees, using-superpowers, verification-before-completion, vibe-conductor, vibe-navigator, vibe-pr-loop, vibe-writer, web-artifacts-builder, webapp-testing, writing-plans, writing-skills, xlsx

**Duplicate inventory**:

| Home | Duplicates | Unique (untouched) |
|------|------------|---------------------|
| `~/code/.agent/skills/` | **30** (ALL skills are codex dupes — zero unique) | 0 |
| `~/.cline/skills/` | **9**: algorithmic-art, brand-guidelines, canvas-design, internal-comms, mcp-builder, skill-creator, slack-gif-creator, theme-factory, webapp-testing | 24 (notion-*, document-skills, etc.) |
| `~/Documents/Cursor/skills/` | **9**: (same 9 as cline — both are git clones of `Prat011/awesome-llm-skills`) | 24 (mirrors cline) |
| `~/.kilocode/skills/` | **1**: mcp-builder | 6 |
| `~/code/professional tools/skills/` | **3**: pro-writing-drafter, pro-writing-researcher, pro-writing-reviewer | 6 |
| `~/.gemini/skills/` | **0** | 7 (all unique) |
| `~/.cursor/skills/` | **0** | 1 (review-and-direct) |
| `~/code/.gemini/skills/` | **0** | 5 (all unique) |
| `~/code/opencode/skills/` | **0** | 4 (all unique) |

**Total duplicates to replace**: 52

**Empty directories to delete (6)**:
- `~/.copilot/skills/`
- `~/.qwen/skills/`
- `~/.codeium/windsurf/skills/`
- `~/.vibe/skills/`
- `~/.kiro/skills/`
- `~/.gemini/antigravity/skills/`

**Notable**: `~/.cline/skills/` and `~/Documents/Cursor/skills/` are both git clones of `Prat011/awesome-llm-skills`. They are full duplicates of *each other* (separate from the codex overlap). Replacing the 9 codex-duplicate subdirs with symlinks will make the git repos dirty, but these are local clones and that's fine.

**Also notable**: `~/code/.agent/skills/` has ZERO unique skills — it is a 100% subset of codex.

---

## Work Objectives

### Core Objective
Establish `~/.codex/skills/` as the single source of truth for all shared skills. Port all codex skills to opencode via symlinks. Eliminate duplicate copies.

### Concrete Deliverables
- 6 empty directories deleted
- 49 symlinks created in `~/.agents/skills/` pointing to codex
- 52 duplicate skill directories replaced with symlinks across 5 agent homes
- All unique skills preserved in their original locations

### Definition of Done
- [ ] `ls -la ~/.agents/skills/` shows 51 entries (2 existing + 49 symlinks)
- [ ] `find ~/.agents/skills -maxdepth 1 -type l | wc -l` returns 49
- [ ] No empty skill directories remain in listed paths
- [ ] All 52 replaced duplicates are now symlinks (`find <path> -maxdepth 1 -type l`)
- [ ] All unique skills still accessible (not removed, not broken)

### Must Have
- Codex skills symlinked to opencode (`~/.agents/skills/`)
- Duplicates replaced with symlinks
- Empty directories removed
- Unique skills untouched

### Must NOT Have (Guardrails)
- DO NOT delete any unique skills (skills that exist only in one home)
- DO NOT modify `~/.codex/skills/` itself (it's the canonical source)
- DO NOT touch `~/.codex/vendor_imports/` or `~/.codex/skills/.system/`
- DO NOT remove non-skill files (READMEs, .git dirs, CONTRIBUTING.md) from git-managed skill directories
- DO NOT create nested symlinks (symlink to a symlink)
- DO NOT follow or dereference existing symlinks during deletion

---

## Verification Strategy (MANDATORY)

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed.

### Test Decision
- **Infrastructure exists**: N/A (filesystem operations, no code)
- **Automated tests**: None (QA scenarios verify everything)
- **Framework**: Bash assertions

### QA Policy
Every task includes agent-executed QA scenarios with bash verification commands.
Evidence saved to `.sisyphus/evidence/task-{N}-{scenario-slug}.{ext}`.

| Deliverable Type | Verification Tool | Method |
|------------------|-------------------|--------|
| Symlinks | Bash | `readlink`, `ls -la`, `test -L`, `find -type l` |
| Deletions | Bash | `test ! -d`, `ls` |
| Unique preservation | Bash | `test -d`, `ls`, content verification |

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (All independent — MAX PARALLEL):
├── Task 1: Delete 6 empty skill directories [quick]
├── Task 2: Symlink 49 codex skills → ~/.agents/skills/ [quick]
├── Task 3: Replace 30 duplicates in ~/code/.agent/skills/ [quick]
├── Task 4: Replace 9 duplicates in ~/.cline/skills/ [quick]
├── Task 5: Replace 9 duplicates in ~/Documents/Cursor/skills/ [quick]
├── Task 6: Replace 1 duplicate in ~/.kilocode/skills/ [quick]
└── Task 7: Replace 3 duplicates in ~/code/professional tools/skills/ [quick]

Wave 2 (After Wave 1 — full verification):
└── Task 8: Verify all symlinks, deletions, and unique skill preservation [quick]

Critical Path: Any Wave 1 task → Task 8
Parallel Speedup: ~85% faster than sequential
Max Concurrent: 7 (Wave 1)
```

### Dependency Matrix

| Task | Depends On | Blocks | Wave |
|------|------------|--------|------|
| 1 | — | 8 | 1 |
| 2 | — | 8 | 1 |
| 3 | — | 8 | 1 |
| 4 | — | 8 | 1 |
| 5 | — | 8 | 1 |
| 6 | — | 8 | 1 |
| 7 | — | 8 | 1 |
| 8 | 1,2,3,4,5,6,7 | — | 2 |

### Agent Dispatch Summary

| Wave | # Parallel | Tasks → Agent Category |
|------|------------|----------------------|
| 1 | **7** | T1-T7 → `quick` |
| 2 | **1** | T8 → `quick` |

---

## TODOs

- [x] 1. Delete empty skill directories

  **What to do**:
  - Remove 6 empty skill directories:
    ```bash
    rmdir ~/.copilot/skills/
    rmdir ~/.qwen/skills/
    rmdir ~/.codeium/windsurf/skills/
    rmdir ~/.vibe/skills/
    rmdir ~/.kiro/skills/
    rmdir ~/.gemini/antigravity/skills/
    ```
  - Use `rmdir` (not `rm -rf`) so it fails safely if a directory isn't actually empty

  **Must NOT do**:
  - Do NOT use `rm -rf` — only empty dirs should be removed
  - Do NOT remove parent directories (e.g. don't remove `~/.copilot/` itself, just the `skills/` subdir)

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Simple directory removal, 6 commands
  - **Skills**: [] (none needed)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2-7)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:
  - None needed — straightforward filesystem operations

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Empty directories removed successfully
    Tool: Bash
    Preconditions: Directories exist and are empty
    Steps:
      1. Run: test ! -d ~/.copilot/skills/ && echo "PASS" || echo "FAIL"
      2. Run: test ! -d ~/.qwen/skills/ && echo "PASS" || echo "FAIL"
      3. Run: test ! -d ~/.codeium/windsurf/skills/ && echo "PASS" || echo "FAIL"
      4. Run: test ! -d ~/.vibe/skills/ && echo "PASS" || echo "FAIL"
      5. Run: test ! -d ~/.kiro/skills/ && echo "PASS" || echo "FAIL"
      6. Run: test ! -d ~/.gemini/antigravity/skills/ && echo "PASS" || echo "FAIL"
    Expected Result: All 6 return "PASS"
    Failure Indicators: Any returns "FAIL"
    Evidence: .sisyphus/evidence/task-1-empty-dirs-removed.txt

  Scenario: Parent directories preserved
    Tool: Bash
    Preconditions: After deletion
    Steps:
      1. Run: test -d ~/.copilot/ && echo "PASS" || echo "SKIP-no-parent"
      2. Run: test -d ~/.qwen/ && echo "PASS" || echo "SKIP-no-parent"
    Expected Result: Parent dirs still exist (or were never there)
    Evidence: .sisyphus/evidence/task-1-parents-preserved.txt
  ```

  **Commit**: NO

---

- [x] 2. Symlink codex skills to opencode (~/.agents/skills/)

  **What to do**:
  - For each of the 49 skills in `~/.codex/skills/`, create a symlink in `~/.agents/skills/`:
    ```bash
    for skill in $(ls -1 ~/.codex/skills/ | grep -v '^\.' ); do
      if [ ! -e ~/.agents/skills/"$skill" ]; then
        ln -s ~/.codex/skills/"$skill" ~/.agents/skills/"$skill"
      else
        echo "SKIP (exists): $skill"
      fi
    done
    ```
  - Preserve the 2 existing skills (`find-skills`, `opentui`) — do NOT overwrite them
  - Only create symlinks for skills that don't already exist in `~/.agents/skills/`

  **Must NOT do**:
  - Do NOT overwrite `find-skills` or `opentui` (they are unique to opencode)
  - Do NOT copy files — use `ln -s` only
  - Do NOT symlink `.system` or hidden directories from codex

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single loop creating symlinks
  - **Skills**: [] (none needed)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 3-7)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:
  - `~/.codex/skills/` — source of all 49 skills to symlink
  - `~/.agents/skills/` — target directory (opencode's skill home)
  - `~/.agents/skills/find-skills/` — existing unique skill, must be preserved
  - `~/.agents/skills/opentui/` — existing unique skill, must be preserved

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: All 49 codex skills symlinked to opencode
    Tool: Bash
    Preconditions: ~/.codex/skills/ has 49 skills, ~/.agents/skills/ has 2 existing
    Steps:
      1. Run: find ~/.agents/skills -maxdepth 1 -type l | wc -l
      2. Assert output is 49
      3. Run: readlink ~/.agents/skills/playwright
      4. Assert output contains "/.codex/skills/playwright"
      5. Run: readlink ~/.agents/skills/systematic-debugging
      6. Assert output contains "/.codex/skills/systematic-debugging"
    Expected Result: 49 symlinks, all pointing to ~/.codex/skills/
    Failure Indicators: Count != 49, or readlink doesn't point to codex
    Evidence: .sisyphus/evidence/task-2-opencode-symlinks.txt

  Scenario: Existing unique skills preserved
    Tool: Bash
    Preconditions: find-skills and opentui exist before operation
    Steps:
      1. Run: test -d ~/.agents/skills/find-skills && echo "PASS" || echo "FAIL"
      2. Run: test ! -L ~/.agents/skills/find-skills && echo "PASS-not-symlink" || echo "FAIL-is-symlink"
      3. Run: test -d ~/.agents/skills/opentui && echo "PASS" || echo "FAIL"
      4. Run: test ! -L ~/.agents/skills/opentui && echo "PASS-not-symlink" || echo "FAIL-is-symlink"
    Expected Result: Both exist and are real directories (not symlinks)
    Failure Indicators: Either missing or replaced with symlink
    Evidence: .sisyphus/evidence/task-2-unique-preserved.txt
  ```

  **Commit**: NO

---

- [x] 3. Replace 30 duplicates in ~/code/.agent/skills/ with symlinks

  **What to do**:
  - `~/code/.agent/skills/` is 100% codex duplicates (30 skills, 0 unique)
  - For each skill, remove the copy and replace with symlink to codex:
    ```bash
    DUPES=(algorithmic-art brainstorming brand-guidelines canvas-design dispatching-parallel-agents doc-coauthoring docx executing-plans finishing-a-development-branch frontend-design internal-comms mcp-builder pdf pptx receiving-code-review requesting-code-review skill-creator slack-gif-creator subagent-driven-development systematic-debugging test-driven-development theme-factory using-git-worktrees using-superpowers verification-before-completion web-artifacts-builder webapp-testing writing-plans writing-skills xlsx)

    for skill in "${DUPES[@]}"; do
      rm -rf ~/code/.agent/skills/"$skill"
      ln -s ~/.codex/skills/"$skill" ~/code/.agent/skills/"$skill"
    done
    ```

  **Must NOT do**:
  - Do NOT remove any non-skill files or directories if they exist
  - Verify skill exists in codex before replacing (safety check)

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Scripted replacement, no decision-making
  - **Skills**: [] (none needed)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1-2, 4-7)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:
  - `~/code/.agent/skills/` — target directory, 30 skill dirs to replace
  - `~/.codex/skills/` — symlink target (canonical source)

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: All 30 duplicates replaced with symlinks
    Tool: Bash
    Preconditions: ~/code/.agent/skills/ had 30 skill directories
    Steps:
      1. Run: find ~/code/.agent/skills -maxdepth 1 -type l | wc -l
      2. Assert output is 30
      3. Run: readlink ~/code/.agent/skills/systematic-debugging
      4. Assert output is /Users/christiansmith/.codex/skills/systematic-debugging
      5. Run: find ~/code/.agent/skills -maxdepth 1 -type d -not -name skills | wc -l
      6. Assert output is 0 (no non-symlink skill dirs remain)
    Expected Result: 30 symlinks, 0 real directories
    Failure Indicators: Any real directories remain or symlinks broken
    Evidence: .sisyphus/evidence/task-3-agent-symlinks.txt

  Scenario: Symlinks resolve to valid targets
    Tool: Bash
    Steps:
      1. Run: for s in ~/code/.agent/skills/*/; do test -e "$s" || echo "BROKEN: $s"; done
      2. Assert no "BROKEN" output
    Expected Result: All symlinks resolve
    Evidence: .sisyphus/evidence/task-3-agent-symlinks-valid.txt
  ```

  **Commit**: NO

---

- [x] 4. Replace 9 duplicates in ~/.cline/skills/ with symlinks

  **What to do**:
  - Replace only the 9 codex duplicates; leave 24 unique cline skills intact
  - Note: `~/.cline/skills/` is a git clone of `Prat011/awesome-llm-skills` — replacing subdirs will make the repo dirty, which is fine
    ```bash
    DUPES=(algorithmic-art brand-guidelines canvas-design internal-comms mcp-builder skill-creator slack-gif-creator theme-factory webapp-testing)

    for skill in "${DUPES[@]}"; do
      rm -rf ~/.cline/skills/"$skill"
      ln -s ~/.codex/skills/"$skill" ~/.cline/skills/"$skill"
    done
    ```

  **Must NOT do**:
  - Do NOT touch these unique cline skills: artifacts-builder, changelog-generator, competitive-ads-extractor, content-research-writer, document-skills, domain-name-brainstormer, file-organizer, image-enhancer, invoice-organizer, lead-research-assistant, meeting-insights-analyzer, notion-knowledge-capture, notion-meeting-intelligence, notion-research-documentation, notion-spec-to-implementation, plann, raffle-winner-picker, skill-share, template-skill, video-downloader
  - Do NOT remove `.git/`, `README.md`, `README 2.md`, `CONTRIBUTING.md`, `CONTRIBUTING 2.md`

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: 9 replacements with explicit list
  - **Skills**: [] (none needed)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1-3, 5-7)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:
  - `~/.cline/skills/` — git clone of `Prat011/awesome-llm-skills`
  - `~/.codex/skills/` — symlink target

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: 9 duplicates replaced, 24+ unique skills preserved
    Tool: Bash
    Preconditions: 9 duplicates identified
    Steps:
      1. Run: find ~/.cline/skills -maxdepth 1 -type l | wc -l
      2. Assert output is 9
      3. Run: test -d ~/.cline/skills/document-skills && echo "PASS" || echo "FAIL"
      4. Run: test -d ~/.cline/skills/notion-meeting-intelligence && echo "PASS" || echo "FAIL"
      5. Run: test ! -L ~/.cline/skills/document-skills && echo "PASS-real-dir" || echo "FAIL-symlink"
      6. Run: readlink ~/.cline/skills/theme-factory
      7. Assert contains "/.codex/skills/theme-factory"
    Expected Result: 9 symlinks to codex, all unique skills remain as real directories
    Failure Indicators: Unique skills missing or converted to symlinks
    Evidence: .sisyphus/evidence/task-4-cline-symlinks.txt
  ```

  **Commit**: NO

---

- [x] 5. Replace 9 duplicates in ~/Documents/Cursor/skills/ with symlinks

  **What to do**:
  - Same 9 duplicates as cline (both are clones of same repo)
    ```bash
    DUPES=(algorithmic-art brand-guidelines canvas-design internal-comms mcp-builder skill-creator slack-gif-creator theme-factory webapp-testing)

    for skill in "${DUPES[@]}"; do
      rm -rf ~/Documents/Cursor/skills/"$skill"
      ln -s ~/.codex/skills/"$skill" ~/Documents/Cursor/skills/"$skill"
    done
    ```

  **Must NOT do**:
  - Do NOT touch unique skills (same list as Task 4)
  - Do NOT remove `.git/`, READMEs, CONTRIBUTING files

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Identical pattern to Task 4
  - **Skills**: [] (none needed)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1-4, 6-7)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:
  - `~/Documents/Cursor/skills/` — git clone of `Prat011/awesome-llm-skills`
  - `~/.codex/skills/` — symlink target

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: 9 duplicates replaced, unique skills preserved
    Tool: Bash
    Steps:
      1. Run: find ~/Documents/Cursor/skills -maxdepth 1 -type l | wc -l
      2. Assert output is 9
      3. Run: test -d ~/Documents/Cursor/skills/document-skills && echo "PASS" || echo "FAIL"
      4. Run: readlink ~/Documents/Cursor/skills/mcp-builder
      5. Assert contains "/.codex/skills/mcp-builder"
    Expected Result: 9 symlinks, unique skills untouched
    Evidence: .sisyphus/evidence/task-5-cursor-symlinks.txt
  ```

  **Commit**: NO

---

- [x] 6. Replace 1 duplicate in ~/.kilocode/skills/ with symlink

  **What to do**:
  - Only 1 duplicate: `mcp-builder`
    ```bash
    rm -rf ~/.kilocode/skills/mcp-builder
    ln -s ~/.codex/skills/mcp-builder ~/.kilocode/skills/mcp-builder
    ```

  **Must NOT do**:
  - Do NOT touch: content-research-writer, skill-share, image-enhancer, artifacts-builder, file-organizer, meeting-insights-analyzer

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single replacement
  - **Skills**: [] (none needed)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1-5, 7)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:
  - `~/.kilocode/skills/` — 1 duplicate to replace
  - `~/.codex/skills/mcp-builder` — symlink target

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: mcp-builder replaced, 6 unique skills preserved
    Tool: Bash
    Steps:
      1. Run: test -L ~/.kilocode/skills/mcp-builder && echo "PASS" || echo "FAIL"
      2. Run: readlink ~/.kilocode/skills/mcp-builder
      3. Assert contains "/.codex/skills/mcp-builder"
      4. Run: test -d ~/.kilocode/skills/image-enhancer && echo "PASS" || echo "FAIL"
      5. Run: test ! -L ~/.kilocode/skills/image-enhancer && echo "PASS-real" || echo "FAIL-symlink"
    Expected Result: 1 symlink, 6 real directories
    Evidence: .sisyphus/evidence/task-6-kilocode-symlinks.txt
  ```

  **Commit**: NO

---

- [x] 7. Replace 3 duplicates in ~/code/professional tools/skills/ with symlinks

  **What to do**:
  - 3 duplicates: pro-writing-drafter, pro-writing-researcher, pro-writing-reviewer
    ```bash
    DUPES=(pro-writing-drafter pro-writing-researcher pro-writing-reviewer)

    for skill in "${DUPES[@]}"; do
      rm -rf ~/code/"professional tools"/skills/"$skill"
      ln -s ~/.codex/skills/"$skill" ~/code/"professional tools"/skills/"$skill"
    done
    ```

  **Must NOT do**:
  - Do NOT touch: evidence-first-writing, job-application-orchestrator, job-description-analyzer, job-hunt-ops, networking-outreach-workflow, professional-privacy-sanitizer

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: 3 replacements
  - **Skills**: [] (none needed)

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1-6)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:
  - `~/code/professional tools/skills/` — 3 duplicates
  - `~/.codex/skills/` — symlink target

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: 3 duplicates replaced, 6 unique skills preserved
    Tool: Bash
    Steps:
      1. Run: find ~/code/"professional tools"/skills -maxdepth 1 -type l | wc -l
      2. Assert output is 3
      3. Run: readlink ~/code/"professional tools"/skills/pro-writing-reviewer
      4. Assert contains "/.codex/skills/pro-writing-reviewer"
      5. Run: test -d ~/code/"professional tools"/skills/job-hunt-ops && echo "PASS" || echo "FAIL"
      6. Run: test ! -L ~/code/"professional tools"/skills/job-hunt-ops && echo "PASS-real" || echo "FAIL"
    Expected Result: 3 symlinks, 6 real directories
    Evidence: .sisyphus/evidence/task-7-protools-symlinks.txt
  ```

  **Commit**: NO

---

- [x] 8. Full verification sweep

  **What to do**:
  - Comprehensive verification of all operations:
    1. Verify all 6 empty dirs are gone
    2. Verify 49 symlinks in `~/.agents/skills/` pointing to codex
    3. Verify `find-skills` and `opentui` are real dirs (not replaced)
    4. Verify all replacement symlinks across 5 homes resolve to valid codex targets
    5. Verify no unique skills were removed or converted
    6. Generate summary report

  **Must NOT do**:
  - Do NOT modify any files — read-only verification

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Read-only verification commands
  - **Skills**: [] (none needed)

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 2 (after all Wave 1 tasks)
  - **Blocks**: None (final task)
  - **Blocked By**: Tasks 1-7

  **References**:
  - All directories listed in tasks 1-7

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Complete consolidation verification
    Tool: Bash
    Steps:
      1. Count empty dirs remaining:
         for d in ~/.copilot/skills ~/.qwen/skills ~/.codeium/windsurf/skills ~/.vibe/skills ~/.kiro/skills ~/.gemini/antigravity/skills; do test -d "$d" && echo "STILL EXISTS: $d"; done
         Assert: no output (all gone)

      2. Count opencode symlinks:
         find ~/.agents/skills -maxdepth 1 -type l | wc -l
         Assert: 49

      3. Verify unique opencode skills preserved:
         test -d ~/.agents/skills/find-skills && test ! -L ~/.agents/skills/find-skills && echo "PASS"
         test -d ~/.agents/skills/opentui && test ! -L ~/.agents/skills/opentui && echo "PASS"
         Assert: both "PASS"

      4. Count total replacement symlinks across all homes:
         TOTAL=0
         for dir in ~/code/.agent/skills ~/.cline/skills ~/Documents/Cursor/skills ~/.kilocode/skills ~/code/"professional tools"/skills; do
           COUNT=$(find "$dir" -maxdepth 1 -type l 2>/dev/null | wc -l)
           TOTAL=$((TOTAL + COUNT))
           echo "$dir: $COUNT symlinks"
         done
         echo "TOTAL: $TOTAL"
         Assert: TOTAL = 52

      5. Check for broken symlinks across all homes:
         for dir in ~/.agents/skills ~/code/.agent/skills ~/.cline/skills ~/Documents/Cursor/skills ~/.kilocode/skills ~/code/"professional tools"/skills; do
           find "$dir" -maxdepth 1 -type l ! -exec test -e {} \; -print
         done
         Assert: no output (no broken symlinks)

      6. Spot-check unique skills:
         test -d ~/.gemini/skills/grisha-skills && echo "PASS gemini grisha"
         test -d ~/.cline/skills/document-skills && echo "PASS cline docs"
         test -d ~/code/"professional tools"/skills/job-hunt-ops && echo "PASS protools"
         test -d ~/code/.gemini/skills/research-director && echo "PASS code-gemini"
         Assert: all "PASS"
    Expected Result: All assertions pass, 0 broken symlinks, 52 total replacements
    Failure Indicators: Any broken symlink, missing unique skill, or wrong count
    Evidence: .sisyphus/evidence/task-8-full-verification.txt
  ```

  **Commit**: NO

---

## Commit Strategy

No commits — this plan operates entirely on home directory filesystem, outside of any git repository.

---

## Success Criteria

### Verification Commands
```bash
# Opencode has all codex skills
find ~/.agents/skills -maxdepth 1 -type l | wc -l  # Expected: 49

# No broken symlinks anywhere
for dir in ~/.agents/skills ~/code/.agent/skills ~/.cline/skills ~/Documents/Cursor/skills ~/.kilocode/skills ~/code/"professional tools"/skills; do
  find "$dir" -maxdepth 1 -type l ! -exec test -e {} \; -print
done
# Expected: no output

# Empty dirs are gone
for d in ~/.copilot/skills ~/.qwen/skills ~/.codeium/windsurf/skills ~/.vibe/skills ~/.kiro/skills ~/.gemini/antigravity/skills; do
  test -d "$d" && echo "FAIL: $d still exists"
done
# Expected: no output
```

### Final Checklist
- [ ] All "Must Have" present
- [ ] All "Must NOT Have" absent
- [ ] 49 codex skills available in opencode
- [ ] 52 duplicates consolidated via symlinks
- [ ] 6 empty directories removed
- [ ] Zero unique skills lost
- [ ] Zero broken symlinks
