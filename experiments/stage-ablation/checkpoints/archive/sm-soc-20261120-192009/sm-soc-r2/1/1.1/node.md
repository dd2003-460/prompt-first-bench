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

父节点级核验通过：正交+完备+无冗余（三个子节点分别定义了分布的三个核心组件：先验/基础变量（intrinsic_value）、均值偏移参数（anchor_bias）以及方差结构（σ²分解）。它们分别对应正态分布的输入、均值和方差，彼此独立且无重叠，共同完整构成了父节点中 P(price | intrinsic_value) 的定义基础。）
