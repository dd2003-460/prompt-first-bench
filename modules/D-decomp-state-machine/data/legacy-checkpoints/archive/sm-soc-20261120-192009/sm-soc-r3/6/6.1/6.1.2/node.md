# N298: 触发阈值 θ_trigger 与经验值 E 的函数关系：假设 θ_trigger(E) = 1.30 - 0.5 * E^0.5；当 E=0（新手）时，θ=1.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N102

## Claim

触发阈值 θ_trigger 与经验值 E 的函数关系：假设 θ_trigger(E) = 1.30 - 0.5 * E^0.5；当 E=0（新手）时，θ=1.30；当 E=1（专家）时，θ=0.80；该函数意味着专家买家对价格偏离的容忍度更低，更容易触发'观察模式'从而抑制高挂价成交。

## Corrected Claim

触发阈值 θ_trigger 与经验值 E 的函数关系：假设 θ_trigger(E) = 1.30 - 0.5 * E^0.5；当 E=0（新手）时，θ=1.30；当 E=1（专家）时，θ=0.80；该函数意味着专家买家对价格偏离的容忍度更低，更容易触发'观察模式'从而抑制高挂价成交。

## Evidence

先验知识/题面给定，逻辑校验通过：函数定义 θ(E) = 1.30 - 0.5 * E^0.5 在 E=0 时 θ=1.30，在 E=1 时 θ=0.80，数值计算准确；逻辑上阈值降低意味着触发条件更容易满足（即对偏离更敏感/容忍度更低），与陈述中“专家买家...更容易触发'观察模式'”的因果解释自洽。

## Search Query

expert buyer price sensitivity threshold model
