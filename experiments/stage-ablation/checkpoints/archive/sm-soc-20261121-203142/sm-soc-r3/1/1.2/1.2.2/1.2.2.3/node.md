# N117: 非线性点击率衰减效应：在 P_ask 超过某个临界点 P_crit 后，CTR 可能因‘价格过高’感知而急剧下降，需检验线性模型 E[CTR] = CTR_ba

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

非线性点击率衰减效应：在 P_ask 超过某个临界点 P_crit 后，CTR 可能因‘价格过高’感知而急剧下降，需检验线性模型 E[CTR] = CTR_base * (1 + γ * δ) 的残差是否存在显著的非线性模式（如二次项系数显著），若存在，需修正为分段线性或指数衰减模型。

## Corrected Claim

非线性点击率衰减效应：在 P_ask 超过某个临界点 P_crit 后，CTR 可能因‘价格过高’感知而急剧下降，需检验线性模型 E[CTR] = CTR_base * (1 + γ * δ) 的残差是否存在显著的非线性模式（如二次项系数显著），若存在，需修正为分段线性或指数衰减模型。

## Evidence

先验知识/题面给定，逻辑校验通过
