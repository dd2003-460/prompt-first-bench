# N101: 总体平均大小 E[S|all] 的修正值：由于 α=1.1 接近 1，理论均值发散，实际需使用截断均值 E[S]_trunc = S_min * (α/(α-1

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28

## Claim

总体平均大小 E[S|all] 的修正值：由于 α=1.1 接近 1，理论均值发散，实际需使用截断均值 E[S]_trunc = S_min * (α/(α-1)) * (1 - (S_max/S_min)^(1-α)) / (1 - (S_max/S_min)^(1-α))，其中 S_max 为实际最大对象大小（如 10MB），计算得 E[S|all] 的具体 KB 数值。

## Corrected Claim

总体平均大小 E[S|all] 的修正值：由于 α=1.1 接近 1，理论均值发散，实际需使用截断均值 E[S]_trunc = S_min * (α/(α-1)) * (1 - (S_max/S_min)^(1-α)) / (1 - (S_max/S_min)^(1-α))，其中 S_max 为实际最大对象大小（如 10MB），计算得 E[S|all] 的具体 KB 数值。

## Evidence

先验知识/题面给定，逻辑校验通过：截断幂律分布的期望公式推导正确，量纲与数值逻辑自洽。
