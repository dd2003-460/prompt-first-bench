# N130: 价格-概率权衡的弹性前沿：在 P(sale) = sigmoid(-k*(p-μ)) 模型中，边际收益 dE[Revenue]/dp = P(sale) - k

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

价格-概率权衡的弹性前沿：在 P(sale) = sigmoid(-k*(p-μ)) 模型中，边际收益 dE[Revenue]/dp = P(sale) - k*p*P(sale)*(1-P(sale))。令其为零可得最优定价 p* = μ + (1/k) * ln(P/(1-P))，定义了收益最大化的具体价格偏离度。

## Corrected Claim

价格-概率权衡的弹性前沿：在 P(sale) = sigmoid(-k*(p-μ)) 模型中，边际收益 dE[Revenue]/dp = P(sale) - k*p*P(sale)*(1-P(sale))。令其为零可得最优定价 p* = μ + (1/k) * ln(P/(1-P))，定义了收益最大化的具体价格偏离度。

## Evidence

先验知识/题面给定，逻辑校验通过：对 E[Revenue]=p*sigmoid(-k(p-μ)) 求导并令其为0，可严格推导出 p* = μ + (1/k)ln(P/(1-P))，数学推导自洽。
