# API Contracts: Mindmap-Highschool

> 反向工程產出 | 2026-04-17

## REST Endpoints

**N/A** — 本專案為純靜態網站，無後端 API。

所有資料透過 `fetch()` 直接讀取靜態 JSON/Markdown 檔案。

---

## Static File Fetch Contracts 🟢

以下為前端 JavaScript 透過 `fetch()` 存取的靜態檔案路徑：

| Method | Path | Handler | 描述 | 來源 |
|--------|------|---------|------|------|
| GET | `content/subjects.json` | `loadSubjects()` | 載入科目索引 | [CODE: js/app.js:62-71] |
| GET | `content/{subject}/topics.json` | `loadTopicsFor()` | 載入主題列表（無子科目） | [CODE: js/app.js:78-82] |
| GET | `content/{subject}/{sub}/topics.json` | `loadTopicsFor()` | 載入主題列表（有子科目） | [CODE: js/app.js:78-82] |
| GET | `content/{subject}/{sub}/*.md` | viewer inline | 載入心智圖 Markdown | [CODE: viewer.html:609-675] |
| GET | `content/{subject}/{sub}/details/{topic}.json` | viewer inline | 載入節點詳細資料 | [CODE: viewer.html:803-807] |
| GET | `questions/{subject}/{sub}/{topic}.json` | viewer inline / `initQuiz()` | 載入題庫 | [CODE: viewer.html:809-813] |

### 回應格式

所有回應為純文字（Markdown）或 JSON。無自訂 HTTP header。
錯誤處理：HTTP status ≠ 200 時 catch → 顯示「無法載入」提示或靜默忽略。

---

## URL Routing Contracts 🟢

路由透過 URL query parameters 實作，無 hash routing。

| Page | URL Pattern | 必要 Params | 可選 Params | 來源 |
|------|-------------|-------------|-------------|------|
| 首頁 | `index.html` | — | — | [CODE: index.html] |
| 科目列表 | `subject.html?subject={id}` | subject | sub | [CODE: js/app.js:244] |
| 心智圖 | `viewer.html?subject={id}` | subject | sub, topic | [CODE: viewer.html:588] |
| 題庫 | `quiz.html?subject={id}&topic={id}` | subject, topic | sub | [CODE: js/app.js:424] |

### 參數驗證

所有 URL params 經 `isValidParam()` 驗證：`/^[a-z0-9-]+$/`。
不合法參數 → redirect 至 `index.html`。

- **來源**: [CODE: js/app.js:53-55]
