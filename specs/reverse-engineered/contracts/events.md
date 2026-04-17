# Event Contracts: Mindmap-Highschool

> 反向工程產出 | 2026-04-17

## Browser Events

本專案無後端事件系統（無 WebSocket、SSE、Message Queue）。

以下為前端 DOM 事件的關鍵互動契約：

| Event | Trigger | Handler | Side Effect | 來源 |
|-------|---------|---------|-------------|------|
| `click` on markmap node text | 使用者單擊心智圖節點 | `toggleNodeFold()` | 展開/收合子節點，250ms debounce | [CODE: viewer.html:870] |
| `dblclick` on markmap node text | 使用者雙擊心智圖節點 | `openSidebar()` | 開啟 detail sidebar | [CODE: viewer.html:874] |
| `change` on sidebar checkbox | 使用者勾選「已完成複習」| `toggleNodeCheck()` | 寫入 LocalStorage ISO timestamp | [CODE: viewer.html:1062] |
| `click` on quiz option button | 使用者選擇答案 | inline handler | 標示正確/錯誤、顯示解析 | [CODE: js/app.js:476-492] |
| `input` on search field | 使用者輸入搜尋 | debounced search (150ms) | 過濾 nodeMap、顯示結果列表 | [CODE: viewer.html:1456] |
| `click` on search result | 使用者選擇搜尋結果 | `navigateToNode()` | 展開祖先、zoom 至節點、highlight | [CODE: viewer.html:1546] |
| `beforeunload` | 離開頁面 | save handler | 儲存 zoom/pan + fold 狀態至 LocalStorage | [CODE: viewer.html:770] |
| `mousedown` on resize handle | 拖拉 sidebar 邊框 | `onResizeStart()` | 調整 sidebar 寬度 | [CODE: viewer.html:1362] |
| `keydown` Ctrl/Cmd+F | 鍵盤快捷鍵 | `toggleSearch()` | 開啟/關閉搜尋面板 | [CODE: viewer.html:1598] |
| `keydown` Escape | 鍵盤快捷鍵 | `closeSearch()` | 關閉搜尋面板 | [CODE: viewer.html:1602] |
