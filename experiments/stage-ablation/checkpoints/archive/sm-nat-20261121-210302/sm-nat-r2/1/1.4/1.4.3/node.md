# N36: 对象更新率 u=1%/天 对命中率的折损机制是：在 T_resident 时间内对象内容发生变化的概率为 P_stale = 1 - exp(-u * T_re

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N8

## Claim

对象更新率 u=1%/天 对命中率的折损机制是：在 T_resident 时间内对象内容发生变化的概率为 P_stale = 1 - exp(-u * T_resident)，导致原本命中的请求变为无效命中（需回源），有效命中率修正为 H_eff = H_original * (1 - P_stale * H_original)。

## Corrected Claim

对象更新率 u=1%/天 对命中率的折损机制是：在 T_resident 时间内对象内容发生变化的概率为 P_stale = 1 - exp(-u * T_resident)，导致原本命中的请求变为无效命中（需回源），有效命中率修正为 H_eff = H_original * (1 - P_stale * H_original)。

## Evidence

先验知识/题面给定，逻辑校验通过
