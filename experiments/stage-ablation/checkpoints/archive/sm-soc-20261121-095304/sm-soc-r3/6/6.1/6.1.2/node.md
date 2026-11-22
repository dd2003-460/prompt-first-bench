# N170: 边际成交概率 dP(deal)/dk 的解析表达式：dP(deal)/dk = -φ(k)，其中 φ(k) 为标准正态分布密度函数。在 k=2 时，dP(dea

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

边际成交概率 dP(deal)/dk 的解析表达式：dP(deal)/dk = -φ(k)，其中 φ(k) 为标准正态分布密度函数。在 k=2 时，dP(deal)/dk ≈ -0.054，即每增加 1σ 的价格偏差，成交概率下降 5.4%，这与 N60 中 -0.5% 的阈值存在显著差异，需重新校准'骤降'的定义。

## Corrected Claim

边际成交概率 dP(deal)/dk 的解析表达式：dP(deal)/dk = -φ(k)，其中 φ(k) 为标准正态分布密度函数。在 k=2 时，dP(deal)/dk ≈ -0.054，即每增加 1σ 的价格偏差，成交概率下降 5.4%，这与 N60 中 -0.5% 的阈值存在显著差异，需重新校准'骤降'的定义。

## Evidence

先验知识/题面给定，逻辑校验通过：标准正态分布密度函数在 k=2 处的值为 1/sqrt(2π)*exp(-2) ≈ 0.054，与陈述中的数值一致；逻辑推导成立，来源未直接覆盖
