# N60: 核心区域（自建POP）的P99延迟 P99_core = RTT_user_pop_core_p99 + T_proc_pop + (1 - H_self) *

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

核心区域（自建POP）的P99延迟 P99_core = RTT_user_pop_core_p99 + T_proc_pop + (1 - H_self) * (RTT_pop_origin + T_transfer_origin)，其中RTT_user_pop_core_p99基于核心区域用户到最近POP的地理分布计算，H_self为自建POP缓存命中率。

## Corrected Claim

核心区域（自建POP）的P99延迟 P99_core = RTT_user_pop_core_p99 + T_proc_pop + (1 - H_self) * (RTT_pop_origin + T_transfer_origin)，其中RTT_user_pop_core_p99基于核心区域用户到最近POP的地理分布计算，H_self为自建POP缓存命中率。

## Evidence

先验知识/题面给定，逻辑校验通过
