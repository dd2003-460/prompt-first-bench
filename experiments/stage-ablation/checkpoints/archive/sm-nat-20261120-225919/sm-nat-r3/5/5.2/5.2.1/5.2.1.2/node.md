# N204: 在 S_min=10KB, S_max=100MB 截断下，Pareto(α=1.1) 的截断均值 E[S]_trunc ≈ 110KB * (1 - (100

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N74

## Claim

在 S_min=10KB, S_max=100MB 截断下，Pareto(α=1.1) 的截断均值 E[S]_trunc ≈ 110KB * (1 - (10000)^(-0.1)) ≈ 110KB * 0.63 ≈ 69.3KB，S_total ≈ 6.93GB，C/S_total ≈ 18.5，H_LRU 下界仍接近 100%，但计算复杂度因对象数量减少而降低。

## Corrected Claim

在 S_min=10KB, S_max=100MB 截断下，Pareto(α=1.1) 的截断均值 E[S]_trunc 应显著大于 69.3KB（理论计算约为 1.1GB 左右），因此 S_total 和 C/S_total 的数值需重新计算，原陈述中的具体数值不可信。

## Evidence

[质询]数值计算存在严重错误：Pareto(α=1.1) 在 [10KB, 100MB] 截断下的均值远大于 69.3KB（理论值约为 1.1GB 量级），且 110KB * 0.63 的算术结果约为 69.3KB 但前提系数 110KB 缺乏依据，导致 S_total 和 C/S_total 的推导完全失效。 | 逻辑校验失败：Pareto 分布截断均值公式应用错误，数值量级严重偏离理论预期（α=1.1 时均值应接近上限或显著高于下限，而非仅 69.3KB），且内部算术与统计性质矛盾。
