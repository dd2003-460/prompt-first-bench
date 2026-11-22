# N139: Stale_bytes 的精确积分表达式：Stale_bytes = ∫_{k=1}^{K} S(k) * (1 - exp(-u * T_res(k))) d

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

Stale_bytes 的精确积分表达式：Stale_bytes = ∫_{k=1}^{K} S(k) * (1 - exp(-u * T_res(k))) dk，其中 T_res(k) = S(k)/R(k) 为对象 k 的驻留时间，u=0.01/天。该积分修正了 N17 中固定 12.8GB 的错误假设，需数值求解以得到实际可用容量 C_eff。

## Corrected Claim

Stale_bytes 的精确积分表达式：Stale_bytes = ∫_{k=1}^{K} S(k) * (1 - exp(-u * T_res(k))) dk，其中 T_res(k) = S(k)/R(k) 为对象 k 的驻留时间，u=0.01/天。该积分修正了 N17 中固定 12.8GB 的错误假设，需数值求解以得到实际可用容量 C_eff。

## Evidence

先验知识/题面给定，逻辑校验通过
