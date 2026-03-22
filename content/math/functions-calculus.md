# 函數與微積分

## 多項式函數
### 一次函數
- 一次函數（linear function）: y = ax + b，圖形為直線
- 斜率（slope）: a 值決定傾斜程度與方向
  - a > 0 向右上升，a < 0 向右下降
- y 截距（y-intercept）: b 值為直線與 y 軸的交點
- 零點（zero）: x = -b/a，直線與 x 軸的交點
### 二次函數
- 標準式（standard form）: y = ax² + bx + c
- 頂點式（vertex form）: y = a(x - h)² + k，頂點為 (h, k)
- 頂點公式（vertex formula）: h = -b/(2a)，k = (4ac - b²)/(4a)
- 開口方向（opening direction）: a > 0 開口向上，a < 0 開口向下
- 判別式（discriminant）: D = b² - 4ac
  - D > 0 兩相異實根
  - D = 0 重根
  - D < 0 無實根
- 對稱軸（axis of symmetry）: x = -b/(2a)
### 高次多項式
- 多項式除法（polynomial division）: 長除法與綜合除法
- 餘式定理（remainder theorem）: f(x) 除以 (x - a) 的餘式為 f(a)
- 因式定理（factor theorem）: f(a) = 0 則 (x - a) 為 f(x) 的因式
- 勘根定理（intermediate value theorem）: 連續函數若 f(a)·f(b) < 0，則 (a, b) 間至少有一根

## 指數與對數函數
### 指數函數
- 指數律（laws of exponents）: aᵐ × aⁿ = aᵐ⁺ⁿ，(aᵐ)ⁿ = aᵐⁿ
- 指數函數圖形（exponential graph）: y = aˣ（a > 0 且 a ≠ 1）
  - a > 1 為遞增函數
  - 0 < a < 1 為遞減函數
- 恆過定點（fixed point）: (0, 1)，因為 a⁰ = 1
### 對數函數
- 對數定義（logarithm definition）: y = logₐx 等價於 aʸ = x
- 對數律（laws of logarithms）:
  - logₐ(xy) = logₐx + logₐy
  - logₐ(x/y) = logₐx - logₐy
  - logₐ(xⁿ) = n·logₐx
- 換底公式（change of base）: logₐb = log b / log a
- 常用對數（common log）: log₁₀，自然對數（natural log）: ln = logₑ
### 指數與對數方程式
- 指數方程式（exponential equations）: 同底比較指數
- 對數方程式（logarithmic equations）: 化為指數形式求解
- 定義域限制（domain restriction）: 對數的真數必須 > 0

## 三角函數
### 三角比
- 直角三角形定義（right triangle definition）:
  - sin θ = 對邊/斜邊
  - cos θ = 鄰邊/斜邊
  - tan θ = 對邊/鄰邊
- 特殊角（special angles）: 30°、45°、60° 的三角比值
- 互餘關係（complementary relation）: sin θ = cos(90° - θ)
### 廣義角與弧度
- 廣義角（general angle）: 角度可為任意實數
- 弧度（radian）: π rad = 180°
- 弧長公式（arc length）: s = rθ（θ 為弧度）
- 扇形面積（sector area）: A = ½r²θ
### 三角函數圖形
- 正弦函數（sine function）: y = sin x，週期 2π
- 餘弦函數（cosine function）: y = cos x，週期 2π
- 正切函數（tangent function）: y = tan x，週期 π
- 振幅（amplitude）: y = A sin(Bx + C) 中 |A| 為振幅
- 週期（period）: T = 2π/|B|
### 三角恆等式
- 畢氏恆等式（Pythagorean identity）: sin²θ + cos²θ = 1
- 和角公式（addition formulas）:
  - sin(α ± β) = sinα cosβ ± cosα sinβ
  - cos(α ± β) = cosα cosβ ∓ sinα sinβ
- 倍角公式（double angle）: sin 2θ = 2 sinθ cosθ，cos 2θ = cos²θ - sin²θ
- 正弦定理（law of sines）: a/sin A = b/sin B = c/sin C = 2R
- 餘弦定理（law of cosines）: c² = a² + b² - 2ab cos C

## 極限與微積分初步
### 極限概念
- 函數極限（limit of function）: lim[x→a] f(x) = L
- 單邊極限（one-sided limits）: 左極限與右極限須相等
- 極限運算性質（limit properties）: 可加減乘除（分母不為零）
- 連續性（continuity）: f(a) = lim[x→a] f(x)
### 導數
- 導數定義（derivative definition）: f'(x) = lim[Δx→0] (f(x+Δx) - f(x))/Δx
- 切線斜率（tangent slope）: f'(a) 為曲線在 x = a 處的切線斜率
- 基本微分公式（basic differentiation）:
  - (xⁿ)' = nxⁿ⁻¹
  - (c)' = 0
  - (cf(x))' = cf'(x)
  - (f ± g)' = f' ± g'
### 微分應用
- 遞增遞減判定（increasing/decreasing）: f'(x) > 0 遞增，f'(x) < 0 遞減
- 極值判定（extrema）: f'(x) = 0 且導數變號為極值
- 最佳化問題（optimization）: 利用微分求最大值或最小值
### 積分初步
- 不定積分（indefinite integral）: ∫xⁿ dx = xⁿ⁺¹/(n+1) + C
- 定積分（definite integral）: ∫[a,b] f(x) dx = F(b) - F(a)
- 面積計算（area calculation）: 曲線與 x 軸圍成的面積
- 微積分基本定理（fundamental theorem）: 微分與積分互為逆運算
