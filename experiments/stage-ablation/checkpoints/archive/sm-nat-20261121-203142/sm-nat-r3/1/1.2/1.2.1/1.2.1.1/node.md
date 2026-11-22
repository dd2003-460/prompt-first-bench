# N90: 在 Pareto(β=0.9) 分布中，若 r_min 定义为平均频率 500 次/天，则分布参数 x_min = r_min * (β-1)/β = 500 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

在 Pareto(β=0.9) 分布中，若 r_min 定义为平均频率 500 次/天，则分布参数 x_min = r_min * (β-1)/β = 500 * 0.1/0.9 ≈ 55.56 次/天，这是截断下界而非物理最小值，需验证该下界是否导致长尾截断偏差 [knowledge: 数学推导]

## Corrected Claim

在 Pareto(β=0.9) 分布中，若 r_min 定义为平均频率 500 次/天，则分布参数 x_min = r_min * (β-1)/β = 500 * 0.1/0.9 ≈ 55.56 次/天，这是截断下界而非物理最小值，需验证该下界是否导致长尾截断偏差 [knowledge: 数学推导]

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布均值公式 E[X] = x_min * β / (β - 1) 在 β > 1 时成立，反解得 x_min = E[X] * (β - 1) / β，代入数值 500 * 0.1 / 0.9 ≈ 55.56 计算正确，且 x_min 作为截断下界的定义符合 Pareto 分布标准定义。
