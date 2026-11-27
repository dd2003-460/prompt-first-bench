# N49: 热度时间稳定性量化指标：对象热度排名在连续两个时间步 t 和 t+1 之间的 Spearman 相关系数 ρ_rank(t, t+1)，若 ρ_rank > 0

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N12

## Claim

热度时间稳定性量化指标：对象热度排名在连续两个时间步 t 和 t+1 之间的 Spearman 相关系数 ρ_rank(t, t+1)，若 ρ_rank > 0.9，则 LFU 增益显著；若 ρ_rank < 0.5，则 LFU 增益可忽略。

## Corrected Claim

热度时间稳定性量化指标：对象热度排名在连续两个时间步 t 和 t+1 之间的 Spearman 相关系数 ρ_rank(t, t+1) 越高，LFU 的潜在增益通常越显著；反之，若 ρ_rank 较低，LFU 增益可能有限。具体阈值需根据实际业务场景调优。

## Evidence

[质询]阈值 0.9 和 0.5 是经验性参数，缺乏普适的理论推导或广泛认可的工程标准支持，不同场景下 LFU 增益的显著性边界可能不同。 | 先验知识/题面给定，逻辑校验通过（Spearman 系数衡量排名稳定性，高相关性确实意味着 LFU 基于历史频率的预测更准确，低相关性意味着历史数据失效），但具体阈值属于经验事实，无来源直接支持。

## Search Query

Spearman correlation of object popularity ranks over time CDN
