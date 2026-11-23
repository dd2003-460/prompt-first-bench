# N114: 全自建策略下，覆盖 90% 核心流量（华东/华南/华北）所需的最低 POP 部署数量 $N_{pop}^{min}$ 及剩余 10% 长尾流量回源路径的平均 R

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

全自建策略下，覆盖 90% 核心流量（华东/华南/华北）所需的最低 POP 部署数量 $N_{pop}^{min}$ 及剩余 10% 长尾流量回源路径的平均 RTT 增量 $\Delta RTT_{tail}$（ms），用于校验 P99≤150ms 约束是否满足。

## Corrected Claim

在全自建策略下，覆盖90%核心流量所需的最低POP部署数量及剩余10%长尾流量的平均RTT增量需基于具体的用户地理分布、网络拓扑及带宽约束进行仿真计算，无法仅凭区域划分直接得出唯一数值。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一优化问题在不同约束权重下的三个离散采样点（N=3, 6, 10），属于同一参数维度的不同取值，存在高度冗余；且父节点明确要求求解'最低'部署数量 N_min 和对应的 ΔRTT_tail，子节点仅提供了静态工作点示例，未给出推导 N_min 的逻辑或具体数值结论（例如是否 N=4 或 5 也能满足约束），未能直接回答父节点的核心问题。）

## Search Query

CDN POP coverage latency tail distribution China region
