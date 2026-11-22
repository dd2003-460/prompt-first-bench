# N22: 在 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布下，LRU 队列中第 k 个对象的 W_LRU(k) 近似为 1 / (sum_

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

在 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布下，LRU 队列中第 k 个对象的 W_LRU(k) 近似为 1 / (sum_{j>k} λ_j)，其中 λ_j 是对象 j 的请求速率。

## Corrected Claim

在 Pareto(α=1.1) 大小分布和 Pareto(β=0.9) 热度分布下，LRU 队列中第 k 个对象的 W_LRU(k) 近似为 1 / (sum_{j>k} λ_j)，其中 λ_j 是对象 j 的请求速率。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点仅覆盖了 k 的两个极端情况（头部和尾部），忽略了中间大部分区域（k 从 1000 到 N_cache-100）的行为，导致完备性不足。此外，两个子节点本质上是同一公式 W_LRU(k) ≈ 1 / (sum_{j>k} λ_j) 在不同 k 值下的特例，具有高度冗余性，可合并为单个节点描述该函数随 k 变化的单调性。）
