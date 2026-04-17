# Tasks: Mindmap-Highschool — 現有功能盤點

**Input**: spec.md + plan.md + 掃描資料

## Format: `[ID] [Status] [Story] Description`

- **[✅]**: 已實作（程式碼存在）
- **[⚠️]**: 部分實作或有問題
- **[❌]**: 規格應有但缺失

---

## Phase 1: 基礎設施

- [✅] T001 [Infra] 專案結構建立 — [CODE: 全目錄結構]
- [✅] T002 [Infra] GitHub Pages 自動部署 — [CODE: .github/workflows/deploy.yml] [GIT: 90ea8d7]
- [✅] T003 [Infra] CSP + SRI 安全 header — [CODE: index.html:5] [GIT: 9f8fa9d]
- [✅] T004 [Infra] 共用 CSS 與 :root custom properties — [CODE: css/style.css]
- [✅] T005 [Infra] 共用 JS 工具函數（escapeHtml, sanitizeHtml, isValidParam） — [CODE: js/app.js:1-90]
- [✅] T006 [Infra] AI 協作架構（CLAUDE.md + copilot-instructions + AGENTS.md） — [GIT: 0d7fe85]
- [⚠️] T007 [Infra] 煙霧測試腳本 — 僅覆蓋化學科目 — [CODE: scripts/smoke-test.py]

---

## Phase 2: US1 — 瀏覽科目與主題 (P1) 🎯

- [✅] T010 [US1] subjects.json 科目索引資料 — [CODE: content/subjects.json]
- [✅] T011 [US1] 首頁科目選擇 grid 渲染 — [CODE: js/app.js:212-254]
- [✅] T012 [US1] subject.html 子科目卡片渲染 — [CODE: js/app.js:298-324]
- [✅] T013 [US1] subject.html 主題列表渲染（含進度條） — [CODE: js/app.js:326-410]
- [✅] T014 [US1] URL query param 路由 + 參數驗證 — [CODE: js/app.js:53-58]
- [✅] T015 [US1] 無子科目科目直接進入 viewer — [CODE: js/app.js:236]

---

## Phase 3: US2 — 心智圖檢視與互動 (P1) 🎯

- [✅] T020 [US2] Markmap CDN 載入（markmap-lib + markmap-view + d3） — [CODE: viewer.html:575-577]
- [✅] T021 [US2] Markdown 載入與 Transformer.transform() — [CODE: viewer.html:700-705]
- [✅] T022 [US2] Markmap.create() 程式化渲染 — [CODE: viewer.html:710-716]
- [✅] T023 [US2] 多主題並行 fetch + 合併 — [CODE: viewer.html:630-675]
- [✅] T024 [US2] groupByCategory 分層合併邏輯 — [CODE: viewer.html:641-666]
- [✅] T025 [US2] 單主題模式（?topic=X） — [CODE: viewer.html:609-627]
- [✅] T026 [US2] 單擊展開/收合（250ms debounce） — [CODE: viewer.html:864-870]
- [✅] T027 [US2] 雙擊開啟 sidebar — [CODE: viewer.html:872-875]
- [✅] T028 [US2] 節點視覺：可點擊（紫色）/ 已完成（綠色）/ 非互動（灰色） — [CODE: viewer.html:303-337]

---

## Phase 4: US3 — Detail Sidebar (P1) 🎯

- [✅] T030 [US3] Sidebar 滑入/滑出動畫 — [CODE: viewer.html:32-36]
- [✅] T031 [US3] 雙 Tab 切換（概念/考試） — [CODE: viewer.html:1006-1012]
- [✅] T032 [US3] 概念 tab：遞迴子節點渲染（最深 4 層） — [CODE: viewer.html:1207-1250]
- [✅] T033 [US3] 概念 tab：associations 生活聯想卡片 — [CODE: viewer.html:1253-1268]
- [✅] T034 [US3] 考試 tab：examTips 考試重點 — [CODE: viewer.html:1085-1098]
- [✅] T035 [US3] 考試 tab：tag 配對歷屆考題 — [CODE: viewer.html:1294-1308]
- [✅] T036 [US3] sidebar 內答題互動 — [CODE: viewer.html:1316-1334]
- [✅] T037 [US3] sidebar checkbox（節點完成） — [CODE: viewer.html:1050-1070]
- [✅] T038 [US3] Google AI 搜尋連結 — [CODE: viewer.html:1228-1234]
- [✅] T039 [US3] sidebar 跨科 detail 配對 scoping — [GIT: 5555213, 560b7f4]

---

## Phase 5: US4 — 節點搜尋 (P2)

