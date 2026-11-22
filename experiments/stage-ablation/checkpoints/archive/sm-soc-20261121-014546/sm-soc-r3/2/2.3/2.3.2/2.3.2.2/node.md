# N207: 成交概率敏感度系数 p'(P_ask) 的解析式：在指数需求模型 p(P) = p_0 * exp(-γ_p * (P - V)) 下，p'(P) = -γ_p

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N61

## Claim

成交概率敏感度系数 p'(P_ask) 的解析式：在指数需求模型 p(P) = p_0 * exp(-γ_p * (P - V)) 下，p'(P) = -γ_p * p(P)，其中 γ_p 为价格弹性参数，典型值 0.5-1.0，需通过历史成交数据回归估计。

## Corrected Claim

成交概率敏感度系数 p'(P_ask) 的解析式：在指数需求模型 p(P) = p_0 * exp(-γ_p * (P - V)) 下，p'(P) = -γ_p * p(P)，其中 γ_p 为价格弹性参数，典型值 0.5-1.0，需通过历史成交数据回归估计。

## Evidence

先验知识/题面给定，逻辑校验通过：对指数函数 p(P) = p_0 * exp(-γ_p * (P - V)) 求导，根据链式法则，p'(P) = p_0 * exp(-γ_p * (P - V)) * (-γ_p) = -γ_p * p(P)，推导严格成立；γ_p 作为价格弹性参数，典型值 0.5-1.0 符合金融市场中成交概率随价格偏离公允价衰减的工程经验量级。
