# Feature Specification: Mindmap-Highschool

**Created**: 2026-04-17
**Status**: Reverse-Engineered Draft
**Source**: 原始碼 + Git Log

---

## User Scenarios & Testing

### US1 — 瀏覽科目與主題 (Priority: P1) 🟢

**作為**台灣高中生，**我想要**在首頁看到所有學測科目並選擇進入，**以便**快速找到我要複習的科目。

**來源**: [CODE: index.html, js/app.js:212-254] [GIT: 1e2b336]

**Acceptance Scenarios**:
1. **Given** 首頁載入, **When** 頁面渲染完成, **Then** 顯示 5 個科目卡片（國文、英文、數學、自然、社會），含圖示、名稱、說明
2. **Given** 科目有子科目（自然、社會）, **When** 點擊該卡片, **Then** 導航至 `subject.html` 顯示子科目選擇
3. **Given** 科目無子科目（國文、數學）, **When** 點擊該卡片, **Then** 直接導航至 `viewer.html` 顯示合併心智圖
4. **Given** 子科目頁面, **When** 點擊子科目, **Then** 導航至合併心智圖（`viewer.html?subject=X&sub=Y`）

---

### US2 — 心智圖檢視與互動 (Priority: P1) 🟢

**作為**高中生，**我想要**以心智圖方式瀏覽學科知識，**以便**透過視覺化結構理解知識脈絡。

**來源**: [CODE: viewer.html:580-700] [GIT: 30603eb, 214874a]

**Acceptance Scenarios**:
1. **Given** 進入 viewer 頁面, **When** Markdown 載入完成, **Then** 使用 Markmap 渲染互動式心智圖（可 zoom/pan）
2. **Given** 多主題科目（如國文 21 篇）, **When** 無指定 topic param, **Then** 所有 .md 檔案並行載入後合併為單一心智圖
3. **Given** 合併模式 + groupByCategory, **When** 渲染, **Then** 按 categories/groups 階層合併（root → group → category → topic）
4. **Given** 指定 topic param, **When** 載入, **Then** 僅載入該主題的單一 .md 檔案
5. **Given** 心智圖節點, **When** 單擊, **Then** 展開/收合子節點（250ms debounce 避免與雙擊衝突）
6. **Given** 心智圖節點（有子節點）, **When** 雙擊, **Then** 開啟 Detail Sidebar

---

### US3 — Detail Sidebar 知識卡 (Priority: P1) 🟢

**作為**高中生，**我想要**點擊心智圖節點查看詳細資料，**以便**深入理解概念並準備考試。

**來源**: [CODE: viewer.html:990-1100] [GIT: 214874a, 5555213]

**Acceptance Scenarios**:
1. **Given** 雙擊一個有子節點的節點, **When** sidebar 開啟, **Then** 顯示兩個 tab：📘 概念與應用、🎯 考試準備
2. **Given** 概念 tab, **When** 節點有 detail JSON, **Then** 顯示 associations（💡 生活聯想）和子節點結構（遞迴深度 4 層）
3. **Given** 考試 tab, **When** 節點有匹配的 questions, **Then** 顯示考試重點 (examTips) + 歷屆考題（可作答）
4. **Given** sidebar 中的 Google 搜尋連結, **When** 點擊, **Then** 開啟 Google AI 搜尋（`udm=50` 參數）
5. **Given** sidebar checkbox, **When** 勾選「已完成複習」, **Then** 記錄 ISO 時間戳至 LocalStorage，心智圖上顯示綠色勾勾 + 時間

---

### US4 — 節點搜尋 (Priority: P2) 🟢

**作為**高中生，**我想要**在心智圖中搜尋特定節點，**以便**快速定位我需要的知識點。

**來源**: [CODE: viewer.html:1410-1600] [GIT: 1fd126e, d34f536, 50889da]

**Acceptance Scenarios**:
1. **Given** 點擊搜尋按鈕或按 Ctrl/Cmd+F, **When** 搜尋面板展開, **Then** Navbar 內 inline 展開 220px 輸入框
2. **Given** 輸入文字, **When** 150ms debounce 後, **Then** 顯示最多 20 筆匹配結果（含高亮 + 路徑麵包屑）
3. **Given** 選擇搜尋結果, **When** 點擊, **Then** 自動展開祖先節點 → zoom 至目標 → 3 次 pulse 動畫高亮
4. **Given** 搜尋結果中 depth ≥ 2 的節點, **When** 導航完成, **Then** 自動開啟 sidebar
5. **Given** 鍵盤, **When** ArrowUp/Down, **Then** 在結果中切換；Enter 確認選擇

---

### US5 — 題庫練習 (Priority: P1) 🟢

**作為**高中生，**我想要**做學測練習題並看到即時批改結果，**以便**檢驗我的學習成果。

**來源**: [CODE: quiz.html, js/app.js:420-510] [GIT: 6041fa4]

**Acceptance Scenarios**:
1. **Given** 進入 quiz.html, **When** 題庫 JSON 載入成功, **Then** 顯示所有題目（含題號、年份、題幹、4 選項）
2. **Given** 使用者選擇一個選項, **When** 點擊, **Then** 立即標示正確（綠）/錯誤（紅），顯示解析，禁止重選
3. **Given** 所有題目已作答, **When** 最後一題回答完, **Then** 顯示計分摘要（答對數/總數 + 答對率%），自動滾動至摘要
4. **Given** 計分摘要, **When** 點擊「重新作答」, **Then** 頁面重新載入

