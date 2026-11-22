# N6: 缓存容量 C=128GB 与工作负载总数据量 W_total 的比值（缓存覆盖率）C/W_total，其中 W_total = 10^5 × E[S]，E[S]

- **status**: verified
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

缓存容量 C=128GB 与工作负载总数据量 W_total 的比值（缓存覆盖率）C/W_total，其中 W_total = 10^5 × E[S]，E[S] 为 Pareto(α=1.1) 分布的期望大小（需假设最小大小 s_min 以计算 E[S] = α·s_min/(α-1)）

## Corrected Claim

缓存容量 C=128GB 与工作负载总数据量 W_total 的比值（缓存覆盖率）C/W_total，其中 W_total = 10^5 × E[S]，E[S] 为 Pareto(α=1.1) 分布的期望大小（需假设最小大小 s_min 以计算 E[S] = α·s_min/(α-1)）

## Evidence

先验知识/题面给定，逻辑校验通过
