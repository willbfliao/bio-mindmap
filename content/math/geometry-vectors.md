# 幾何與向量

## 直線與圓
### 直線方程式
- 斜截式（slope-intercept form）: y = mx + b
- 點斜式（point-slope form）: y - y₁ = m(x - x₁)
- 一般式（general form）: ax + by + c = 0
- 截距式（intercept form）: x/a + y/b = 1
- 兩點式斜率（slope from two points）: m = (y₂ - y₁)/(x₂ - x₁)
### 距離公式
- 兩點距離（distance between two points）: d = √((x₂-x₁)² + (y₂-y₁)²)
- 點到直線距離（point-to-line distance）: d = |ax₀ + by₀ + c| / √(a² + b²)
- 中點公式（midpoint formula）: M = ((x₁+x₂)/2, (y₁+y₂)/2)
### 直線關係
- 平行條件（parallel condition）: 斜率相等 m₁ = m₂
- 垂直條件（perpendicular condition）: m₁ × m₂ = -1
- 兩平行線距離（distance between parallel lines）: d = |c₁ - c₂| / √(a² + b²)
### 圓方程式
- 標準式（standard form）: (x - h)² + (y - k)² = r²，圓心 (h, k)，半徑 r
- 一般式（general form）: x² + y² + Dx + Ey + F = 0
- 圓心（center）: (-D/2, -E/2)，半徑: r = √(D²/4 + E²/4 - F)
- 圓與直線關係（circle-line relation）: 利用圓心到直線距離 d 與 r 比較
  - d < r 相交（兩交點）
  - d = r 相切（一交點）
  - d > r 相離（無交點）

## 平面向量
### 向量基本概念
- 向量（vector）: 具有大小與方向的量，記作 →a 或 a
- 位置向量（position vector）: 從原點到點 P 的向量
- 向量相等（equal vectors）: 大小相同且方向相同
- 零向量（zero vector）: 大小為零，方向不定
### 向量運算
- 向量加法（vector addition）: →a + →b，平行四邊形法則或三角形法則
- 向量減法（vector subtraction）: →a - →b = →a + (-→b)
- 純量乘法（scalar multiplication）: k→a，改變大小與方向
- 向量分解（vector decomposition）: →a = a₁→i + a₂→j
### 內積
- 內積定義（dot product）: →a · →b = |→a||→b| cos θ
- 座標表示（coordinate form）: →a · →b = a₁b₁ + a₂b₂
- 向量長度（magnitude）: |→a| = √(a₁² + a₂²)
- 夾角公式（angle formula）: cos θ = (→a · →b) / (|→a||→b|)
- 垂直判定（perpendicularity）: →a · →b = 0 則 →a ⊥ →b
### 投影
- 正射影（projection）: proj_b a = (→a · →b / |→b|²) →b
- 投影長（projection length）: |→a| cos θ = →a · →b / |→b|
- 面積公式（area formula）: 三角形面積 = ½|→a × →b| = ½|a₁b₂ - a₂b₁|

## 空間向量與空間幾何
### 空間座標
- 三維座標（3D coordinates）: P(x, y, z)
- 空間兩點距離（distance in 3D）: d = √((x₂-x₁)² + (y₂-y₁)² + (z₂-z₁)²)
- 空間中點公式（midpoint in 3D）: M = ((x₁+x₂)/2, (y₁+y₂)/2, (z₁+z₂)/2)
### 空間向量運算
- 空間內積（dot product in 3D）: →a · →b = a₁b₁ + a₂b₂ + a₃b₃
- 外積（cross product）: →a × →b，結果為垂直於兩向量的向量
  - |→a × →b| = |→a||→b| sin θ
- 外積行列式（determinant form）: →a × →b = (a₂b₃-a₃b₂, a₃b₁-a₁b₃, a₁b₂-a₂b₁)
### 平面方程式
- 一般式（general form）: ax + by + cz + d = 0
- 法向量（normal vector）: →n = (a, b, c)
- 點到平面距離（point-to-plane distance）: d = |ax₀ + by₀ + cz₀ + d| / √(a² + b² + c²)
### 空間直線
- 參數式（parametric form）: x = x₀ + at, y = y₀ + bt, z = z₀ + ct
- 方向向量（direction vector）: →d = (a, b, c)

## 圓錐曲線
### 拋物線
- 標準式（standard form）: y² = 4px（焦點在 x 軸上）
- 焦點（focus）: F(p, 0)
- 準線（directrix）: x = -p
- 定義（definition）: 到焦點與準線等距的點之軌跡
### 橢圓
- 標準式（standard form）: x²/a² + y²/b² = 1（a > b > 0）
- 焦點（foci）: F(±c, 0)，其中 c² = a² - b²
- 定義（definition）: 到兩焦點距離和為 2a 的點之軌跡
- 離心率（eccentricity）: e = c/a（0 < e < 1）
### 雙曲線
- 標準式（standard form）: x²/a² - y²/b² = 1
- 焦點（foci）: F(±c, 0)，其中 c² = a² + b²
- 定義（definition）: 到兩焦點距離差的絕對值為 2a 的點之軌跡
- 漸近線（asymptotes）: y = ±(b/a)x
- 離心率（eccentricity）: e = c/a（e > 1）
