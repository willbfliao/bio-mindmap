# Project Guidelines

## Overview

Bio-Mindmap is a **static** educational web app for Taiwan high school students. It displays multi-subject content as interactive mind maps (via Markmap) and provides exam practice questions. Subjects include 國文, 英文, 數學, 自然 (物理/化學/生物/地科), and 社會 (歷史/地理/公民). All UI text is in **Traditional Chinese (繁體中文)**.

## Tech Stack

- **Vanilla JS** — no framework, no TypeScript, no bundler
- **Markmap** via CDN (`jsDelivr`) for mind map rendering
- **Plain CSS** with CSS custom properties for theming
- **LocalStorage** for read/completion progress tracking
- **GitHub Pages** deployment (auto via GitHub Actions on push to `main`)

No `package.json` exists. To serve locally: `python3 -m http.server 8000` or `npx http-server`.

## Architecture

Four-page structure with shared logic in `js/app.js`:

| Page | Purpose | Data Source |
|------|---------|-------------|
| `index.html` | Subject selector grid | `content/subjects.json` |
| `subject.html` | Sub-subject or topic listing | `content/{subject}/{sub}/topics.json` |
| `viewer.html` | Markmap mind map viewer | `content/{subject}/{sub}/*.md` |
| `quiz.html` | Exam practice & scoring | `questions/{subject}/{sub}/*.json` |

Navigation flow: Homepage → select subject → (optional sub-subject) → select topic → Viewer or Quiz.

Routing uses URL query params (`?subject=science&sub=biology&topic=nervous-system`).

## Code Style

- **camelCase** for JS functions/variables; **kebab-case** for CSS classes
- Section headers: `/* ===== SECTION NAME ===== */`
- Functions grouped by page feature: Homepage, Subject, Viewer, Quiz
- Use `async/await` for fetch calls with try/catch
- DOM creation via `document.createElement()` and `.innerHTML` string templates
- CSS follows BEM-like naming (`.card-icon`, `.btn-primary`)

## Content Structure

- `content/subjects.json` — master subject index with hierarchy (subjects, sub-subjects)
- `content/{subject}/topics.json` — topics for subjects without sub-subjects (e.g., chinese, english, math)
- `content/{subject}/{sub}/topics.json` — topics for sub-subjects (e.g., science/biology, social/history)
- `content/{subject}/{sub}/*.md` — Markmap source; headers (`#`/`##`/`###`) define map nodes
- `questions/{subject}/{sub}/*.json` — multiple-choice questions with `answer` (letter) and `explanation`

Subjects with `hasSubjects: true` (自然, 社會) contain sub-subjects. Others are flat.

## Conventions

- All user-facing strings must be in Traditional Chinese
- English variable/function names in code
- CSS custom properties defined in `:root` for theming — use them instead of hardcoded colors
- Keep the project dependency-free (no npm packages); external libs loaded via CDN only
- Progress state stored in LocalStorage with `isRead(subjectId, subId, topicId)` / `markAsRead(...)` helpers
