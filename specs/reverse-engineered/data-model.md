# Data Model: Mindmap-Highschool

> 反向工程產出 | 2026-04-17
> **Source**: [CODE: content/, questions/, js/app.js, viewer.html]

本專案無後端資料庫。所有持久化資料分兩類：
1. **靜態內容** — JSON + Markdown 檔案（Git 版控）
2. **使用者狀態** — LocalStorage（瀏覽器端）

---

## 靜態內容實體

### subjects.json（科目索引）🟢
- **路徑**: `content/subjects.json`
- **角色**: 全站科目結構的唯一入口

| 欄位 | 型別 | 約束 | 說明 | 來源 |
|------|------|------|------|------|
| title | string | required | 網站標題 | [CODE: content/subjects.json:2] |
| subtitle | string | required | 網站副標題 | [CODE: content/subjects.json:3] |
| subjects[] | array | required | 科目清單 | [CODE: content/subjects.json:4] |
| subjects[].id | string | required, kebab-case | 科目 ID（URL param） | [CODE] |
| subjects[].title | string | required | 中文名稱 | [CODE] |
| subjects[].titleEn | string | required | 英文名稱 | [CODE] |
| subjects[].icon | string | required | Emoji 圖示 | [CODE] |
| subjects[].color | string | required | Hex 色碼 | [CODE] |
| subjects[].description | string | required | 說明文字 | [CODE] |
| subjects[].hasSubjects | boolean | required | 是否有子科目 | [CODE] |
| subjects[].subSubjects[] | array | optional | 子科目清單（hasSubjects=true 時） | [CODE] |
| subSubjects[].id | string | required | 子科目 ID | [CODE] |
| subSubjects[].title | string | required | 中文名稱 | [CODE] |
| subSubjects[].titleEn | string | required | 英文名稱 | [CODE] |
| subSubjects[].icon | string | required | Emoji 圖示 | [CODE] |
| subSubjects[].color | string | required | Hex 色碼 | [CODE] |

### topics.json（主題列表）🟢
- **路徑**: `content/{subject}/topics.json` 或 `content/{subject}/{sub}/topics.json`
- **角色**: 每個科目/子科目的主題索引

| 欄位 | 型別 | 約束 | 說明 | 來源 |
|------|------|------|------|------|
| title | string | required | 科目心智圖標題 | [CODE] |
| subtitle | string | required | 副標題 | [CODE] |
| groupByCategory | boolean | optional | 合併時是否按分類分組 | [CODE: viewer.html:639] |
| categories[] | array | required | 分類清單 | [CODE] |
| categories[].id | string | required | 分類 ID | [CODE] |
| categories[].name | string | required | 分類名稱 | [CODE] |
| categories[].group | string | optional | 上層分組名稱（僅 groupByCategory=true 時） | [CODE: viewer.html:650] |
| categories[].tag | string | optional | 分類標籤（如「必修」「選修」） | [CODE: js/app.js:361] |
| categories[].topics[] | array | required | 主題清單 | [CODE] |
| topics[].id | string | required | 主題 ID（= 檔名） | [CODE] |
| topics[].file | string | required | .md 檔名 | [CODE] |
| topics[].title | string | required | 中文標題 | [CODE] |
| topics[].titleEn | string | required | 英文標題 | [CODE] |
| topics[].icon | string | required | Emoji | [CODE] |
| topics[].color | string | optional | Hex 色碼 | [CODE] |
| topics[].examRatio | number | required | 學測佔比（%） | [CODE: js/app.js:387] |
| topics[].questionCount | number | optional | 題目數量 | [CODE] |

### Markmap Content（心智圖 Markdown）🟢
- **路徑**: `content/{subject}/{sub}/*.md`
- **格式**: Markmap-compatible Markdown
- **規則**: `#` = 根節點、`##` = 主分類、`###` = 子分類、以此類推
- **來源**: [CODE: content/chinese/rhetoric.md]

