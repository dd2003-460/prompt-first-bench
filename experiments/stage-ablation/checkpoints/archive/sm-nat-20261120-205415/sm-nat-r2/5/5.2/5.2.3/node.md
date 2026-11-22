# N70: Pareto 分布截断对参数有效性的约束：当 α=1.1 且截断上限 B=10^4.5 MB 时，需验证积分 ∫_xmin^B x^(-1.2) dx 是否收敛

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

Pareto 分布截断对参数有效性的约束：当 α=1.1 且截断上限 B=10^4.5 MB 时，需验证积分 ∫_xmin^B x^(-1.2) dx 是否收敛，确保给定参数在物理约束下自洽

## Corrected Claim

Pareto 分布截断对参数有效性的约束：当 α=1.1 且截断上限 B=10^4.5 MB 时，需验证积分 ∫_xmin^B x^(-1.2) dx 是否收敛，确保给定参数在物理约束下自洽

## Evidence

先验知识/题面给定，逻辑校验通过：积分 ∫ x^(-1.2) dx 的原函数为 x^(-0.2)/(-0.2)，在有限上限 B=10^4.5 处收敛，无发散风险，参数自洽。
