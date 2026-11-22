# N342: 用于判断 PPL 增量差异是否显著的统计阈值公式：Delta_PPL_significant = max(0.5, 1.96 * StdDev_PPL / sq

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N121

## Claim

用于判断 PPL 增量差异是否显著的统计阈值公式：Delta_PPL_significant = max(0.5, 1.96 * StdDev_PPL / sqrt(N_samples))，其中 StdDev_PPL 需从多次独立量化运行中估计。

## Corrected Claim

用于判断 PPL 增量差异是否显著的统计阈值公式：Delta_PPL_significant = max(0.5, 1.96 * StdDev_PPL / sqrt(N_samples))，其中 StdDev_PPL 需从多次独立量化运行中估计。

## Evidence

先验知识/题面给定，逻辑校验通过
