# N412: 西部长尾用户对整体 P99 延迟的贡献项 L_p99_tail_contribution = w_tail * (L_prop_tail + L_jitter_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N136

## Claim

西部长尾用户对整体 P99 延迟的贡献项 L_p99_tail_contribution = w_tail * (L_prop_tail + L_jitter_p99 + L_backhaul_tail * (1 - H_tail))，其中 H_tail 为西部用户缓存命中率（通常低于全国均值 5-10%，因内容热度分布差异），L_backhaul_tail 为西部回源延迟（比东部高 10-20 ms）。

## Corrected Claim

西部长尾用户对整体 P99 延迟的贡献项 L_p99_tail_contribution = w_tail * (L_prop_tail + L_jitter_p99 + L_backhaul_tail * (1 - H_tail))，其中 H_tail 为西部用户缓存命中率（通常低于全国均值 5-10%，因内容热度分布差异），L_backhaul_tail 为西部回源延迟（比东部高 10-20 ms）。

## Evidence

先验知识/题面给定，逻辑校验通过
