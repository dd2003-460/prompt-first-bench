# N126: 下游投影 2：买家放弃当前商品的概率 P_abandon = P(E[Benefit_search] > 0) = 1 - Φ(-μ_Benefit / σ_B

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

下游投影 2：买家放弃当前商品的概率 P_abandon = P(E[Benefit_search] > 0) = 1 - Φ(-μ_Benefit / σ_Benefit)，其中 μ_Benefit 和 σ_Benefit 为 E[Benefit_search] 的均值和标准差，需验证 P_abandon 是否显著高于基线，以确认机会成本是买家放弃的主因。

## Corrected Claim

下游投影 2：买家放弃当前商品的概率 P_abandon = P(E[Benefit_search] > 0) = 1 - Φ(-μ_Benefit / σ_Benefit)，其中 μ_Benefit 和 σ_Benefit 为 E[Benefit_search] 的均值和标准差，需验证 P_abandon 是否显著高于基线，以确认机会成本是买家放弃的主因。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态分布假设，P(X>0) = 1 - Φ(-μ/σ) 是标准的概率计算公式，逻辑自洽且量纲正确。
