# N120: 在 M/C = 1.0 的极限工作点下，若引入 TTL 机制（TTL=1天），LRU 队列中对象的平均驻留时间 T_res_avg 受限于 TTL，P_expi

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N45

## Claim

在 M/C = 1.0 的极限工作点下，若引入 TTL 机制（TTL=1天），LRU 队列中对象的平均驻留时间 T_res_avg 受限于 TTL，P_expire = 1 - exp(-1/100) ≈ 0.00995，折损系数约为 0.990。

## Corrected Claim

在 M/C = 1.0 的极限工作点下，若引入 TTL 机制（TTL=1天），LRU 队列中对象的平均驻留时间 T_res_avg 受限于 TTL，P_expire = 1 - exp(-1/100) ≈ 0.00995，折损系数约为 0.990。

## Evidence

先验知识/题面给定，逻辑校验通过：指数分布下平均驻留时间受TTL截断，P_expire = 1 - exp(-TTL/T_res_avg) 计算正确，折损系数 1-P_expire 数值合理。
