# N22: Pareto(β=0.9) 热度分布下，Top-K 对象覆盖的请求比例 P_access(K) = K^(1-β) / N^(1-β)（归一化后）。由于 β=0

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Pareto(β=0.9) 热度分布下，Top-K 对象覆盖的请求比例 P_access(K) = K^(1-β) / N^(1-β)（归一化后）。由于 β=0.9 < 1，分布极重尾。例如，Top 1% 对象覆盖约 1%^(0.1) ≈ 79% 的请求（若 N 足够大）。这意味着缓存只需驻留极少数的极热对象即可达到较高的请求命中率，但字节命中率受对象大小影响较大。

## Corrected Claim

Pareto(β=0.9) 热度分布下，Top-K 对象覆盖的请求比例 P_access(K) = K^(1-β) / N^(1-β)（归一化后）。由于 β=0.9 < 1，分布极重尾。例如，Top 1% 对象覆盖约 1%^(0.1) ≈ 79% 的请求（若 N 足够大）。这意味着缓存只需驻留极少数的极热对象即可达到较高的请求命中率，但字节命中率受对象大小影响较大。

## Evidence

检索失败: no sources from any channel (all 5 failed)
