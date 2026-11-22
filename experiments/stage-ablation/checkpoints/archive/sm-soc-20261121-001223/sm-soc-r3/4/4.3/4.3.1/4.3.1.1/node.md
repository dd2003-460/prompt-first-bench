# N173: 倾向得分 (Propensity Score) 的具体回归模型：定义 P(Treat=1 | X) = 1 / (1 + e^(-β_0 - Σβ_i X_i)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64

## Claim

倾向得分 (Propensity Score) 的具体回归模型：定义 P(Treat=1 | X) = 1 / (1 + e^(-β_0 - Σβ_i X_i))，其中协变量 X 包括卖家历史信用分、商品品类、初始挂价溢价率、上架时长等；需指定具体的协变量集合及回归方法（如 Logistic 回归），以量化匹配前的选择偏差。

## Corrected Claim

倾向得分 (Propensity Score) 的具体回归模型：定义 P(Treat=1 | X) = 1 / (1 + e^(-β_0 - Σβ_i X_i))，其中协变量 X 包括卖家历史信用分、商品品类、初始挂价溢价率、上架时长等；需指定具体的协变量集合及回归方法（如 Logistic 回归），以量化匹配前的选择偏差。

## Evidence

先验知识/题面给定，逻辑校验通过
