# N262: 分母选择对 t 统计量的影响量化：当使用曝光量作分母时，由于同一用户多次曝光导致观测值非独立，标准误 SE_exposure 需乘以修正因子 √(1 + (m-

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

分母选择对 t 统计量的影响量化：当使用曝光量作分母时，由于同一用户多次曝光导致观测值非独立，标准误 SE_exposure 需乘以修正因子 √(1 + (m-1)*ICC)，其中 m 为平均每人曝光次数，ICC 为组内相关系数；若 ICC > 0.1，则基于曝光量的 t 检验会显著低估标准误，导致 p 值偏小（假阳性风险增加）。

## Corrected Claim

分母选择对 t 统计量的影响量化：当使用曝光量作分母时，由于同一用户多次曝光导致观测值非独立，标准误 SE_exposure 需乘以修正因子 √(1 + (m-1)*ICC)，其中 m 为平均每人曝光次数，ICC 为组内相关系数；若 ICC > 0.1，则基于曝光量的 t 检验会显著低估标准误，导致 p 值偏小（假阳性风险增加）。

## Evidence

先验知识/题面给定，逻辑校验通过：基于设计效应（Design Effect）公式 Var_cluster = Var_ind * (1 + (m-1)*ICC)，当 ICC > 0 时，聚类标准误大于独立假设下的标准误，因此忽略聚类效应（即使用曝光量作分母且假设独立）会导致标准误低估、t 值虚高、p 值偏小，逻辑自洽且符合统计原理。

## Search Query

intraclass correlation coefficient adjustment for clustered data in t-test
