# N30: 陆地表面拖曳系数 C_d,land 由粗糙长度 z_0 决定，典型草地 z_0 ≈ 0.05 m，城市 z_0 ≈ 1-10 m，C_d,land 与 z_0 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

陆地表面拖曳系数 C_d,land 由粗糙长度 z_0 决定，典型草地 z_0 ≈ 0.05 m，城市 z_0 ≈ 1-10 m，C_d,land 与 z_0 的关系近似为 C_d ∝ (ln(z/z_0))^(-2)，导致在相同风速下 C_d,land 比 C_d,ocean 高一个数量级（3-10 倍）。

## Corrected Claim

陆地表面拖曳系数 C_d,land 由粗糙长度 z_0 决定，典型草地 z_0 ≈ 0.05 m，城市 z_0 ≈ 1-10 m，C_d,land 与 z_0 的关系近似为 C_d ∝ (ln(z/z_0))^(-2)，导致在相同风速下 C_d,land 比 C_d,ocean 高一个数量级（3-10 倍）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于Monin-Obukhov相似理论，地表摩擦速度u*与z0关系为u* = u / ln(z/z0)，拖曳系数Cd ∝ (u*)^2/u^2 ∝ (ln(z/z0))^-2。草地z0≈0.05m，城市z0≈1-10m，海洋z0≈0.0001-0.001m。取z=10m，草地ln(200)≈5.3，Cd∝1/28；海洋ln(10000)≈9.2，Cd∝1/85。比值约3倍，符合'高一个数量级（3-10倍）'的量级描述。逻辑自洽，数值量级合理。
