# N35: 最小对象大小 s_min 的合理取值范围及典型值需基于边缘 CDN 实际负载统计确定，常见假设区间为 [1KB, 100KB]，该参数直接决定归一化容量 c 的

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

最小对象大小 s_min 的合理取值范围及典型值需基于边缘 CDN 实际负载统计确定，常见假设区间为 [1KB, 100KB]，该参数直接决定归一化容量 c 的数量级。

## Corrected Claim

最小对象大小 s_min 的合理取值范围需基于边缘 CDN 实际负载统计确定，常见假设区间通常在 KB 至百 KB 量级，该参数直接决定归一化容量 c 的数量级。

## Evidence

[质询]该陈述包含具体的经验性数值区间 [1KB, 100KB]，属于硬件/网络负载统计的经验事实，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

typical minimum object size edge CDN cache Pareto distribution s_min assumption
