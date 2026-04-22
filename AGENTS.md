## Agent Guide

Last updated: 2026-04-22
Scope: reusable template baseline for repository-scoped agent execution guidance.

## Skills — Load These Automatically

When a task matches a description below, load the skill **before starting work** using the skill tool.
Do not ask the user whether to load it — load it proactively.
These mappings are starter defaults for this template; replace or trim them after copying to a target project.

| Task type | Skill name |
|---|---|
| Build/export/upload a ThreeFold flist, validate zinit runtime, SSH/nginx/service debug on a deployed VM | `flist-build-upload` |
| Work on any app or lib inside an Nx monorepo (NestJS, React, TypeScript) | `hub-monorepo` |
| Deploy or debug a VM via the local orchestrator API or TFGrid directly | `vm-deployment` |
| Work on SynGPipe runtime, Dockerfile.threefold, zinit services, workspace layout, fileserver | `syngpipe-runtime` |

If a task spans multiple skill areas, load all relevant skills before starting.

## Precedence

1. Runtime/platform instructions (system/developer/tooling)
2. `AGENTS.md`
3. Task-specific user requests

If instructions conflict, follow the highest priority and call it out.

## Customization (Project-Specific)

Use this section for repository-specific context after copying this template.

## Required customization after copy

Update the items below before using this file in a production repository:

- [ ] Replace **Repository Layout** with actual top-level directories and boundaries.
- [ ] Replace **Documentation Map** with real docs and ownership paths.
- [ ] Replace/trim the **Skills** table to only include relevant skills.
- [ ] Update **Stop-And-Confirm Cases** if the project has additional risk gates.

### Repository Layout

- `<replace-me>/`: primary product codebase.
- `<replace-me>/`: infrastructure/deployment assets.
- `<replace-me>/`: supporting services, tooling, or mocks.

Treat these as distinct scopes unless a task explicitly spans multiple areas.

### Documentation Map

Agent system docs:

- `AGENTS.md`: agent behavior, collaboration process, risk gates, done criteria.
- `ARCHITECTURE.md`: system architecture snapshot, key decisions, key files.
- `RUNBOOK.md`: executable workflows and commands for setup, dev, validation, and release.

Project scope docs:

- `<replace-me>/README.md`: high-level product overview and onboarding.
- `<replace-me>/README.md`: infrastructure/deployment context and ops notes.
- `<replace-me>/README.md`: service-specific behavior and local run instructions.

## Collaboration Defaults

- Plan before coding; align on non-trivial choices.
- Surface assumptions, edge cases, and trade-offs.
- Ask clarifying questions when ambiguity changes behavior/architecture.
- Treat style choices as preference, not correctness.
- Push back on risky or flawed approaches.

## Delivery Process

1. Identify material decisions.
2. Present options with trade-offs.
3. Lane-specific execution:
   - **standard lane**: confirm approach before implementation.
   - **full-auto lane**: proceed autonomously without routine confirmation.
4. Implement.
5. Re-align if new constraints appear.

## Stop-And-Confirm Cases

- Security/auth model changes or secret handling
- Billing/payment or funds-flow changes
- Data-loss risk (destructive/irreversible ops)
- External API contract breaks

Proceed autonomously for low-risk details that do not change agreed behavior.

## Done Criteria

- Changed code builds.
- Formatting/lint pass for touched scope.
- Tests for changed behavior pass (or are added if missing).
- API/schema/config contract changes are documented.
- Any plan deviation is explained in handoff.

## Command Policy

- Prefer project-local scripts and workspace tooling defined by the repo.
- Before handoff, run the smallest relevant set of checks for touched scope:
  - build/compile
  - formatting/lint
  - tests
- For cross-service changes, run an end-to-end/system-level verification path.
- Keep project command references in `RUNBOOK.md` (and keep `README.md` high-level).

## Source of Truth

- If docs and code differ, trust code and report mismatch.
- Keep architecture details in `ARCHITECTURE.md`.
- Keep operational commands and workflows in `RUNBOOK.md`.
- Update docs when architecture or workflows change.
