# N25: 共享随机源：损失厌恶系数 λ 的个体异质性分布 λ_i ~ N(λ_mean, σ_λ²)，其中 λ_mean = 2.0，σ_λ² ≈ 0.25（基于 Kah

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N6

## Claim

共享随机源：损失厌恶系数 λ 的个体异质性分布 λ_i ~ N(λ_mean, σ_λ²)，其中 λ_mean = 2.0，σ_λ² ≈ 0.25（基于 Kahneman 等 1991 年实验数据的个体差异估计），该分布决定了不同卖家对同一 V_true 和 P_market 产生的 P_min 离散度。

## Corrected Claim

共享随机源：损失厌恶系数 λ 的个体异质性分布 λ_i ~ N(λ_mean, σ_λ²)，其中 λ_mean = 2.0，σ_λ² ≈ 0.25（基于 Kahneman 等 1991 年实验数据的个体差异估计），该分布决定了不同卖家对同一 V_true 和 P_market 产生的 P_min 离散度。

## Evidence

父节点级核验未通过：不完备（子节点分别描述了P_min的计算和基于P_min的拒绝概率，两者在逻辑上是串联关系而非正交维度，但内容不重复。主要问题在于完备性：父节点强调分布决定了P_min的'离散度'，但子节点仅展示了确定性公式，未显式体现随机采样导致的分布特性（如方差传播或置信区间），且缺少对'个体异质性分布'本身的统计描述子节点。）

## Search Query

loss aversion coefficient individual variance behavioral economics
