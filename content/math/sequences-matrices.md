# 數列與矩陣

## 數與式
### 實數系統
- 實數（real numbers）: 有理數與無理數的聯集
- 有理數（rational numbers）: 可表示為 p/q（q ≠ 0）的數
- 無理數（irrational numbers）: 不循環無限小數，如 √2、π
- 數線（number line）: 實數與數線上的點一一對應
### 絕對值
- 絕對值定義（absolute value）: |x| = x（x ≥ 0），|x| = -x（x < 0）
- 幾何意義（geometric meaning）: x 到原點的距離
- 三角不等式（triangle inequality）: |a + b| ≤ |a| + |b|
- 絕對值方程式與不等式（equations and inequalities）:
  - |x| = a → x = ±a
  - |x| < a → -a < x < a
  - |x| > a → x > a 或 x < -a
### 多項式運算
- 多項式加減乘（polynomial arithmetic）: 合併同類項
- 多項式除法（polynomial division）: 長除法，商式與餘式
- 因式分解（factoring）: 提公因式、十字交乘、公式法
- 分式運算（rational expressions）: 通分、約分

## 數列與級數
### 等差數列
- 等差數列定義（arithmetic sequence）: aₙ = a₁ + (n-1)d
- 公差（common difference）: d = aₙ₊₁ - aₙ
- 等差中項（arithmetic mean）: aₙ = (aₙ₋₁ + aₙ₊₁) / 2
- 等差級數求和（arithmetic series）: Sₙ = n(a₁ + aₙ)/2 = n(2a₁ + (n-1)d)/2
### 等比數列
- 等比數列定義（geometric sequence）: aₙ = a₁ · rⁿ⁻¹
- 公比（common ratio）: r = aₙ₊₁ / aₙ
- 等比中項（geometric mean）: aₙ² = aₙ₋₁ · aₙ₊₁
- 等比級數求和（geometric series）: Sₙ = a₁(1 - rⁿ)/(1 - r)（r ≠ 1）
- 無窮等比級數（infinite geometric series）: S = a₁/(1 - r)（|r| < 1 時收斂）
### 其他數列
- 遞迴關係（recurrence relation）: 以前項定義後項
- 數學歸納法（mathematical induction）:
  - 步驟一: 驗證 n = 1 成立
  - 步驟二: 假設 n = k 成立，證明 n = k+1 也成立
- Σ 符號（sigma notation）: Σ[i=1,n] aᵢ = a₁ + a₂ + ... + aₙ
- 常用求和公式（summation formulas）:
  - Σk = n(n+1)/2
  - Σk² = n(n+1)(2n+1)/6

## 矩陣
### 矩陣基本概念
- 矩陣（matrix）: m × n 的數字矩形排列
- 矩陣表示（notation）: A = [aᵢⱼ]，aᵢⱼ 為第 i 列第 j 行的元素
- 特殊矩陣（special matrices）:
  - 零矩陣（zero matrix）: 所有元素為 0
  - 單位矩陣（identity matrix）: I，對角線為 1 其餘為 0
  - 方陣（square matrix）: 列數 = 行數
### 矩陣運算
- 矩陣加減（addition/subtraction）: 對應元素相加減，須同階
- 純量乘法（scalar multiplication）: 每個元素乘以純量
- 矩陣乘法（matrix multiplication）: (AB)ᵢⱼ = Σ aᵢₖbₖⱼ
  - A(m×n) × B(n×p) = C(m×p)
  - 矩陣乘法不滿足交換律: AB ≠ BA（一般情況）
- 轉置矩陣（transpose）: Aᵀ，列與行互換
### 行列式與反矩陣
- 二階行列式（2×2 determinant）: det(A) = ad - bc
- 反矩陣（inverse matrix）: A⁻¹，使得 AA⁻¹ = A⁻¹A = I
- 二階反矩陣公式（2×2 inverse）: A⁻¹ = (1/det(A)) × [d, -b; -c, a]
- 可逆條件（invertibility）: det(A) ≠ 0
### 線性方程組
- 矩陣表示（matrix form）: AX = B
- 克乃美公式（Cramer's rule）:
  - x = det(Aₓ)/det(A)
  - y = det(Aᵧ)/det(A)
- 解的情況（solution types）:
  - det(A) ≠ 0: 唯一解
  - det(A) = 0: 無解或無窮多解
- 高斯消去法（Gaussian elimination）: 列運算化為階梯形矩陣
