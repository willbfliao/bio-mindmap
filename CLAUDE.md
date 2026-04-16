# Mindmap-Highschool — Project Guidelines (唯一真理來源)

> **此檔案為專案的唯一真理來源 (Single Source of Truth)。**
> 所有 AI 工具（Claude Code、GitHub Copilot、Agent）皆必須以此檔案為最終依據。

---

## Cross-Reference（三位一體架構）

本專案的 AI 協作規範由三份檔案組成，各司其職、互不衝突：

| 檔案 | 角色 | 職責 |
|------|------|------|
| **`CLAUDE.md`**（本檔案） | 核心中樞 | 技術棧、目錄結構、開發指令、編碼規範、行為準則 |
| **`.github/copilot-instructions.md`** | 行為映射 | GitHub Copilot 回應風格、程式碼生成偏好、工具行為約束（引用本檔規則，不重複定義） |
| **`AGENTS.md`** | 角色流程 | Agent 角色定義、標準作業流程 (SOP)、任務分派規則（引用本檔指令） |

**規則**：當指令衝突時，以 `CLAUDE.md` 為準。

---

## Overview

Mindmap-Highschool is a **static** educational web app for Taiwan high school students. It displays multi-subject content as interactive mind maps (via Markmap) and provides exam practice questions. Subjects include 國文, 英文, 數學, 自然 (物理/化學/生物/地科), and 社會 (歷史/地理/公民). All UI text is in **Traditional Chinese (繁體中文)**.

## Tech Stack

- **Vanilla JS** — no framework, no TypeScript, no bundler
- **Markmap** via CDN (`jsDelivr`) for mind map rendering (`markmap-lib@0.15`, `markmap-view@0.15`, `d3@7`)
- **Plain CSS** with CSS custom properties for theming
- **LocalStorage** for read/completion progress tracking
- **GitHub Pages** deployment (auto via GitHub Actions on push to `main`)

No `package.json` exists. External libs loaded via CDN only.

## Core Development Commands

```bash
# 本地開發伺服器
python3 -m http.server 8000
# 或
npx http-server

# 內容驗證
python3 scripts/smoke-test.py        # 煙霧測試（檔案參照、JSON 格式）
python3 scripts/validate-chemistry.py # 化學內容驗證

# JSON 格式檢查（單檔）
python3 -c "import json; json.load(open('path/to/file.json'))"
```

> 本專案無 `package.json`，不使用 npm/build/lint 工具。所有驗證透過上述腳本執行。

## Project Directory Structure

```
mindmap-highschool/
├── CLAUDE.md                          # 核心中樞（本檔案）
├── AGENTS.md                          # 角色流程定義
├── .github/
│   ├── copilot-instructions.md        # AI 行為映射
│   └── agents/                        # Copilot Agent 詳細 prompt
│       ├── coding.agent.md
│       ├── content.agent.md
│       ├── planning.agent.md
│       ├── reviewer.agent.md
│       ├── testing.agent.md
│       └── doc-writer.agent.md
├── index.html                         # 首頁（科目選擇）
├── subject.html                       # 科目/主題列表
├── viewer.html                        # 心智圖檢視器
├── quiz.html                          # 測驗頁面
├── js/
│   └── app.js                         # 共用核心邏輯
├── css/
│   └── style.css                      # 全域樣式
├── content/
│   ├── subjects.json                  # 科目索引（主結構）
│   └── {subject}/
│       ├── topics.json                # 主題列表（無子科目時）
│       └── {sub}/
│           ├── topics.json            # 主題列表（有子科目時）
│           ├── *.md                   # Markmap 心智圖內容
│           └── details/*.json         # 節點詳細資料
├── questions/
│   └── {subject}/{sub}/*.json         # 測驗題 JSON
└── scripts/
    ├── smoke-test.py                  # 煙霧測試
    ├── validate-chemistry.py          # 化學驗證
    └── add-tags.js                    # 標籤工具
```

## Architecture

Four-page structure with shared logic in `js/app.js`:

| Page | Purpose | Data Source |
|------|---------|-------------|
| `index.html` | Subject selector grid | `content/subjects.json` |
| `subject.html` | Sub-subject or topic listing | `content/{subject}/{sub}/topics.json` |
| `viewer.html` | Markmap mind map viewer + sidebar | `content/{subject}/{sub}/*.md` |
| `quiz.html` | Exam practice & scoring | `questions/{subject}/{sub}/*.json` |

Navigation flow: Homepage → select subject → (optional sub-subject) → viewer (merged mind map) or Quiz.

Routing uses URL query params (`?subject=science&sub=biology&topic=nervous-system`).

### Viewer Architecture

