# N26: 在 α=1.1 (size) 和 β=0.9 (frequency) 的 Pareto 分布下，由于 α 接近 1，大小分布具有极重尾特征，前 1% 的对象可能

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在 α=1.1 (size) 和 β=0.9 (frequency) 的 Pareto 分布下，由于 α 接近 1，大小分布具有极重尾特征，前 1% 的对象可能占据总数据量的 50%-70%，导致缓存容量 C=128GB 可能仅能覆盖极少数超大对象或大量微小对象，需通过截断 Pareto 分布计算累积质量。

## Corrected Claim

在 α=1.1 (size) 和 β=0.9 (frequency) 的 Pareto 分布下，由于 α 接近 1，大小分布具有极重尾特征，前 1% 的对象可能占据总数据量的 50%-70%，导致缓存容量 C=128GB 可能仅能覆盖极少数超大对象或大量微小对象，需通过截断 Pareto 分布计算累积质量。

## Evidence

检索失败: no sources from any channel (all 5 failed)
