# opencode-setup

A reusable **OpenCode orchestration baseline** you can copy into any repository.

It provides a two-lane workflow (`standard` and `full-auto`) with delegation-first execution, plus project-level guidance and reusable skills.

## What this repo includes

- `opencode.json` — agent registry, permissions, and defaults
- `AGENTS.md` — project execution policy, risk gates, and collaboration rules
- `.opencode/agents/` — primary orchestrators and specialist subagents
  - primary: `standard`, `full-auto`
  - standard specialists: `standard-plan`, `standard-build`, `standard-test-automation`, `standard-refactor`, `standard-devops`, `standard-docs-writer`
  - auto specialists: `auto-plan`, `auto-build`, `auto-test-automation`, `auto-refactor`, `auto-devops`, `auto-docs-writer`
  - shared specialists: `explore`, `code-reviewer`, `security-auditor`, `performance-analyzer`, `codebase-architecture-mapper`, `type-change-inconsistency-finder`
- `.opencode/skills/` — bundled, loadable skills (`flist-build-upload`, `hub-monorepo`, `syngpipe-runtime`, `vm-deployment`)

## Lane model (core workflow)

Both lanes are **delegation-first**: primary orchestrators do not directly edit files or run state-changing commands. They route execution to specialist subagents.

### `standard` lane (default)

- Confirmation-oriented orchestration
- Delegates executable work to `standard-*` specialists
- Explicitly confirms plan/approach before implementation for non-trivial tasks

### `full-auto` lane

- Autonomous orchestration
- Delegates executable work to `auto-*` specialists
- Proceeds without routine confirmation prompts, except in risk-gated cases

## Delegation flow (non-trivial task)

Typical flow is:

1. `explore` to map files and context
2. lane planner (`standard-plan` or `auto-plan`) to produce execution plan
3. lane builder (`standard-build` or `auto-build`) to implement
4. `code-reviewer` for a review pass
5. `type-change-inconsistency-finder` when shared contracts/types changed

Additional specialists (tests, docs, devops, refactor, security, performance) are invoked when the task scope requires them.

## Permission and safety model (high level)

- Primary orchestrators (`standard`, `full-auto`) are configured as orchestration-only (no direct write/edit/bash execution).
- Write/command execution happens in subagents with scoped permissions.
- Baseline command guardrails in `opencode.json` deny clearly dangerous operations (for example force-reset or recursive destructive deletes).
- Both lanes enforce stop-and-confirm for high-risk changes such as:
  - security/auth model changes
  - billing/payment or funds-flow changes
  - destructive/irreversible operations
  - external API contract breaks

## How to use this in another repo

1. Copy these files/folders into the target repo root:
   - `opencode.json`
   - `AGENTS.md`
   - `.opencode/agents/`
   - `.opencode/skills/`
2. Update `AGENTS.md`:
   - repository layout and terminology
   - risk gates and done criteria
   - documentation/runbook references
3. Update skills:
   - keep only skills relevant to your project
   - rename/add skill folders under `.opencode/skills/` as needed
   - make sure `AGENTS.md` skill-routing table matches actual skill names
4. Adjust `opencode.json`:
   - set your preferred `default_agent` (`standard` or `full-auto`)
   - tune permission rules for your environment
   - keep delegation boundaries intact unless you intentionally want direct execution in primaries
5. Reload/restart OpenCode so agent/skill config is re-read.

## Notes

- Current default agent in this repo is `standard`.
- The included `AGENTS.md` and skill set are prefilled for a Phase4AI hub-style workspace and should be customized when reused.
