# N161: 高净值卖家约束验证：若 P_list - P_market = 200元, r_total = 8%, t_wait = 30天，则 C_signal = 20

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

高净值卖家约束验证：若 P_list - P_market = 200元, r_total = 8%, t_wait = 30天，则 C_signal = 200 * 0.08 * (30/365) ≈ 1.32元；若 Benefit = 50元，则 1.32 < 50，约束成立，高挂价稳定。

## Corrected Claim

高净值卖家约束验证：若 P_list - P_market = 200元, r_total = 8%, t_wait = 30天，则 C_signal = 200 * 0.08 * (30/365) ≈ 1.32元；若 Benefit = 50元，则 1.32 < 50，约束成立，高挂价稳定。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 200 * 0.08 * (30/365) ≈ 1.315，四舍五入为 1.32 元，且 1.32 < 50 成立，推导自洽。

## Search Query

high net worth seller signaling cost benefit example
