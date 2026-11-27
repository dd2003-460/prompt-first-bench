# N51: 内生性偏差控制：在计算 ρ_phenomena 时，需控制卖家特征向量 X_seller（如卖家信用分、历史成交率）作为控制变量，使用多元回归 T_close 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

内生性偏差控制：在计算 ρ_phenomena 时，需控制卖家特征向量 X_seller（如卖家信用分、历史成交率）作为控制变量，使用多元回归 T_close = α + ρ1*ΔQ + β*X_seller + ε 来提取偏相关系数；若控制后 ρ1 仍显著为负，则排除卖家异质性导致的虚假相关，增强因果推断效力。

## Corrected Claim

内生性偏差控制：在计算 ρ_phenomena 时，需控制卖家特征向量 X_seller（如卖家信用分、历史成交率）作为控制变量，使用多元回归 T_close = α + ρ1*ΔQ + β*X_seller + ε 来提取偏相关系数；若控制后 ρ1 仍显著为负，则排除卖家异质性导致的虚假相关，增强因果推断效力。

## Evidence

先验知识/题面给定，逻辑校验通过：多元回归控制变量以提取偏相关系数是标准的统计推断方法，用于缓解内生性偏差，逻辑自洽且符合计量经济学原理。
