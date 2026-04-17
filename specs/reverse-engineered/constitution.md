# Mindmap-Highschool Constitution

> 反向工程產出 | 基於 commit `2ddf3fa` | 2026-04-17

## Core Principles

### I. Zero-Dependency Static Architecture 🟢
專案不使用任何 npm 套件、bundler 或框架。所有外部函式庫（Markmap、D3、KaTeX）透過 CDN 引入，確保部署簡單且無 build step。
- **證據**: [CODE: CLAUDE.md — "No `package.json` exists"] [CODE: index.html — CDN script tags with SRI]
- **禁止**: npm install, TypeScript, 任何前端框架

### II. Vanilla JS with Programmatic Markmap 🟢
使用 `markmap-lib` + `markmap-view` 的 programmatic API（`Transformer.transform()` → `Markmap.create()`）而非 `markmap-autoloader`。兩個庫均匯出至 `window.markmap` 全域。
- **證據**: [CODE: viewer.html:574-579 — programmatic CDN import] [CODE: CLAUDE.md — "Do NOT use markmap-autoloader"]

### III. XSS Prevention as First-Class Concern 🟢
所有使用者可見的動態內容必須經過 `escapeHtml()` 或 `sanitizeHtml()` 處理。CSP header 限制腳本來源，CDN 腳本使用 SRI integrity 驗證。
- **證據**: [CODE: js/app.js:4-10 — escapeHtml] [CODE: js/app.js:16-51 — sanitizeHtml] [CODE: index.html:5 — CSP meta tag] [GIT: 9f8fa9d — "security: fix XSS, add SRI/CSP"]

### IV. Content-Driven Architecture 🟢
功能圍繞「內容」建構：Markdown → 心智圖、JSON → 題庫/詳細資料。新增科目只需增加 content/questions 目錄下的檔案並註冊到 `topics.json`，無需修改程式碼。
- **證據**: [CODE: content/subjects.json — master index] [CODE: js/app.js:78-84 — loadTopicsFor dynamic path resolution]

### V. Traditional Chinese UI / English Code 🟢
所有使用者介面文字使用繁體中文。程式碼中的變數名、函數名、註解使用英文。
- **證據**: [CODE: CLAUDE.md — "All user-facing strings must be in Traditional Chinese"] [CODE: js/app.js — camelCase naming throughout]

### VI. Surgical Changes 🟢
每次修改只觸及必要範圍。不改善鄰近程式碼、不重構未壞的東西、不增加未要求的功能。
- **證據**: [CODE: CLAUDE.md — "Surgical Changes" section] [CODE: AGENTS.md — all agents reference this principle]

## Development Workflow

### Local Development
```bash
python3 -m http.server 8000   # 本地伺服器
```
- 無 build step、無 hot reload
- 直接編輯 HTML/JS/CSS/MD/JSON 後瀏覽器重新整理

### Content Validation
```bash
python3 scripts/smoke-test.py          # 檔案參照驗證（需 localhost:8001）
python3 scripts/validate-chemistry.py  # 化學內容驗證
python3 -c "import json; json.load(open('path/to/file.json'))"  # JSON 格式驗證
```

### Deployment
- **自動部署**: push to `main` → GitHub Actions → GitHub Pages
- **流程**: checkout → upload-pages-artifact(path: '.') → deploy-pages
- 無 build/compile 步驟，整個 repo 直接部署
- **證據**: [CODE: .github/workflows/deploy.yml]

## Quality Gates

### Code Quality
- `escapeHtml()` / `sanitizeHtml()` — 所有動態 DOM 內容
- `isValidParam()` — URL query params 正則驗證 (`/^[a-z0-9-]+$/`)
- CSP meta tag — 限制 script-src, style-src 來源
- SRI integrity — CDN 腳本完整性驗證

### Content Quality
- `smoke-test.py` — topics.json 檔案參照完整性
- `validate-chemistry.py` — 化學科目特定驗證
- JSON 格式驗證 — `python3 -c "import json; ..."`

### AI Collaboration
- 三檔案架構：CLAUDE.md（核心）、copilot-instructions.md（行為映射）、AGENTS.md（角色流程）
- 6 個 Agent 角色：coding / content / planning / reviewer / testing / doc-writer
- 五階段工作流：Clarify → Design → Task Breakdown → TDD Implementation → Review

## Governance
- 本 Constitution 由原始碼反向工程產出
- 衝突時以 `CLAUDE.md` 為最終依據
- 所有 🟡🔴 標記項目建議由團隊審閱後正式批准

**Version**: 1.0.0-reverse-engineered | **Created**: 2026-04-17
