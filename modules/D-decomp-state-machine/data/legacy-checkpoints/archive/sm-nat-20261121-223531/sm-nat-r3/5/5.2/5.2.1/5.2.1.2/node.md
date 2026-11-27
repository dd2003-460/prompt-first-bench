# N183: LFU 阈值 $h_{th}$ 的确定机制：在容量受限假设下（假设 $S_{total} > C$），$h_{th}$ 是满足 $\sum_{h_i > h_{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

LFU 阈值 $h_{th}$ 的确定机制：在容量受限假设下（假设 $S_{total} > C$），$h_{th}$ 是满足 $\sum_{h_i > h_{th}} S_i \le C$ 的最大热度值。由于热度 $H$ 服从 Pareto($\beta=0.9$)，$h_{th}$ 对应于按热度降序排列的对象中，累计大小达到 $C$ 时的热度截断点。

## Corrected Claim

LFU 阈值 $h_{th}$ 的确定机制：在容量受限假设下（假设 $S_{total} > C$），$h_{th}$ 是满足 $\sum_{h_i > h_{th}} S_i \le C$ 的最大热度值。由于热度 $H$ 服从 Pareto($\beta=0.9$)，$h_{th}$ 对应于按热度降序排列的对象中，累计大小达到 $C$ 时的热度截断点。

## Evidence

先验知识/题面给定，逻辑校验通过：在容量受限且对象按热度降序排列的LFU/缓存替换策略中，阈值定义为累计大小不超过容量C的最大热度截断点，符合定义逻辑。
