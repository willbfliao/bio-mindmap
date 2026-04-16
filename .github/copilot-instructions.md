# Copilot Instructions

> 所有代碼生成必須嚴格遵循專案根目錄 `CLAUDE.md` 中的規範。
> 本檔案僅定義 GitHub Copilot 的工具行為偏好，不重複 `CLAUDE.md` 的規則。

## 規範引用

執行任何任務前，必須先參考 `CLAUDE.md` 取得：
- Tech Stack & Architecture
- Code Style & Conventions
- Content Structure
- Core Workflow (Clarify → Design → Task Breakdown → TDD Implementation → Review)
- Behavioral Guidelines (Think Before Coding / Simplicity First / Surgical Changes / Goal-Driven Execution)
- Do NOT 清單

角色定義與 SOP 請參考 `AGENTS.md`。

## 回應風格

- 簡潔回覆，避免解釋已知概念
- 繁體中文為使用者溝通語言
- 英文用於程式碼（變數名、函數名、註解）
- 有不確定時先問，不要猜

## 程式碼生成偏好

- Vanilla JS only — 禁止引入任何框架或 TypeScript
- 使用 `async/await` + `try/catch`，不用 `.then()` chain
- DOM 操作使用 `document.createElement()` 或 `.innerHTML` template
- 動態內容必須使用 `escapeHtml()` 防止 XSS
- CSS 使用 `:root` custom properties，不使用 hardcoded 色碼
- 外部套件僅限 CDN 引入，禁止 npm

## 工具行為約束

- 編輯前必須先讀取目標檔案
- 每次變動僅觸及必要範圍（參照 `CLAUDE.md` → Surgical Changes）
- JSON 檔案修改後驗證：`python3 -c "import json; json.load(open('file'))"`
- 新增主題後須更新對應 `topics.json` 並執行 `python3 scripts/smoke-test.py`
