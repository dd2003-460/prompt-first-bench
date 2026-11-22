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

父节点级核验未通过：不完备, 有冗余（子节点仅覆盖了分布的两端（头部和尾部），遗漏了中间区域（如 k 在 1001 到 N_cache-101 之间）的行为，导致不完备。此外，两个子节点本质上是同一公式 W_LRU(k) = 1/sum_{j>k} λ_j 在不同 k 值下的具体实例化，属于同一参数的不同取值，存在结构性冗余。）
