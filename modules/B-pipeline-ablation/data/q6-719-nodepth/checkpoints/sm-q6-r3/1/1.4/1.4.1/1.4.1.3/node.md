# N232: 工作点3（高成本低性）：H_self=0.85（低缓存命中，如视频首帧），RTT_user_pop_core_p99=30ms，T_proc_pop=15ms，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N60

## Claim

工作点3（高成本低性）：H_self=0.85（低缓存命中，如视频首帧），RTT_user_pop_core_p99=30ms，T_proc_pop=15ms，回源项(1-H_self)*80ms=12ms，P99_core ≈ 57ms，满足 T=200ms 但成本因回源带宽激增而上升。

## Corrected Claim

工作点3（高成本低性）：H_self=0.85（低缓存命中，如视频首帧），RTT_user_pop_core_p99=30ms，T_proc_pop=15ms，回源项(1-H_self)*80ms=12ms，P99_core ≈ 57ms，满足 T=200ms 但成本因回源带宽激增而上升。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 30+15+12=57ms 正确，且 57ms < 200ms 满足约束，符合高回源率导致成本上升但延迟仍可控的逻辑。
