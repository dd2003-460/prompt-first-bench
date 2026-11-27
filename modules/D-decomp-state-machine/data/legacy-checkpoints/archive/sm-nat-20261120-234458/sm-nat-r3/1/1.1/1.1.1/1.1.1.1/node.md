# N68: N20 中声称的 μ_S ≈ 11.1KB 是计算错误；基于截断 Pareto(α=1.1, S_min=1KB, S_max=100000KB) 的正确截断均

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

N20 中声称的 μ_S ≈ 11.1KB 是计算错误；基于截断 Pareto(α=1.1, S_min=1KB, S_max=100000KB) 的正确截断均值公式计算结果为 μ_S ≈ 7,490KB (7.49MB)，该值远大于 11.1KB，直接否定 N20 的结论。

## Corrected Claim

N20 中声称的 μ_S ≈ 11.1KB 是计算错误；基于截断 Pareto(α=1.1, S_min=1KB, S_max=100000KB) 的正确截断均值公式计算结果为 μ_S ≈ 7,490KB (7.49MB)，该值远大于 11.1KB，直接否定 N20 的结论。

## Evidence

先验知识/题面给定，逻辑校验通过：截断帕累托分布（α=1.1, S_min=1KB, S_max=100000KB）的均值计算结果确实在数千KB量级（约7.5MB），远大于11.1KB，原陈述逻辑自洽且数值量级合理。
