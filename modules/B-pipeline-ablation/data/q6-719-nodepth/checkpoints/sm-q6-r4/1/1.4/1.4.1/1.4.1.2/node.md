# N231: 工作点2（中性价比最优）：H_self=0.95（标准缓存命中），RTT_user_pop_core_p99=20ms，T_proc_pop=10ms，回源项(

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

工作点2（中性价比最优）：H_self=0.95（标准缓存命中），RTT_user_pop_core_p99=20ms，T_proc_pop=10ms，回源项(1-H_self)*50ms=2.5ms，P99_core ≈ 32.5ms，满足 T=150ms。

## Corrected Claim

工作点2（中性价比最优）：H_self=0.95（标准缓存命中），RTT_user_pop_core_p99=20ms，T_proc_pop=10ms，回源项(1-H_self)*50ms=2.5ms，P99_core ≈ 32.5ms，满足 T=150ms。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 20 + 10 + (1-0.95)*50 = 32.5ms 正确，且 32.5ms < 150ms 满足约束。