- Individual `.md` files fetched in parallel via `Promise.all`, merged at runtime
- Programmatic Markmap: `new Transformer().transform(md)` → `Markmap.create(svg, opts, root)`
- Both `markmap-lib` and `markmap-view` export to `window.markmap` global
- Sidebar with 2 tabs: 📘 概念與應用 / 🎯 考試準備
- Node completion tracked per-node in LocalStorage with ISO timestamps
- Detail JSON files (`content/{subject}/{sub}/details/{topic}.json`) provide `associations` and `examTips`
- Question JSON files (`questions/{subject}/{sub}/{topic}.json`) have `tags` arrays for node matching

## Code Style

- **camelCase** for JS functions/variables; **kebab-case** for CSS classes
- Section headers: `/* ===== SECTION NAME ===== */`
- Functions grouped by page feature: Homepage, Subject, Viewer, Quiz
- Use `async/await` for fetch calls with try/catch
- DOM creation via `document.createElement()` and `.innerHTML` string templates
- CSS follows BEM-like naming (`.card-icon`, `.btn-primary`)
- XSS prevention: use `escapeHtml()` for user-visible dynamic content

## Content Structure

- `content/subjects.json` — master subject index with hierarchy (subjects, sub-subjects)
- `content/{subject}/topics.json` — topics for subjects without sub-subjects (e.g., chinese, english, math)
- `content/{subject}/{sub}/topics.json` — topics for sub-subjects (e.g., science/biology, social/history)
- `content/{subject}/{sub}/*.md` — Markmap source; headers (`#`/`##`/`###`) define map nodes
- `content/{subject}/{sub}/details/*.json` — node detail data (associations, examTips)
- `questions/{subject}/{sub}/*.json` — multiple-choice questions with `answer`, `explanation`, and `tags`

Subjects with `hasSubjects: true` (自然, 社會) contain sub-subjects. Others are flat.

## Conventions

- All user-facing strings must be in Traditional Chinese
- English variable/function names in code
- CSS custom properties defined in `:root` for theming — use them instead of hardcoded colors
- Keep the project dependency-free (no npm packages); external libs loaded via CDN only
- Progress state stored in LocalStorage with `isRead(subjectId, subId, topicId)` / `markAsRead(...)` helpers
- Node-level progress stored as ISO timestamp via `toggleNodeCheck()` / `isNodeChecked()` / `getNodeCheckedTime()`

## Core Workflow

Every non-trivial feature follows this five-phase flow. Do NOT skip phases or merge them silently.

### Phase 1 — Clarify (planning agent)

Ask questions before writing any code. Output: shared understanding of scope, constraints, and acceptance criteria.

- Identify ambiguities and list them as numbered questions
- State assumptions explicitly — let the user confirm or correct
- Define **done** in measurable terms (e.g., "smoke-test passes", "quiz renders 5 questions")

### Phase 2 — Design (planning agent)

Produce a **sectioned design document** for incremental user approval. Do NOT proceed to Phase 3 until every section is confirmed.

- Break the design into logical sections (data schema → UI flow → edge cases)
- Present **one section at a time**; wait for user confirmation before the next
- Flag tradeoffs and alternatives — don't decide silently

### Phase 3 — Task Breakdown (planning agent)

Convert the approved design into a numbered task list. Each task should be completable in **2–5 minutes**.

- Format: `[Task N] → file: [path] → verify: [check]`
- Each task has a single, verifiable acceptance criterion
- Order tasks by dependency; independent tasks can be parallelized

### Phase 4 — TDD Implementation (coding agent)

For each task, follow a strict Red → Green → Refactor cycle:

1. **Red** — Write a failing test (or validation check) that captures the expected behavior
2. **Green** — Write the minimum code to make the test pass
3. **Refactor** — Clean up only what you just wrote, without changing behavior

In this project (no npm/test framework), "test" means:
- JSON schema: `python3 -c "import json; json.load(open('file'))"`
- File references: `python3 scripts/smoke-test.py`
- Manual verification: describe the expected UI state for the user to confirm

### Phase 5 — Review (reviewer agent)

After each task is implemented, perform a mini code review before moving to the next:

- Check changed files against Code Style and Conventions (this document)
- Verify no forbidden patterns (see **Do NOT** list)
- Confirm XSS prevention: all dynamic content uses `escapeHtml()`
- Confirm every changed line traces to the user's request (Surgical Changes)
- Report: `✅ pass` or list issues with severity and file references

---

**Skip/compress phases for trivial tasks** (typo fix, single-line config change). Use judgment.

## Behavioral Guidelines

Guidelines to reduce common LLM coding mistakes. Bias toward caution over speed; for trivial tasks, use judgment.

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, and clarifying questions come before implementation rather than after mistakes.

## Do NOT

- Add npm packages or build tools
- Introduce TypeScript or any framework
- Modify files outside the requested scope
- Use `markmap-autoloader` (use programmatic API instead)
- Use `window.markmapView` (both libs export to `window.markmap`)
