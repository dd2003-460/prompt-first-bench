# N10: Pareto 分布下对象大小总和与头部对象占比的解析解：总字节数 E[S] = α/(α-1) * X_min (当 α>1)，前 k% 对象占总字节数的比例为

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

Pareto 分布下对象大小总和与头部对象占比的解析解：总字节数 E[S] = α/(α-1) * X_min (当 α>1)，前 k% 对象占总字节数的比例为 1 - (0.01)^((α-1)/α)，用于确定缓存需覆盖的最小对象集

## Corrected Claim

Pareto 分布下对象大小总和与头部对象占比的解析解：总字节数 E[S] = α/(α-1) * X_min (当 α>1)，前 k% 对象占总字节数的比例为 1 - (0.01)^((α-1)/α)，用于确定缓存需覆盖的最小对象集

## Evidence

父节点级核验未通过：不完备（子节点仅讨论了特定参数（α=1.1）下的数值稳定性问题，未覆盖父节点中关于“前k%对象占比解析解”以及“确定缓存最小覆盖集”的核心逻辑推导，导致内容缺失严重。）

## Search Query

Pareto distribution cumulative byte fraction head objects formula
