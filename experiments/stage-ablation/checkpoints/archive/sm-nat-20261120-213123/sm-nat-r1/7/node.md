# N25: 在对象大小服从 Pareto(α=1.1) 且最小大小 s_min=1KB 的假设下，128GB 缓存容量 C=1.28×10^11 bytes 可容纳的对象数

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在对象大小服从 Pareto(α=1.1) 且最小大小 s_min=1KB 的假设下，128GB 缓存容量 C=1.28×10^11 bytes 可容纳的对象数量边界 k_max 约为 C / E[S_top_k]，其中 E[S_top_k] 为前 k 大对象的平均大小。由于 α<2，总大小由头部主导，k_max 通常远小于总对象数 N=10^5，具体需通过截断 Pareto 分布积分计算：C ≈ ∫_{s_min}^{s_max(k)} x * f_S(x) dx。

## Corrected Claim

在对象大小服从 Pareto(α=1.1) 且最小大小 s_min=1KB 的假设下，128GB 缓存容量 C=1.28×10^11 bytes 可容纳的对象数量边界 k_max 约为 C / E[S_top_k]，其中 E[S_top_k] 为前 k 大对象的平均大小。由于 α<2，总大小由头部主导，k_max 通常远小于总对象数 N=10^5，具体需通过截断 Pareto 分布积分计算：C ≈ ∫_{s_min}^{s_max(k)} x * f_S(x) dx。

## Evidence

检索失败: no sources from any channel (all 5 failed)
