# N67: RTT_pop 的量化分解：基于 10 个自建 POP 的地理分布（N32），计算用户到最近 POP 的加权平均 RTT，公式 RTT_pop = 2 * Σ(

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

RTT_pop 的量化分解：基于 10 个自建 POP 的地理分布（N32），计算用户到最近 POP 的加权平均 RTT，公式 RTT_pop = 2 * Σ(w_i * d_pop_i / c)，其中 d_pop_i 为用户到最近自建 POP 的距离，典型值为 15ms-40ms（覆盖半径≤500km）

## Corrected Claim

RTT_pop 的量化分解：基于 10 个自建 POP 的地理分布（N32），计算用户到最近 POP 的加权平均 RTT，公式 RTT_pop = 2 * Σ(w_i * d_pop_i / c)，其中 d_pop_i 为用户到最近自建 POP 的距离，典型值为 15ms-40ms（覆盖半径≤500km）

## Evidence

父节点级核验未通过：非正交（子节点3（光速传播延迟）存在严重的逻辑包含和范围矛盾。它既定义了物理层光速参数 c，又给出了具体的 RTT 计算结果（5-10ms 及 15-40ms），这与父节点定义的公式结果以及子节点2（距离估算）的计算逻辑重叠且冲突。父节点已明确 RTT_pop 的典型值为 15-40ms，而子节点3内部先算出 3ms 物理延迟，又强行加上路由延迟得出 5-10ms 纯物理层结论，最后又跳回 15-40ms，导致该子节点混杂了参数定义（c）和最终结果验证，破坏了正交性。）

## Search Query

Self-built edge POP RTT calculation geographic distribution 500km radius
