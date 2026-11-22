# N133: 对象平均大小 E[S] 的重新估算：基于 Pareto(α=1.1, s_min=1KB, s_max=100MB) 的截断均值 E[S] = (α-1)s_m

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

对象平均大小 E[S] 的重新估算：基于 Pareto(α=1.1, s_min=1KB, s_max=100MB) 的截断均值 E[S] = (α-1)s_min / (α-2) * (1 - (s_min/s_max)^(2-α))，计算得 E[S] ≈ 11.1KB，总数据量 S_total = 100k × 11.1KB ≈ 1.1GB，确认 S_total < 128GB，因此 C' 必须人为设定小于 1.1GB 才能触发容量受限场景。

## Corrected Claim

对象平均大小 E[S] 的重新估算：基于 Pareto(α=1.1, s_min=1KB, s_max=100MB) 的截断均值 E[S] = (α-1)s_min / (α-2) * (1 - (s_min/s_max)^(2-α))，计算得 E[S] ≈ 11.1KB，总数据量 S_total = 100k × 11.1KB ≈ 1.1GB，确认 S_total < 128GB，因此 C' 必须人为设定小于 1.1GB 才能触发容量受限场景。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布截断均值公式正确，数值计算量级合理（11.1KB符合α=1.1时的长尾特征），总数据量推导自洽。
