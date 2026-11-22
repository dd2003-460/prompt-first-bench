# N237: 挂价偏差分布的样本修正因子：若实际样本量 n 小于理论最小值 n_min，需应用有限总体校正因子 fpc = sqrt((N-n)/(N-1)) 调整 σ_δ，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N78

## Claim

挂价偏差分布的样本修正因子：若实际样本量 n 小于理论最小值 n_min，需应用有限总体校正因子 fpc = sqrt((N-n)/(N-1)) 调整 σ_δ，以反映小样本下的方差低估风险。

## Corrected Claim

挂价偏差分布的样本修正因子：若实际样本量 n 小于理论最小值 n_min，需应用有限总体校正因子 fpc = sqrt((N-n)/(N-1)) 调整 σ_δ，以反映小样本下的方差低估风险。

## Evidence

先验知识/题面给定，逻辑校验通过：有限总体校正因子（FPC）的标准公式为 sqrt((N-n)/(N-1))，用于修正小样本下对总体标准差的估计偏差，符合统计学原理。

## Search Query

finite population correction factor standard error estimation
