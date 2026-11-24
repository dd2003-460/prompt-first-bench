# N538: P_video 的敏感性边界：当短视频渗透率提升导致 P_video 从 30% 增至 50% 时，加权平均对象大小 s_weighted 将从约 4.6MB 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N177

## Claim

P_video 的敏感性边界：当短视频渗透率提升导致 P_video 从 30% 增至 50% 时，加权平均对象大小 s_weighted 将从约 4.6MB 跃升至约 10.2MB，触发 s_critical (3.2MB) 阈值，使公有云带宽成本占比超过 70%，此时自建策略的成本优势扩大，需重新评估策略排序。

## Corrected Claim

当短视频渗透率提升导致 P_video 从 30% 增至 50% 时，加权平均对象大小 s_weighted 将从约 4.6MB 显著增加（具体数值需依据对象大小分布重新计算），若该增长导致成本结构变化，需重新评估策略排序。

## Evidence

[质询]数值量级与逻辑推导存在潜在矛盾：若 s_weighted 从 4.6MB 跃升至 10.2MB，增幅约为 122%。通常加权平均大小由对象大小分布决定，若短视频（假设大小显著大于其他对象）渗透率从 30% 增至 50%，除非短视频对象大小极大（如几十MB以上）且其他对象极小，否则 10.2MB 的跃升幅度可能偏高；此外，'触发 s_critical (3.2MB)' 表述模糊，因为 4.6MB 已大于 3.2MB，若 3.2MB 是阈值，则初始状态已触发，此处逻辑表述可能存在歧义或错误。 | 来源不可用，且逻辑校验发现 s_critical 阈值与初始 s_weighted 数值存在逻辑矛盾（4.6MB > 3.2MB，初始即应触发），导致因果链条不清晰。

## Search Query

short video traffic growth impact on CDN bandwidth cost
