# Agents

> Agent definitions for this project.
> GitHub Copilot uses `.github/agents/*.agent.md` files (detailed per-agent prompts).
> Claude Code uses this file for agent role reference.
> Both share the same project context from `CLAUDE.md` / `.github/copilot-instructions.md`.

## Common Rules (all agents)

Every agent must follow these steps before executing its role-specific SOP:

1. **Read `CLAUDE.md`** — consult the relevant sections for your role (listed in each SOP below)
2. **Surgical Changes** — only touch what the task requires; every change must trace to the user's request
3. **Verify** — validate your output before reporting done (JSON: `python3 -c "import json; json.load(open('file'))"`)

## coding

Write or edit code — JavaScript, HTML, CSS, JSON, or Markdown content files.
Use for implementing features, fixing bugs, adding topics, and modifying UI.

**Constraints**: Read target files before editing. Match existing code style. Minimal changes only. No npm, no framework.

**SOP** (after Common Rules — ref: Code Style & Conventions):
1. Read target file(s) to understand current code
2. Implement changes — match existing patterns (camelCase, section headers, `escapeHtml()`)
3. Verify: no broken references, changes trace directly to user's request

## content

Create or expand educational content — mind map Markdown files, quiz question JSON files, and topics.json registration.
Use for adding new topics, new subjects, new sub-subjects, bulk content generation, and content quality review.

**Constraints**: Follow 心智圖四大設計原則 (keywords, radiant structure, color, association). Validate JSON schema. Register in topics.json.

**SOP** (after Common Rules — ref: Content Structure):
1. Check existing examples: read a similar `.md` / `.json` file for format reference
2. Create content following Markmap header conventions (`#`/`##`/`###`)
3. Register new topic in `content/{subject}/{sub}/topics.json`
4. Create matching `details/*.json` and `questions/{subject}/{sub}/*.json` if applicable
5. Verify: `python3 scripts/smoke-test.py` passes

## planning

Plan features, break down tasks, design solutions, create implementation plans.
Use for architecture decisions, feature scoping, and task decomposition.

**Constraints**: DO NOT write code. Produce numbered task lists with file references and acceptance criteria.

**SOP** (after Common Rules — ref: Architecture, Project Directory Structure):
1. Identify affected files and components
2. Produce numbered plan with verifiable acceptance criteria per step
3. Flag any risks, tradeoffs, or ambiguities (Think Before Coding principle)
4. Output format: `[Step] → file: [path] → verify: [check]`

## reviewer

Review code changes, audit code quality, check for security issues, evaluate pull requests.
Use for code review, best practices validation, and accessibility checks.

**Constraints**: Read-only analysis. Flag XSS risks, broken references, CSS inconsistencies, data schema violations.

**SOP** (after Common Rules — ref: Code Style, Conventions, Do NOT):
1. Check each changed file against coding standards
2. Verify XSS prevention: all dynamic content uses `escapeHtml()`
3. Verify no forbidden patterns (npm, TypeScript, framework, `markmap-autoloader`, `window.markmapView`)
4. Check data integrity: JSON schema compliance, file reference validity
5. Report: list issues with severity (critical/warning/info) and file:line references

## testing

Test the application, validate changes, check for broken links, verify data integrity.
Use for smoke testing, content validation, and cross-file consistency checks.

**Constraints**: Run validation scripts. Check JSON validity, file references, content completeness.

**SOP** (after Common Rules — ref: Core Development Commands):
1. Run `python3 scripts/smoke-test.py` for full validation
2. Validate specific content: `python3 scripts/validate-chemistry.py` (if chemistry-related)
3. Verify topics.json entries match existing `.md` files
4. Report: pass/fail summary with specific error details

## doc-writer

Write documentation, README files, code comments, JSDoc annotations, content guides.
Use for creating or updating project documentation.

**Constraints**: Match existing documentation style. Use Traditional Chinese for user-facing docs.

**SOP** (after Common Rules — ref: Cross-Reference):
1. Read existing docs to match tone and format
2. Write in Traditional Chinese for user-facing content; English for code comments
3. Ensure cross-references between CLAUDE.md / copilot-instructions.md / AGENTS.md remain consistent
4. Verify: no broken markdown links, correct file paths
