# N5: 共享随机源：卖家初始挂价分布服从 P(price | intrinsic_value) = N(μ, σ²)，其中 μ = intrinsic_value * 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

共享随机源：卖家初始挂价分布服从 P(price | intrinsic_value) = N(μ, σ²)，其中 μ = intrinsic_value * (1 + anchor_bias)，σ² 代表随机偏好噪声；该分布是后续所有博弈的初始状态。

## Corrected Claim

共享随机源：卖家初始挂价分布服从 P(price | intrinsic_value) = N(μ, σ²)，其中 μ = intrinsic_value * (1 + anchor_bias)，σ² 代表随机偏好噪声；该分布是后续所有博弈的初始状态。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别定义了父节点分布中的三个关键参数（内在价值先验、均值偏移项 anchor_bias、条件方差结构），三者逻辑独立且互不重叠；共同覆盖了父节点公式 P(price | intrinsic_value) = N(μ, σ²) 中 μ 和 σ² 的完整来源及 intrinsic_value 的分布假设，无遗漏。）
