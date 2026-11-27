# N182: 共享随机源：买家对算法推荐价的信任度 T_trust 的分布参数，建模为 T_trust ~ N(μ_trust, σ_trust²)，其中 μ_trust 为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N57

## Claim

共享随机源：买家对算法推荐价的信任度 T_trust 的分布参数，建模为 T_trust ~ N(μ_trust, σ_trust²)，其中 μ_trust 为平台用户调研中‘相信算法推荐价合理’的比例均值，σ_trust 为个体差异标准差，该随机源决定 ΔT_sale 公式中信任项的波动范围。

## Corrected Claim

共享随机源：买家对算法推荐价的信任度 T_trust 的分布参数，建模为 T_trust ~ N(μ_trust, σ_trust²)，其中 μ_trust 为平台用户调研中‘相信算法推荐价合理’的比例均值，σ_trust 为个体差异标准差，该随机源决定 ΔT_sale 公式中信任项的波动范围。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布建模信任度是合理的统计假设，参数定义（均值对应调研比例，标准差对应个体差异）符合统计学惯例，且作为模型内部随机源的定义在逻辑上自洽。

## Search Query

trust in algorithmic pricing recommendation survey mean standard deviation
