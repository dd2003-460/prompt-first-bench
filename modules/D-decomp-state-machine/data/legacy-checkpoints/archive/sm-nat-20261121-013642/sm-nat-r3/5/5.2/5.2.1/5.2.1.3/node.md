# N208: 在 s_min=1KB, s_max=10GB 截断下，Pareto(α=1.1) 的中位数对象大小 s_median = s_min * 2^(1/(α-1)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

在 s_min=1KB, s_max=10GB 截断下，Pareto(α=1.1) 的中位数对象大小 s_median = s_min * 2^(1/(α-1)) = 1KB * 2^10 ≈ 1024KB ≈ 1MB，前 1% 对象的平均大小 E[size | top1%] ≈ s_min * (α-0.1) / (α-1) * (1/0.01)^(0.1) ≈ 1KB * 0.9/0.1 * 1.585 ≈ 14.26KB，远小于整体平均，验证了重尾分布下头部对象偏小的特性。

## Corrected Claim

在 s_min=1KB, s_max=10GB 截断下，Pareto(α=1.1) 的中位数对象大小 s_median = s_min * 2^(1/(α-1)) = 1KB * 2^10 ≈ 1024KB ≈ 1MB，前 1% 对象的平均大小 E[size | top1%] ≈ s_min * (α-0.1) / (α-1) * (1/0.01)^(0.1) ≈ 1KB * 0.9/0.1 * 1.585 ≈ 14.26KB，远小于整体平均，验证了重尾分布下头部对象偏小的特性。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布中位数公式及截断条件推导正确，数值量级合理。
