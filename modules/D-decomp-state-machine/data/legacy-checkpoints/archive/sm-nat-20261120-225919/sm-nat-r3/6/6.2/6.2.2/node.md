# N236: 若 s_min=10KB（更现实的 CDN 最小对象大小），截断至 1.3MB 的截断均值 E[S|trunc] ≈ 10KB * (1 - (1/13)^0.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N85

## Claim

若 s_min=10KB（更现实的 CDN 最小对象大小），截断至 1.3MB 的截断均值 E[S|trunc] ≈ 10KB * (1 - (1/13)^0.1) / (1 - (1/13)^0.1) ≈ 10.3KB，总大小 S_total ≈ 1.03GB，仍远小于 128GB。

## Corrected Claim

若 s_min=10KB，截断均值计算需修正。假设对象大小服从帕累托分布（α=1.1, x_min=10KB），截断至 1.3MB 的均值约为 1.2MB（具体取决于分布参数），总大小 S_total 将显著大于 1.03GB，需重新评估是否小于 128GB。

## Evidence

[质询]数学公式存在严重的逻辑与算术错误：截断均值公式中分子分母完全相同，结果恒等于 s_min (10KB)，与声称的 10.3KB 不符；且若按帕累托分布截断均值计算，数值量级应远大于 10KB（通常在 MB 级别），导致 S_total 远大于 1.03GB，结论不成立。 | 逻辑校验失败：公式 (1 - x)/(1 - x) = 1，故 E[S|trunc] 应严格等于 10KB 而非 10.3KB；且截断均值计算逻辑错误，导致总量估算严重偏低。
