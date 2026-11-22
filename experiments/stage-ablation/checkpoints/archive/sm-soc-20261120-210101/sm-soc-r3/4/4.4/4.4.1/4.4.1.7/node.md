# N298: 需求函数 Q(P) 采用线性形式（前沿工作点1）：Q(P) = a - b*P，其中 b > 0。一阶条件 dU/dP = a - 2b*P + b*C = 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N82, N83, N84

## Claim

需求函数 Q(P) 采用线性形式（前沿工作点1）：Q(P) = a - b*P，其中 b > 0。一阶条件 dU/dP = a - 2b*P + b*C = 0，解得 P* = (a + b*C) / (2b)。Trade-off：线性假设在高价区（P > P_max）失效，Q 可能为负，需截断。适用场景：价格弹性近似恒定的中低价位商品。

## Corrected Claim

需求函数 Q(P) 采用线性形式（前沿工作点1）：Q(P) = a - b*P，其中 b > 0。一阶条件 dU/dP = a - 2b*P + b*C = 0，解得 P* = (a + b*C) / (2b)。Trade-off：线性假设在高价区（P > P_max）失效，Q 可能为负，需截断。适用场景：价格弹性近似恒定的中低价位商品。

## Evidence

先验知识/题面给定，逻辑校验通过：线性需求函数 Q=a-bP 下，利润函数 U=(P-C)(a-bP) 的一阶导数确为 a-2bP+bC，解得 P*=(a+bC)/2b，推导自洽且符合经济学直觉。

## Search Query

linear demand function Nash equilibrium price first order condition
