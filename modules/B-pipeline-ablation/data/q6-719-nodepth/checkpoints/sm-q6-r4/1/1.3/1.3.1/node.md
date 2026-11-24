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

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一公式在不同参数（H_pop, T_origin_fetch, 阈值T）下的具体数值计算实例，属于参数取值的枚举而非逻辑维度的分解，因此存在冗余。此外，父节点公式包含 RTT 和 Proc 两项，但子节点仅详细讨论了回源项的影响，未覆盖 RTT/Proc 的构成或约束，导致不完备。）

## Search Query

Self-built POP P99 latency breakdown RTT processing cache miss
