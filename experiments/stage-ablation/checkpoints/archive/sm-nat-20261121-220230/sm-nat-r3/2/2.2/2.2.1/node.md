# N49: 热度时间稳定性量化指标：对象热度排名在连续两个时间步 t 和 t+1 之间的 Spearman 相关系数 ρ_rank(t, t+1)，若 ρ_rank > 0

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N12

## Claim

热度时间稳定性量化指标：对象热度排名在连续两个时间步 t 和 t+1 之间的 Spearman 相关系数 ρ_rank(t, t+1)，若 ρ_rank > 0.9，则 LFU 增益显著；若 ρ_rank < 0.5，则 LFU 增益可忽略。

## Corrected Claim

热度时间稳定性量化指标：对象热度排名在连续两个时间步 t 和 t+1 之间的 Spearman 相关系数 ρ_rank(t, t+1) 越高，LFU 的潜在增益通常越显著；反之，若 ρ_rank 较低，LFU 增益可能有限。具体阈值需根据实际业务场景调优。

## Evidence

父节点级核验未通过：有冗余（子节点在逻辑上正交且覆盖了父节点定义的高、中、低稳定性三个区间，内容完整。然而，三个子节点本质上是同一量化指标（Spearman相关系数）在不同数值区间下的具体实例化，属于典型的‘参数取值枚举’，存在结构性冗余。）

## Search Query

Spearman correlation of object popularity ranks over time CDN
