# N195: 平台长期净现值 NPV_intervention 的计算公式：NPV_intervention = ∑_{t=0}^{T} [ (ΔLTV_t * w2 - S

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

平台长期净现值 NPV_intervention 的计算公式：NPV_intervention = ∑_{t=0}^{T} [ (ΔLTV_t * w2 - Subsidy_Cost_t) / (1 + r)^t ]，其中 ΔLTV_t 为第t期用户生命周期价值增量，w2 为平台目标函数中LTV权重（N67），Subsidy_Cost_t 为第t期补贴总支出，r 为平台资本成本率（通常 8-12%）。

## Corrected Claim

平台长期净现值 NPV_intervention 的计算公式：NPV_intervention = ∑_{t=0}^{T} [ (ΔLTV_t * w2 - Subsidy_Cost_t) / (1 + r)^t ]，其中 ΔLTV_t 为第t期用户生命周期价值增量，w2 为平台目标函数中LTV权重（N67），Subsidy_Cost_t 为第t期补贴总支出，r 为平台资本成本率（通常 8-12%）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

net present value calculation for platform subsidy programs
