# N56: 自建 10 POP 单请求 P99 延迟的构成公式：P99_self = P99(RTT_user_pop) + P99(T_proc_pop) + (1-H_

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

自建 10 POP 单请求 P99 延迟的构成公式：P99_self = P99(RTT_user_pop) + P99(T_proc_pop) + (1-H_pop)*P99(T_origin_fetch_self)，其中 H_pop 为自建 POP 缓存命中率。

## Corrected Claim

自建 10 POP 单请求 P99 延迟的构成公式：P99_self = P99(RTT_user_pop) + P99(T_proc_pop) + (1-H_pop)*P99(T_origin_fetch_self)，其中 H_pop 为自建 POP 缓存命中率。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数（H_pop, T_origin, T_threshold）下的两个具体算例，属于冗余而非正交分解；且未涵盖公式中关键项 P99(RTT_user_pop) 和 P99(T_proc_pop) 的独立分析或约束，导致对父节点公式的覆盖不完备。）

## Search Query

Self-built POP P99 latency breakdown RTT processing cache miss