- [✅] T040 [US4] Navbar inline 搜尋面板 — [CODE: viewer.html:1410-1430]
- [✅] T041 [US4] 即時搜尋（150ms debounce） — [CODE: viewer.html:1456]
- [✅] T042 [US4] 搜尋結果列表（最多 20 筆 + 高亮） — [CODE: viewer.html:1470-1510]
- [✅] T043 [US4] 導航至節點（展開祖先 + zoom + highlight） — [CODE: viewer.html:1546-1590]
- [✅] T044 [US4] 鍵盤導航（Arrow + Enter + Escape） — [CODE: viewer.html:1520-1540, 1598-1605]
- [✅] T045 [US4] Ctrl/Cmd+F 快捷鍵 — [CODE: viewer.html:1598]

---

## Phase 6: US5 — 題庫練習 (P1) 🎯

- [✅] T050 [US5] quiz.html 頁面結構 — [CODE: quiz.html]
- [✅] T051 [US5] 題庫 JSON 載入 — [CODE: js/app.js:444-450]
- [✅] T052 [US5] 題目渲染（題號 + 年份 + 選項） — [CODE: js/app.js:455-495]
- [✅] T053 [US5] 即時批改（正確/錯誤標示 + 解析顯示） — [CODE: js/app.js:476-492]
- [✅] T054 [US5] 計分摘要 — [CODE: js/app.js:497-510]

---

## Phase 7: US6 — 學習進度追蹤 (P2)

- [✅] T060 [US6] 已讀狀態 LocalStorage — [CODE: js/app.js:86-106]
- [✅] T061 [US6] 節點完成狀態（ISO timestamp） — [CODE: js/app.js:118-140]
- [✅] T062 [US6] 進度條（navbar + subject page） — [CODE: viewer.html:792-800, js/app.js:337-340]
- [✅] T063 [US6] zoom/pan 狀態持久化 — [CODE: js/app.js:160-178] [GIT: 766609c]
- [✅] T064 [US6] fold 狀態持久化 — [CODE: js/app.js:184-197] [GIT: f67024b]
- [✅] T065 [US6] 科目上次位置記憶 — [CODE: js/app.js:144-156] [GIT: 682db0e]

---

## Phase 8: US7 — KaTeX 公式渲染 (P2)

- [✅] T070 [US7] KaTeX CDN 載入 — [CODE: viewer.html:572-573]
- [✅] T071 [US7] 心智圖內公式渲染（markmap-lib plugin） — [CODE: viewer.html:571 — "must load BEFORE markmap-lib"]
- [✅] T072 [US7] sidebar 公式卡片渲染 — [CODE: viewer.html:1100-1190]
- [✅] T073 [US7] 深色背景公式顏色修正 — [CODE: viewer.html:284-298]

---

## Phase 9: US8 — Sidebar 寬度調整 (P3)

- [✅] T080 [US8] resize handle 拖拉 — [CODE: viewer.html:1348-1400]
- [✅] T081 [US8] 寬度 LocalStorage 持久化 — [CODE: viewer.html:1380, 1392]
- [✅] T082 [US8] 響應式：mobile 全寬 — [CODE: viewer.html:479-482]

---

## Phase 10: 內容

- [✅] T090 [Content] 國文：古文十五篇 + 國學常識 + 語文能力（21 主題） — [GIT: 34a811a..9794751]
- [✅] T091 [Content] 數學：4 主題 — [GIT: 97e46dc, b3e0946]
- [✅] T092 [Content] 物理：必修 + 選修 I~V（27 主題） — [GIT: 6041fa4, a20eece]
- [✅] T093 [Content] 化學：108課綱 23 主題 — [GIT: 756840c]
- [✅] T094 [Content] 生物：必修 + 選修 I~IV（34 主題） — [GIT: a1c32f2, 373eaa7]
- [❌] T095 [Content] 英文：尚無內容
- [❌] T096 [Content] 地球科學：尚無內容
- [❌] T097 [Content] 歷史：尚無內容
- [❌] T098 [Content] 地理：尚無內容
- [❌] T099 [Content] 公民與社會：尚無內容

---

## 缺口分析

| 缺口 | 嚴重度 | 相關 | 來源 | 建議 |
|------|-------|------|------|------|
| 5 科目完全空白 | 中 | T095-T099 | [SCAN] | 依優先順序逐步開發 |
| 物理題庫覆蓋率 19%（5/27） | 中 | T092 | [SCAN] | 補充 22 主題題庫 |
| 生物題庫覆蓋率 24%（8/34） | 中 | T094 | [SCAN] | 補充 26 主題題庫 |
| smoke-test.py 僅化學 | 低 | T007 | [CODE] | 擴展為通用驗證 |
| viewer.html 1634 行未拆分 | 低 | — | [CODE] | 考慮拆分 viewer JS |
| LocalStorage prefix `bio-mindmap-` | 低 | — | [CODE] | 語義不精確但功能正常 |
