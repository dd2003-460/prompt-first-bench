# N230: 工作点1（高性低成）：H_self=0.98（极高缓存命中），RTT_user_pop_core_p99=15ms，T_proc_pop=5ms，回源项(1-H

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

工作点1（高性低成）：H_self=0.98（极高缓存命中），RTT_user_pop_core_p99=15ms，T_proc_pop=5ms，回源项(1-H_self)*50ms=1ms，P99_core ≈ 21ms，满足 T=100ms。

## Corrected Claim

工作点1（高性低成）：H_self=0.98（极高缓存命中），RTT_user_pop_core_p99=15ms，T_proc_pop=5ms，回源项(1-H_self)*50ms=1ms，P99_core ≈ 21ms，满足 T=100ms。

## Evidence

先验知识/题面给定，逻辑校验通过：0.98*15 + 0.02*50 + 5 = 14.7 + 1 + 5 = 20.7ms ≈ 21ms，且 21ms < 100ms，数值量级与逻辑自洽。
