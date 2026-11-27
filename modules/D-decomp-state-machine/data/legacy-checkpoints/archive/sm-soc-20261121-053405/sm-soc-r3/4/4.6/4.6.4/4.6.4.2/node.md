# N206: 投影1：对数回归模型定义：建立回归模型 \(\ln(\Delta R) = \alpha + S \cdot \ln(\Delta P_{consult}) +

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N78

## Claim

投影1：对数回归模型定义：建立回归模型 \(\ln(\Delta R) = \alpha + S \cdot \ln(\Delta P_{consult}) + \epsilon\)。若数据支持该线性对数关系，则斜率系数 S 即为敏感度系数。需检验残差的正态性和异方差性，若违反假设，需使用稳健标准误重新估计 S。

## Corrected Claim

投影1：对数回归模型定义：建立回归模型 \(\ln(\Delta R) = \alpha + S \cdot \ln(\Delta P_{consult}) + \epsilon\)。若数据支持该线性对数关系，则斜率系数 S 即为敏感度系数。需检验残差的正态性和异方差性，若违反假设，需使用稳健标准误重新估计 S。

## Evidence

先验知识/题面给定，逻辑校验通过：对数-对数回归模型中斜率系数确实代表弹性/敏感度，且残差检验与稳健标准误的使用符合计量经济学标准规范。

## Search Query

log-log regression model sensitivity coefficient robust standard errors
