# N334: β_platform = ∂Equilibrium_Stability/∂w_speed 的估计方法：Equilibrium_Stability 定义为均衡点附

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N114

## Claim

β_platform = ∂Equilibrium_Stability/∂w_speed 的估计方法：Equilibrium_Stability 定义为均衡点附近最大特征值的绝对值 |λ_max|，通过有限差分法 Δβ_platform ≈ (|λ_max(w+Δw)| - |λ_max(w)|) / Δw 估算，需选择足够小的 Δw 以逼近导数。

## Corrected Claim

β_platform = ∂Equilibrium_Stability/∂w_speed 的估计方法：Equilibrium_Stability 定义为均衡点附近最大特征值的绝对值 |λ_max|，通过有限差分法 Δβ_platform ≈ (|λ_max(w+Δw)| - |λ_max(w)|) / Δw 估算，需选择足够小的 Δw 以逼近导数。

## Evidence

先验知识/题面给定，逻辑校验通过：有限差分法是估算导数的标准数值方法，公式结构正确，量纲一致，且符合控制论中稳定性指标（特征值模长）的定义。
