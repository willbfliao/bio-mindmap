# Research: Mindmap-Highschool

> 反向工程產出 | 2026-04-17

## 技術棧分析

| 類別 | 選擇 | 版本 | 來源 |
|------|------|------|------|
| Language | Vanilla JavaScript (ES2020+) | — | [CODE: js/app.js] 🟢 |
| Styling | Plain CSS + Custom Properties | — | [CODE: css/style.css] 🟢 |
| Mind Map | markmap-lib + markmap-view | 0.15.5 / 0.15.8 | [CODE: viewer.html:576-577] 🟢 |
| Math Rendering | KaTeX | 0.16.11 | [CODE: viewer.html:572] 🟢 |
| DOM/SVG | D3.js | 7.9.0 | [CODE: viewer.html:575] 🟢 |
| Deployment | GitHub Pages | — | [CODE: .github/workflows/deploy.yml] 🟢 |
| CI/CD | GitHub Actions | v4 | [CODE: .github/workflows/deploy.yml] 🟢 |
| Storage | LocalStorage | — | [CODE: js/app.js:98-196] 🟢 |
| Package Manager | 無（Zero npm） | — | [CODE: CLAUDE.md] 🟢 |
| Build Tool | 無（Zero build step） | — | [CODE: CLAUDE.md] 🟢 |

## 演進歷程

### 功能演進時間線

```
2026-03-21  專案誕生 — 生物心智圖互動學習網站
     │      多科目架構重構
     │      UX 改版 — 合併心智圖、側邊欄、節點完成狀態
     │      CI: GitHub Pages 部署
2026-03-22  物理科心智圖 + 題庫（5 主題）
     │      數學科心智圖 + 題庫（4 主題）
2026-03-25  心智圖節點搜尋功能
2026-03-28  化學科全面改版（23 主題、184 題）
     │      國文科古文十五篇
2026-03-31  國文國學常識 + 語文能力 6 主題
     │      Sidebar recursive rendering fix
2026-04-01  古文十五篇分組層級 + 跨題比較
2026-04-04  物理選修 I~V + 搜尋面板改 inline
2026-04-05  KaTeX 公式全面整合
2026-04-07  國文心智圖扁平化重構
2026-04-09  Zoom/Pan + Fold 狀態記憶
     │      國學常識錯誤修正
2026-04-11  單擊展開/雙擊 sidebar 交互邏輯
     │      學測名師 Skill
2026-04-14  生物完整課綱架構（必修＋選修 I~IV）
2026-04-16  三檔案 AI 協作架構
     │      Security: XSS/SRI/CSP 強化
     │      生物 31 主題加入考試重點
     │      數學內容擴充
2026-04-17  免疫系統內容 + sidebar 跨科 bug 修正
     │      Skills 結構重整
```

## 核心模組分析

| 排名 | 檔案 | 變更次數 | 風險評估 | 來源 |
|------|------|---------|---------|------|
| 1 | viewer.html | 23 | 高 — 最複雜，1634 行，含 inline JS/CSS | [GIT] 🟢 |
| 2 | js/app.js | 11 | 中 — 共用邏輯核心，510 行 | [GIT] 🟢 |
| 3 | css/style.css | 6 | 低 — 純樣式 | [GIT] 🟢 |
| 4 | content/chinese/*.md | 4-5 each | 低 — 純內容 | [GIT] 🟢 |
| 5 | index.html | 4 | 低 — 簡單，23 行 | [GIT] 🟢 |

### 風險觀察

| 觀察 | 原因 | 建議 | 來源 |
|------|------|------|------|
| viewer.html 過大（1634 行） | 所有 viewer 邏輯（JS+CSS）內嵌 | 考慮拆分 viewer JS 至獨立檔案 | [CODE: viewer.html] 🟡 |
| smoke-test.py 僅覆蓋化學 | 腳本 hardcode 化學檔案路徑 | 擴展為通用驗證腳本 | [CODE: scripts/smoke-test.py] 🟡 |
| 物理/生物題庫覆蓋率低 | 心智圖 27/34 個但題庫僅 5/8 個 | 補充題庫內容 | [GIT] 🟡 |

## 技術債分析

| 類型 | 數量 | 說明 | 來源 |
|------|------|------|------|
| TODO | 0 | 程式碼中無 TODO 標記 | [SCAN] 🟢 |
| FIXME | 0 | 程式碼中無 FIXME 標記 | [SCAN] 🟢 |
| HACK | 0 | 程式碼中無 HACK 標記 | [SCAN] 🟢 |

## CDN 依賴清單

| 套件 | CDN | SRI | 用途 |
|------|-----|-----|------|
| d3 v7.9.0 | jsDelivr | ✅ | SVG 操作、zoom/pan |
| markmap-lib v0.15.5 | jsDelivr | ✅ | Markdown → Markmap tree 轉換 |
| markmap-view v0.15.8 | jsDelivr | ✅ | Markmap SVG 渲染 |
| KaTeX v0.16.11 | jsDelivr | ✅ | 數學公式渲染 |
| KaTeX CSS v0.16.11 | jsDelivr | ✅ | 公式樣式 |
