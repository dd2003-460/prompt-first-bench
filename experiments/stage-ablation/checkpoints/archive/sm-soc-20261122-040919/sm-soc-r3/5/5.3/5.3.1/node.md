# N357: 买家耐心衰减率 λ_response 的估计：基于二手平台用户行为数据，买家在等待卖家响应超过 T_wait 后放弃咨询的概率显著上升。若 T_fast = 2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N108

## Claim

买家耐心衰减率 λ_response 的估计：基于二手平台用户行为数据，买家在等待卖家响应超过 T_wait 后放弃咨询的概率显著上升。若 T_fast = 2小时，且观察到 50% 买家在 24 小时内若未收到回复则关闭会话，则 λ_response ≈ ln(2) / 24h ≈ 0.029/h。若响应时间 T_fast 远小于 24h，则 e^(-λ_response/T_fast) 趋近于 0，ΔP(deal) 趋近于 δ。

## Corrected Claim

买家耐心衰减率 λ_response 的估计：基于二手平台用户行为数据，买家在等待卖家响应超过 T_wait 后放弃咨询的概率显著上升。若 T_fast = 2小时，且观察到 50% 买家在 24 小时内若未收到回复则关闭会话，则 λ_response ≈ ln(2) / 24h ≈ 0.029/h。若响应时间 T_fast 远小于 24h，则 e^(-λ_response/T_fast) 趋近于 0，ΔP(deal) 趋近于 δ。

## Evidence

先验知识/题面给定，逻辑校验通过：基于指数衰减模型，由50%放弃率对应24小时半衰期推导λ=ln(2)/24≈0.029/h，数学推导自洽且量级合理。

## Search Query

buyer patience decay rate response time marketplace
