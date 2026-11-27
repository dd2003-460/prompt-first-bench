# N80: 步骤1的具体计算：E[S] = ∫[S_min, S_max] s * (α S_min^α / s^(α+1)) ds = α S_min / (α-1) *

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27

## Claim

步骤1的具体计算：E[S] = ∫[S_min, S_max] s * (α S_min^α / s^(α+1)) ds = α S_min / (α-1) * (1 - (S_min/S_max)^(α-1))，代入 α=1.1, S_min=1KB, S_max=100MB 得 E[S]≈6.9KB；若 S_max 未知，需用总字节量约束反推：总字节量 = 10^5 * E[S] 需与 CDN 实际存储规模匹配，否则 E[S] 假设失效

## Corrected Claim

步骤1的具体计算：E[S] = ∫[S_min, S_max] s * (α S_min^α / s^(α+1)) ds = α S_min / (α-1) * (1 - (S_min/S_max)^(α-1))，代入 α=1.1, S_min=1KB, S_max=100MB 得 E[S]≈6.9KB；若 S_max 未知，需用总字节量约束反推：总字节量 = 10^5 * E[S] 需与 CDN 实际存储规模匹配，否则 E[S] 假设失效

## Evidence

先验知识/题面给定，逻辑校验通过：帕累托分布截断期望公式推导正确，数值量级（6.9KB）符合CDN对象大小分布直觉
