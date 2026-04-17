# Reverse-Engineering Checklist: Mindmap-Highschool

**Created**: 2026-04-17

## 來源驗證
- [x] CHK001 所有 User Story 有 [CODE] 或 [GIT] 來源標注
- [x] CHK002 所有 FR 有 [CODE: file:line] 標注
- [x] CHK003 技術棧與實際 CDN 引入一致 — viewer.html script tags 已驗證
- [ ] CHK004 API 端點與路由定義交叉驗證 — N/A（無後端 API）
- [x] CHK005 資料模型與實際 JSON 檔案交叉驗證 — 已核對 topics.json, details/*.json, questions/*.json schema

## 使用者確認追蹤
- [x] CHK006 掃描報告呈現，使用者確認「功能已完整」
- [ ] CHK007 Phase 4 審閱 — 待使用者確認
- [x] CHK008 所有 [NEEDS CONFIRMATION] 已處理 — 無未解項目

## 完整性
- [x] CHK009 所有入口點已識別 — index.html, subject.html, viewer.html, quiz.html
- [x] CHK010 所有外部依賴已列於 research.md — markmap-lib, markmap-view, d3, KaTeX
- [x] CHK011 Edge Cases 已從 fix commits 提取 — 跨科 sidebar 配對、搜尋被 sidebar 遮住、fold 狀態記憶
- [x] CHK012 使用者確認可追溯 — 使用者回覆「應已完整」

## 品質
- [x] CHK013 未包含 LLM 臆測的不存在功能 — 全部有 CODE/GIT 證據
- [ ] CHK014 Mermaid 語法正確 — 本套文件未使用 Mermaid（plan.md 用 ASCII art）
- [x] CHK015 所有檔案路徑在 codebase 中存在 — 已通過 file scan 驗證
- [x] CHK016 敏感資訊已排除 — 專案無密鑰/token

## 信心度統計
- 🟢 高: 62 項（91%）— 有程式碼直接證據
- 🟡 中: 6 項（9%）— 程式碼有跡象但為建議性質（viewer 拆分、smoke-test 擴展等）
- 🔴 低: 0 項（0%）
- **結果**: ✅ 達標（🟢 > 70%，🔴 < 10%）

## 人工審閱
- [ ] CHK017 領域專家確認 spec.md — 8 個 User Story 是否涵蓋所有核心場景
- [ ] CHK018 架構師確認 constitution.md — 6 項核心原則是否正確
- [ ] CHK019 開發者確認 tasks.md — 82 個 task status 是否準確
- [ ] CHK020 所有文件間無矛盾 — 待交叉審閱

## 產出文件清單

| # | 文件 | 狀態 | 行數 |
|---|------|------|------|
| 1 | [constitution.md](./constitution.md) | ✅ 已產出 | 核心原則 6 項 |
| 2 | [research.md](./research.md) | ✅ 已產出 | 技術棧 + 演進 + 風險 |
| 3 | [data-model.md](./data-model.md) | ✅ 已產出 | 6 實體 + LocalStorage 6 key |
| 4 | [contracts/rest-api.md](./contracts/rest-api.md) | ✅ 已產出 | N/A（靜態站）+ 6 static fetch |
| 5 | [contracts/events.md](./contracts/events.md) | ✅ 已產出 | 10 DOM 事件契約 |
| 6 | [spec.md](./spec.md) | ✅ 已產出 | 8 User Stories, 14 FR, 4 NFR |
| 7 | [plan.md](./plan.md) | ✅ 已產出 | 架構 + 結構 + 複雜度 + 覆蓋率 |
| 8 | [tasks.md](./tasks.md) | ✅ 已產出 | 82 tasks (76 ✅, 0 ⚠️ code, 5 ❌ content) |
| 9 | [quickstart.md](./quickstart.md) | ✅ 已產出 | 安裝 + 4 驗證場景 + SOP |
| 10 | [checklist.md](./checklist.md) | ✅ 已產出 | 20 檢核項目 |
