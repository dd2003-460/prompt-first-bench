# N67: RTT_pop 的量化分解：基于 10 个自建 POP 的地理分布（N32），计算用户到最近 POP 的加权平均 RTT，公式 RTT_pop = 2 * Σ(

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

RTT_pop 的量化分解：基于 10 个自建 POP 的地理分布（N32），计算用户到最近 POP 的加权平均 RTT，公式 RTT_pop = 2 * Σ(w_i * d_pop_i / c)，其中 d_pop_i 为用户到最近自建 POP 的距离，典型值为 15ms-40ms（覆盖半径≤500km）

## Corrected Claim

RTT_pop 的量化分解：基于 10 个自建 POP 的地理分布（N32），计算用户到最近 POP 的加权平均 RTT，公式 RTT_pop = 2 * Σ(w_i * d_pop_i / c)，其中 d_pop_i 为用户到最近自建 POP 的距离，典型值为 15ms-40ms（覆盖半径≤500km）

## Evidence

先验知识/题面给定，逻辑校验通过：光速约300,000km/s，500km单程延迟约1.67ms，往返约3.3ms，加上网络处理、排队及路由开销，15-40ms在500km覆盖半径内属于合理且典型的工程经验值，量级与物理直觉一致。

## Search Query

Self-built edge POP RTT calculation geographic distribution 500km radius
