# Quickstart: Mindmap-Highschool

> 反向工程產出 | 2026-04-17

## 環境需求

- 現代瀏覽器（Chrome / Safari / Edge / Firefox）
- Python 3（用於本地伺服器 + 驗證腳本）
- Git
- 網路連線（CDN 載入 Markmap / D3 / KaTeX）

**不需要**: Node.js, npm, 任何 build tool

## 安裝與啟動

```bash
# 1. Clone 專案
git clone <repo-url>
cd mindmap-highschool

# 2. 啟動本地伺服器
python3 -m http.server 8000

# 3. 開啟瀏覽器
open http://localhost:8000
```

## 驗證場景

### Scenario 1: 首頁科目載入
1. 開啟 `http://localhost:8000`
2. **預期結果**: 顯示 5 個科目卡片（國文、英文、數學、自然、社會）
3. 點擊「國文」→ 進入心智圖檢視器
4. **預期結果**: 顯示合併的國文心智圖（古文十五篇 + 國學常識 + 語文能力）

### Scenario 2: 心智圖互動
1. 在心智圖檢視器中，單擊一個節點
2. **預期結果**: 子節點展開/收合
3. 雙擊一個有子節點的節點
4. **預期結果**: 右側 sidebar 開啟，顯示概念與考試兩個 tab

### Scenario 3: 題庫練習
1. 從首頁進入自然 → 化學
2. 在主題列表點擊「📝 練習」
3. **預期結果**: 顯示題目列表
4. 選擇一個答案
5. **預期結果**: 即時標示正確/錯誤 + 顯示解析

### Scenario 4: 搜尋功能
1. 在心智圖檢視器中按 `Ctrl+F`（Mac: `Cmd+F`）
2. 輸入搜尋文字
3. **預期結果**: 顯示匹配節點列表（150ms debounce）
4. 點擊結果
5. **預期結果**: 心智圖自動展開並 zoom 至目標節點

## 開發指令

```bash
# 內容驗證（需先啟動 localhost:8001）
python3 -m http.server 8001 &
python3 scripts/smoke-test.py

# JSON 格式驗證
python3 -c "import json; json.load(open('content/chinese/topics.json'))"

# 化學內容驗證
python3 scripts/validate-chemistry.py
```

## 新增內容 SOP

### 新增主題
1. 建立 `content/{subject}/{sub}/{topic-id}.md`（Markmap 格式）
2. 建立 `content/{subject}/{sub}/details/{topic-id}.json`（associations + examTips）
3. 建立 `questions/{subject}/{sub}/{topic-id}.json`（題庫）
4. 在 `content/{subject}/{sub}/topics.json` 的 categories 中註冊主題
5. 驗證：`python3 -c "import json; json.load(open('content/{subject}/{sub}/topics.json'))"`

### 新增科目
1. 在 `content/subjects.json` 中新增科目定義
2. 建立 `content/{subject}/topics.json`
3. 按照上方 SOP 新增主題
