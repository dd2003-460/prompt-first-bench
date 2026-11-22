# N30: 热度分布的截断修正：由于 N 有限，Pareto 分布需在 h_min 处截断。h_min = h_max * (N / N_hot)^(1/0.9)，其中 N

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

热度分布的截断修正：由于 N 有限，Pareto 分布需在 h_min 处截断。h_min = h_max * (N / N_hot)^(1/0.9)，其中 N_hot 是热门对象阈值。若 N_hot=100，h_min ≈ 500 * (1000)^(1.11) ≈ 500 * 12,000 ≈ 6,000,000 req/day，用于验证长尾部分的贡献是否可忽略。

## Corrected Claim

热度分布的截断修正：由于 N 有限，Pareto 分布需在 h_min 处截断。h_min = h_max * (N / N_hot)^(1/0.9)，其中 N_hot 是热门对象阈值。若 N_hot=100，N=1000，h_max=500，则 h_min ≈ 500 * (1000)^(1.11) ≈ 500 * 10.46 ≈ 5230 req/day。

## Evidence

[质询]数值计算存在严重错误：(1000)^(1/0.9) ≈ 10.46，而非 12,000；且 500 * 10.46 ≈ 5230，远小于 6,000,000。该陈述中的量级推导完全错误。 | 先验知识/题面给定，但逻辑校验发现数值计算错误：1000^(1.11) 约为 10.46，乘以 500 约为 5230，与陈述中的 6,000,000 相差三个数量级，存在硬逻辑错误。