---

### US6 — 學習進度追蹤 (Priority: P2) 🟢

**作為**高中生，**我想要**追蹤我的學習進度，**以便**知道哪些內容已複習完畢。

**來源**: [CODE: js/app.js:86-198, viewer.html:792-800] [GIT: 214874a, 766609c, 682db0e, f67024b]

**Acceptance Scenarios**:
1. **Given** 心智圖 navbar, **When** 頁面載入, **Then** 顯示進度條（已勾選/可勾選節點數）
2. **Given** sidebar checkbox 勾選, **When** 狀態改變, **Then** 即時更新進度條 + 心智圖節點視覺
3. **Given** 離開 viewer 頁面, **When** beforeunload, **Then** 自動儲存 zoom/pan + fold 狀態
4. **Given** 重新開啟同一心智圖, **When** 頁面載入, **Then** 恢復上次的 zoom/pan + fold 狀態
5. **Given** subject.html 主題列表, **When** 頁面載入, **Then** 已讀主題卡片顯示 ✓ 標記

---

### US7 — KaTeX 公式渲染 (Priority: P2) 🟢

**作為**高中生，**我想要**看到正確渲染的數學公式，**以便**準確理解數學和物理概念。

**來源**: [CODE: viewer.html:1100-1190] [GIT: 5b4ab6e, 84e2743]

**Acceptance Scenarios**:
1. **Given** 心智圖中含 LaTeX 公式, **When** Markmap 渲染, **Then** KaTeX 自動渲染公式（由 markmap-lib KaTeX plugin 處理）
2. **Given** sidebar 中有 formulaDetails, **When** 開啟, **Then** 顯示公式卡片（LaTeX 渲染 + 符號表 + 幾何意義 + 考試重點）
3. **Given** 深色背景, **When** 公式渲染, **Then** 公式顏色繼承節點文字色（不被 KaTeX 預設白底覆蓋）

---

### US8 — Sidebar 寬度調整 (Priority: P3) 🟢

**來源**: [CODE: viewer.html:1348-1400] [GIT: 8539316]

**Acceptance Scenarios**:
1. **Given** sidebar 開啟, **When** 拖拉左邊 resize handle, **Then** 調整寬度（280px ~ 60vw）
2. **Given** 調整後, **When** 下次開啟, **Then** 記住上次的寬度偏好

---

## Requirements

### Functional Requirements
- **FR-001**: 科目索引載入與渲染 — [CODE: js/app.js:62-71, 212-254] 🟢
- **FR-002**: 多層級科目導航（subject → sub → topic） — [CODE: js/app.js:256-300] 🟢
- **FR-003**: Markmap 心智圖程式化渲染 — [CODE: viewer.html:700-720] 🟢
- **FR-004**: 多主題 Markdown 並行載入與合併 — [CODE: viewer.html:630-675] 🟢
- **FR-005**: Detail sidebar 雙 tab 內容展示 — [CODE: viewer.html:990-1100] 🟢
- **FR-006**: 節點完成狀態追蹤（ISO timestamp） — [CODE: js/app.js:118-140] 🟢
- **FR-007**: 題庫即時批改與計分 — [CODE: js/app.js:450-510] 🟢
- **FR-008**: 心智圖節點搜尋與導航 — [CODE: viewer.html:1410-1600] 🟢
- **FR-009**: Zoom/Pan/Fold 狀態持久化 — [CODE: js/app.js:160-197] 🟢
- **FR-010**: KaTeX 數學公式渲染 — [CODE: viewer.html:572, 1100-1190] 🟢
- **FR-011**: CSP + SRI 安全防護 — [CODE: index.html:5, viewer.html:576-577] 🟢
- **FR-012**: XSS 防護（escapeHtml + sanitizeHtml + isValidParam） — [CODE: js/app.js:4-55] 🟢
- **FR-013**: 響應式設計（mobile sidebar 全寬） — [CODE: viewer.html:479-486] 🟢
- **FR-014**: sidebar 題庫 tag 配對 — [CODE: viewer.html:1294-1308] 🟢

### Non-Functional Requirements
- **NFR-001**: 純靜態部署，無後端依賴 🟢
- **NFR-002**: GitHub Pages 自動部署（push to main） 🟢
- **NFR-003**: Zero npm — 所有外部庫透過 CDN 🟢
- **NFR-004**: 繁體中文 UI 🟢

## Success Criteria

- **SC-001**: 所有 HTML 頁面可正常載入（無 JS 錯誤） 🟢
- **SC-002**: topics.json 檔案參照完整（smoke-test 通過） 🟡 [目前 smoke-test 僅覆蓋化學]
- **SC-003**: 所有動態 DOM 操作使用 escapeHtml/sanitizeHtml 🟢
- **SC-004**: GitHub Pages 部署正常 🟢

## Assumptions
- 使用者使用現代瀏覽器（Chrome/Safari/Edge，ES2020+ 支援）
- 網路環境可存取 jsDelivr CDN
- 內容以 108 課綱為基礎
