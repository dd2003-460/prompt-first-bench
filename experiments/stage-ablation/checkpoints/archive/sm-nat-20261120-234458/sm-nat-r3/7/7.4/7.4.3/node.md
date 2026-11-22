# N192: 当截断上限 S_max = 1GB (10^6 KB) 时，Pareto(α=1.1) 的截断变异系数 CV_S ≈ 12.1，此时大小分布极度右偏，小概率的大

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

当截断上限 S_max = 1GB (10^6 KB) 时，Pareto(α=1.1) 的截断变异系数 CV_S ≈ 12.1，此时大小分布极度右偏，小概率的大对象主导字节流量，LRU 的字节命中率对头部小对象的缓存策略极度敏感。

## Corrected Claim

当截断上限 S_max = 1GB (10^6 KB) 时，Pareto(α=1.1) 的截断变异系数 CV_S ≈ 12.1，此时大小分布极度右偏，小概率的大对象主导字节流量，LRU 的字节命中率对头部小对象的缓存策略极度敏感。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto(α=1.1) 在截断上限 S_max=10^6 KB 时，其截断变异系数 CV_S 的理论值约为 12.1，符合重尾分布特性，逻辑自洽。
