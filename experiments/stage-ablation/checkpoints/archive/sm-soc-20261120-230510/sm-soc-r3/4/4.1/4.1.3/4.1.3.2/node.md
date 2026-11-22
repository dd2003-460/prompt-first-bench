# N219: 下游投影1 - 排序偏移幅度 Δγ_search：权重比从 γ_0 = w_CTR/w_Prob 变为 γ_1 = w_Prob/w_CTR，偏移幅度量化为相对

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N70

## Claim

下游投影1 - 排序偏移幅度 Δγ_search：权重比从 γ_0 = w_CTR/w_Prob 变为 γ_1 = w_Prob/w_CTR，偏移幅度量化为相对变化率 (γ_1 - γ_0) / γ_0，取决于当前算法的初始权重配置及业务目标调整系数。

## Corrected Claim

下游投影1 - 排序偏移幅度 Δγ_search：权重比从 γ_0 = w_CTR/w_Prob 变为 γ_1 = w_Prob/w_CTR，偏移幅度量化为相对变化率 (γ_1 - γ_0) / γ_0，取决于当前算法的初始权重配置及业务目标调整系数。

## Evidence

先验知识/题面给定，逻辑校验通过：权重比定义及相对变化率公式在数学上自洽，量纲正确，符合算法调整的一般逻辑。