### Detail JSON（節點詳細資料）🟢
- **路徑**: `content/{subject}/{sub}/details/{topic}.json`

| 欄位 | 型別 | 說明 | 來源 |
|------|------|------|------|
| nodes | object | key = 節點文字, value = 節點資料 | [CODE: content/chinese/details/rhetoric.json] |
| nodes[key].associations | string[] | 生活聯想與應用 | [CODE] |
| nodes[key].examTips | string[] | 考試重點提示 | [CODE] |
| nodes[key].formulaDetails | object[] | 公式卡片（數學/物理用） | [CODE: viewer.html:1103] |
| formulaDetails[].title | string | 公式名稱 | [CODE] |
| formulaDetails[].latex | string | KaTeX LaTeX 字串 | [CODE] |
| formulaDetails[].symbols | object[] | 符號解析 {symbol, name, type} | [CODE] |
| formulaDetails[].geometricMeaning | string | 幾何意義 | [CODE] |
| formulaDetails[].examTips | string[] | 考試重點 | [CODE] |

### Question JSON（題庫）🟢
- **路徑**: `questions/{subject}/{sub}/{topic}.json`

| 欄位 | 型別 | 說明 | 來源 |
|------|------|------|------|
| topicId | string | 對應主題 ID | [CODE: questions/chinese/rhetoric.json:2] |
| year_stats | string | 年份統計說明 | [CODE: js/app.js:459] |
| questions[] | array | 題目清單 | [CODE] |
| questions[].id | string | 題目 ID（如 "q1"） | [CODE] |
| questions[].text | string | 題幹文字 | [CODE] |
| questions[].options | string[] | 選項（通常 4 個） | [CODE] |
| questions[].answer | string | 正確答案（"A"/"B"/"C"/"D"） | [CODE] |
| questions[].explanation | string | 解析說明 | [CODE] |
| questions[].tags | string[] | 關聯節點標籤（用於 sidebar 配對） | [CODE: viewer.html:1302] |
| questions[].year | number | optional | 學測年份 | [CODE: js/app.js:465] |

---

## LocalStorage 資料模型 🟢

所有 key 以 `bio-mindmap-` 為前綴。

| Key Pattern | Value | 用途 | 來源 |
|-------------|-------|------|------|
| `bio-mindmap-read-{subject}-{sub?}-{topic}` | `"1"` | 主題已讀標記 | [CODE: js/app.js:88-106] |
| `bio-mindmap-node-{subject}-{sub?}-{...path}` | ISO timestamp 或 `"1"` | 節點完成時間戳 | [CODE: js/app.js:118-140] |
| `bio-mindmap-last-{subject}` | `{"sub":"...","topic":"..."}` JSON | 科目上次瀏覽位置 | [CODE: js/app.js:144-156] |
| `bio-mindmap-view-{subject}-{sub?}-{topic?}` | `{"k":number,"x":number,"y":number}` JSON | Zoom/Pan 變換矩陣 | [CODE: js/app.js:164-178] |
| `bio-mindmap-fold-{subject}-{sub?}-{topic?}` | `{path: foldValue}` JSON | 展開/收合狀態 | [CODE: js/app.js:184-197] |
| `bio-mindmap-sidebar-width` | number string | Sidebar 寬度偏好 | [CODE: viewer.html:1380] |

---

## 實體關係

```
subjects.json
  └── Subject (id, title, hasSubjects)
        ├── [hasSubjects=false] → topics.json → Topic → *.md + details/*.json + questions/*.json
        └── [hasSubjects=true] → SubSubject (id, title)
              └── topics.json → Topic → *.md + details/*.json + questions/*.json

Topic ──1:1──→ Markdown (.md)
Topic ──1:0..1→ Detail JSON (details/{id}.json)
Topic ──1:0..1→ Question JSON (questions/{id}.json)

Detail.nodes[key] ──tag match──→ Question.questions[].tags
```
