# N119: 在 M/C = 1.0 的极限工作点下，若引入对象更新率 u=1%/天，LRU 队列中对象的平均驻留时间 T_res_avg 约为 100 天，导致 P_inv

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

在 M/C = 1.0 的极限工作点下，若引入对象更新率 u=1%/天，LRU 队列中对象的平均驻留时间 T_res_avg 约为 100 天，导致 P_invalid = 1 - exp(-0.01 * 100) ≈ 0.632。

## Corrected Claim

在 M/C = 1.0 的极限工作点下，若引入对象更新率 u=1%/天，LRU 队列中对象的平均驻留时间 T_res_avg 约为 100 天，导致 P_invalid = 1 - exp(-0.01 * 100) ≈ 0.632。

## Evidence

先验知识/题面给定，逻辑校验通过：M/C=1.0 时 LRU 驻留时间约为 1/C=100 天，失效概率计算 1-exp(-0.01*100)≈0.632 符合指数分布规律
