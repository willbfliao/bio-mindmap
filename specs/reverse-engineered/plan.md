# Implementation Plan: Mindmap-Highschool

**Date**: 2026-04-17 | **Spec**: [./spec.md](./spec.md)

## Summary

Mindmap-Highschool 是一個面向台灣高中生的靜態教育網站，使用 Markmap 將學科知識以心智圖方式呈現，搭配測驗題庫與進度追蹤功能。專案採用零依賴架構（Vanilla JS + CDN），透過 GitHub Pages 自動部署。

## Technical Context

| 項目 | 值 | 來源 |
|------|-----|------|
| **Language/Version** | Vanilla JavaScript (ES2020+) | [CODE: js/app.js] 🟢 |
| **Styling** | Plain CSS + Custom Properties | [CODE: css/style.css] 🟢 |
| **Primary Dependencies** | markmap-lib 0.15.5, markmap-view 0.15.8, d3 7.9.0, KaTeX 0.16.11 | [CODE: viewer.html] 🟢 |
| **Storage** | LocalStorage (browser) | [CODE: js/app.js] 🟢 |
| **Testing** | Python scripts (smoke-test.py) | [CODE: scripts/] 🟢 |
| **Target Platform** | GitHub Pages (static hosting) | [CODE: .github/workflows/deploy.yml] 🟢 |
| **Project Type** | Static educational web app | [INFER: 無後端] 🟢 |
| **Build Step** | 無 | [CODE: CLAUDE.md] 🟢 |

## Constitution Check
- [x] Zero-Dependency Static Architecture — [CODE: 無 package.json]
- [x] Vanilla JS with Programmatic Markmap — [CODE: viewer.html]
- [x] XSS Prevention as First-Class Concern — [CODE: js/app.js:4-55]
- [x] Content-Driven Architecture — [CODE: content/ 目錄結構]
- [x] Traditional Chinese UI / English Code — [CODE: 全站]
- [x] Surgical Changes — [CODE: CLAUDE.md]

## Project Structure

```
mindmap-highschool/
├── index.html              # 首頁：科目選擇 grid
├── subject.html            # 科目頁：子科目/主題列表
├── viewer.html             # 心智圖檢視器（最複雜，1634 行）
│                           #   含 inline CSS + JS：Markmap 渲染、
│                           #   Sidebar、搜尋、進度、KaTeX
├── quiz.html               # 題庫頁：多選題作答 + 計分
├── js/
│   └── app.js              # 共用核心邏輯（510 行）
│                           #   工具函數、LocalStorage helpers、
│                           #   Homepage/Subject/Quiz 初始化
├── css/
│   └── style.css           # 全域樣式（515 行）
│                           #   :root CSS vars、Grid、Card、Nav
├── content/
│   ├── subjects.json       # 科目索引（5 科目 + 子科目）
│   ├── {subject}/
│   │   ├── topics.json     # 主題列表（含 categories/groups）
│   │   ├── *.md            # Markmap 心智圖內容
│   │   └── details/*.json  # 節點詳細資料（associations, examTips）
│   └── {subject}/{sub}/    # 子科目結構（同上）
├── questions/
│   └── {subject}/{sub}/*.json  # 題庫 JSON
├── scripts/
│   ├── smoke-test.py       # 煙霧測試（僅化學）
│   ├── validate-chemistry.py  # 化學驗證
│   └── add-tags.js         # 標籤工具
└── .github/
    ├── workflows/deploy.yml    # GitHub Pages 自動部署
    ├── copilot-instructions.md # AI 行為映射
    └── agents/*.agent.md       # 6 個 Agent prompt
```

## Complexity Tracking

| 觀察 | 原因 | 影響 | 來源 |
|------|------|------|------|
| viewer.html 1634 行含 inline JS+CSS | 初期快速開發，未拆分 | 維護性降低，修改風險高 | [CODE] 🟡 |
| smoke-test.py 僅覆蓋化學 | 腳本建立時僅有化學內容 | 其他科目變更無自動驗證 | [CODE] 🟡 |
| LocalStorage prefix 仍為 `bio-mindmap-` | 源自生物科目起點 | 功能正常但語義不精確 | [CODE: js/app.js:3] 🟡 |
| 5 科目內容為空 | 尚在開發中 | 英文/地科/歷史/地理/公民頁面顯示空白 | [SCAN] 🟡 |
| 物理/生物題庫覆蓋率低 | 優先開發心智圖內容 | 部分主題無題庫可練習 | [SCAN] 🟡 |

## Content Coverage Matrix

| 科目 | 心智圖(.md) | 題庫(.json) | 詳細(.json) | 完整度 |
|------|------------|-------------|-------------|--------|
| 國文 chinese | 21 | 21 | 21 | ✅ 100% |
| 英文 english | 0 | 0 | 0 | ❌ 0% |
| 數學 math | 4 | 4 | 4 | ✅ 100% |
| 物理 physics | 27 | 5 | 5 | ⚠️ 19% 題庫 |
| 化學 chemistry | 27 | 26 | 26 | ✅ 96% |
| 生物 biology | 34 | 8 | 8 | ⚠️ 24% 題庫 |
| 地科 earth-science | 0 | 0 | 0 | ❌ 0% |
| 歷史 history | 0 | 0 | 0 | ❌ 0% |
| 地理 geography | 0 | 0 | 0 | ❌ 0% |
| 公民 civics | 0 | 0 | 0 | ❌ 0% |

## Page Architecture

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│ index.html  │────→│ subject.html │────→│ viewer.html  │
│ 科目選擇     │     │ 子科目/主題   │     │ 心智圖檢視器  │
│ initHomepage│     │ initSubject  │     │ (inline IIFE)│
└─────────────┘     └──────┬───────┘     └──────┬───────┘
                           │                     │
                           │              ┌──────┴───────┐
                           └─────────────→│  quiz.html   │
                                          │  題庫練習     │
                                          │  initQuiz    │
                                          └──────────────┘

共用: js/app.js (所有頁面載入)
      css/style.css (所有頁面載入)
```

## Data Flow

```
[content/subjects.json]
        │ fetch()
        ▼
  loadSubjects() → 科目卡片渲染
        │
[content/{s}/{sub}/topics.json]
        │ fetch()
        ▼
  loadTopicsFor() → 主題列表 or 心智圖載入
        │
  ┌─────┴──────────────────┐
  │ Viewer (parallel fetch) │
  │ *.md → Transformer     │
  │ → Markmap.create(svg)  │
  │                         │
  │ details/*.json → cache │
  │ questions/*.json → cache│
  └────────────────────────┘
        │
  [LocalStorage]
  ├── read status
  ├── node completion (ISO timestamp)
  ├── view transform (k, x, y)
  ├── fold state
  └── sidebar width
```
