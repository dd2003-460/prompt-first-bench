# N20: 候选最小干预措施2：对降价后48小时内无咨询的卖家推送‘价格竞争力诊断’，计算其当前价与同类活跃商品加权均价的比值 R = P_current / Σ(w_i 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

候选最小干预措施2：对降价后48小时内无咨询的卖家推送‘价格竞争力诊断’，计算其当前价与同类活跃商品加权均价的比值 R = P_current / Σ(w_i * P_i)，若 R > 1.15 则触发强制建议降价阈值 ΔP_min = P_current * (R - 1.15)

## Corrected Claim

候选最小干预措施2：对降价后48小时内无咨询的卖家推送‘价格竞争力诊断’，计算其当前价与同类活跃商品加权均价的比值 R = P_current / Σ(w_i * P_i)，若 R > 1.15 则触发强制建议降价阈值 ΔP_min = P_current * (R - 1.15)

## Evidence

先验知识/题面给定，逻辑校验通过
