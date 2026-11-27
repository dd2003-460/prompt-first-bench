# N196: 交互项系数β_interaction的显著性检验需考虑多重共线性影响，若Price_Premium与Price_Drop的相关系数|ρ|>0.8，则需对变量进行

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64, N65, N66

## Claim

交互项系数β_interaction的显著性检验需考虑多重共线性影响，若Price_Premium与Price_Drop的相关系数|ρ|>0.8，则需对变量进行中心化处理后重新估计β_interaction，否则标准误膨胀将导致p值失真。

## Corrected Claim

交互项系数β_interaction的显著性检验需考虑多重共线性影响，若Price_Premium与Price_Drop的相关系数|ρ|>0.8，则需对变量进行中心化处理后重新估计β_interaction，否则标准误膨胀将导致p值失真。

## Evidence

先验知识/题面给定，逻辑校验通过：高多重共线性确实会导致交互项系数标准误膨胀，中心化是标准处理方法。

## Search Query

interaction term multicollinearity centering variables regression standard error inflation
