# N155: 在 γ=0.5（更新率与大小平方根正相关）的中间工作点下，更新率随大小增长放缓，P_invalidate(s) 的分布更均匀；此时 D_bytes 介于基准值（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

在 γ=0.5（更新率与大小平方根正相关）的中间工作点下，更新率随大小增长放缓，P_invalidate(s) 的分布更均匀；此时 D_bytes 介于基准值（0.99998）和 γ=1 极限值之间，具体数值取决于截断 Pareto 分布中 s^(0.5) 的矩 E[S^0.5] 与 E[S] 的比值，该比值可通过数值积分求得。

## Corrected Claim

在 γ=0.5（更新率与大小平方根正相关）的中间工作点下，更新率随大小增长放缓，P_invalidate(s) 的分布更均匀；此时 D_bytes 介于基准值（0.99998）和 γ=1 极限值之间，具体数值取决于截断 Pareto 分布中 s^(0.5) 的矩 E[S^0.5] 与 E[S] 的比值，该比值可通过数值积分求得。

## Evidence

先验知识/题面给定，逻辑校验通过
