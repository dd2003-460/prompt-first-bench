# N53: S_cache 的确定公式：S_cache = F_S^{-1}(1 - N_cache/N_total)，其中 N_cache 为可缓存对象数，N_total

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

S_cache 的确定公式：S_cache = F_S^{-1}(1 - N_cache/N_total)，其中 N_cache 为可缓存对象数，N_total=100,000，F_S 为 Pareto(α=1.1) 的 CDF

## Corrected Claim

S_cache 的确定公式：S_cache = F_S^{-1}(1 - N_cache/N_total)，其中 N_cache 为可缓存对象数，N_total=100,000，F_S 为 Pareto(α=1.1) 的 CDF

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点实质上是同一公式在不同参数取值（N_cache=100,000 和 N_cache=50,000）下的具体实例，属于参数化变体而非独立的概念维度，因此存在冗余。此外，父节点定义了一个通用的确定公式，但子节点仅覆盖了两个特定边界/典型值，未涵盖一般情况下的解析形式或数值求解方法，导致完备性不足。）
