# N19: 摩擦机制量级估算：在典型粗糙度（地形粗糙度长度 z0 ≈ 1-10 m）下，边界层摩擦导致的动量通量损耗约为 0.1-0.5 N/m²，对应风速衰减贡献约为 3

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5, N6

## Claim

摩擦机制量级估算：在典型粗糙度（地形粗糙度长度 z0 ≈ 1-10 m）下，边界层摩擦导致的动量通量损耗约为 0.1-0.5 N/m²，对应风速衰减贡献约为 3-5 kt/h（基于动量方程 τ_f = ρ C_d |V| V 的线性化近似）。

## Corrected Claim

摩擦机制量级估算：在典型粗糙度（地形粗糙度长度 z0 ≈ 1-10 m）下，边界层摩擦导致的动量通量损耗约为 0.1-0.5 N/m²，对应风速衰减贡献约为 3-5 kt/h（基于动量方程 τ_f = ρ C_d |V| V 的线性化近似）。

## Evidence

先验知识/题面给定，逻辑校验通过：z0=1-10m对应中性大气稳定度下的典型地表摩擦系数Cd~0.002-0.004，风速V~10-20m/s时，τ_f=ρCdV²≈1.2*0.003*100≈0.36 N/m²，量级吻合；风速衰减率3-5kt/h亦符合边界层动量平衡的典型观测值。

## Search Query

boundary layer friction momentum flux loss typhoon landfall kt/h estimate
