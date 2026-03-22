# 機率統計與數據分析

## 排列組合
### 計數原理
- 加法原理（addition principle）: 完成一件事有 m 類方法或 n 類方法，共 m + n 種
- 乘法原理（multiplication principle）: 完成一件事需先後兩步，共 m × n 種
### 排列
- 排列數（permutation）: P(n, r) = n!/(n-r)!
- 階乘（factorial）: n! = n × (n-1) × ... × 2 × 1，0! = 1
- 相同物排列（identical objects）: n! / (n₁! × n₂! × ... × nₖ!)
- 環狀排列（circular permutation）: (n-1)!
### 組合
- 組合數（combination）: C(n, r) = n! / (r!(n-r)!)
- 組合性質（combination properties）:
  - C(n, r) = C(n, n-r)
  - C(n, 0) = C(n, n) = 1
  - C(n, r) = C(n-1, r-1) + C(n-1, r)（巴斯卡定理）
### 二項式定理
- 二項式展開（binomial theorem）: (a+b)ⁿ = Σ C(n,k) aⁿ⁻ᵏbᵏ
- 一般項（general term）: 第 k+1 項 = C(n,k) aⁿ⁻ᵏbᵏ

## 古典機率
### 樣本空間
- 樣本空間（sample space）: 所有可能結果的集合 S
- 事件（event）: 樣本空間的子集合
- 基本事件（elementary event）: 只含一個結果的事件
### 古典機率定義
- 機率公式（probability formula）: P(A) = n(A)/n(S)
- 機率範圍（probability range）: 0 ≤ P(A) ≤ 1
- 必然事件（certain event）: P(S) = 1
- 不可能事件（impossible event）: P(∅) = 0
### 機率運算
- 餘事件（complement）: P(A') = 1 - P(A)
- 聯集（union）: P(A∪B) = P(A) + P(B) - P(A∩B)
- 互斥事件（mutually exclusive）: P(A∩B) = 0 則 P(A∪B) = P(A) + P(B)

## 數據分析
### 集中趨勢
- 算術平均數（arithmetic mean）: x̄ = Σxᵢ / n
- 中位數（median）: 資料排序後中間值
- 眾數（mode）: 出現次數最多的值
### 離散程度
- 全距（range）: 最大值 - 最小值
- 變異數（variance）: σ² = Σ(xᵢ - x̄)² / n
- 標準差（standard deviation）: σ = √(變異數)
- 標準化值（z-score）: z = (x - x̄) / σ
### 相關分析
- 散布圖（scatter plot）: 觀察兩變數的關聯
- 相關係數（correlation coefficient）: r，-1 ≤ r ≤ 1
  - r 接近 1 正相關
  - r 接近 -1 負相關
  - r 接近 0 無線性相關
- 最小平方法（least squares method）: 迴歸直線 ŷ = a + bx
  - 斜率: b = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²
  - 截距: a = ȳ - bx̄
  - 迴歸直線必過 (x̄, ȳ)

## 條件機率與貝氏定理
### 條件機率
- 條件機率定義（conditional probability）: P(A|B) = P(A∩B) / P(B)
- 意義（interpretation）: 在 B 已發生的條件下，A 發生的機率
### 獨立事件
- 獨立事件（independent events）: P(A∩B) = P(A) × P(B)
- 判定方法（independence test）: P(A|B) = P(A) 則 A、B 獨立
### 貝氏定理
- 貝氏定理（Bayes' theorem）: P(A|B) = P(B|A)·P(A) / P(B)
- 全機率公式（total probability）: P(B) = Σ P(B|Aᵢ)·P(Aᵢ)
- 應用場景（applications）: 疾病檢測、垃圾郵件過濾

## 隨機變數與期望值
### 隨機變數
- 隨機變數（random variable）: 將樣本空間對應到實數的函數
- 機率分配（probability distribution）: 列出所有可能值及其機率
- 機率分配表（probability table）: ΣP(X = xᵢ) = 1
### 期望值
- 期望值（expected value）: E(X) = Σ xᵢ · P(X = xᵢ)
- 期望值性質（properties）:
  - E(aX + b) = aE(X) + b
  - E(X + Y) = E(X) + E(Y)
- 變異數（variance）: Var(X) = E(X²) - [E(X)]²
### 二項分配
- 伯努利試驗（Bernoulli trial）: 只有成功與失敗兩種結果
- 二項分配（binomial distribution）: X ~ B(n, p)
  - P(X = k) = C(n,k) pᵏ (1-p)ⁿ⁻ᵏ
- 期望值: E(X) = np
- 標準差: σ = √(np(1-p))
