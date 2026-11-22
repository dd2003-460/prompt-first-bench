# N180: 控制变量回归模型中，'商品质量'的代理变量必须量化为卖家历史好评率 R_good 与商品成色评分 S_cond（1-5分），回归方程为 ln(T) = α + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

控制变量回归模型中，'商品质量'的代理变量必须量化为卖家历史好评率 R_good 与商品成色评分 S_cond（1-5分），回归方程为 ln(T) = α + β1*Premium + β2*R_good + β3*S_cond + ε，其中 β1 为需估计的净信号效应系数。

## Corrected Claim

控制变量回归模型中，'商品质量'的代理变量必须量化为卖家历史好评率 R_good 与商品成色评分 S_cond（1-5分），回归方程为 ln(T) = α + β1*Premium + β2*R_good + β3*S_cond + ε，其中 β1 为需估计的净信号效应系数。

## Evidence

先验知识/题面给定，逻辑校验通过
