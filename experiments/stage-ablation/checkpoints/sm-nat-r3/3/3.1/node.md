# N14: LFU 性能增益上限：在稳态下 LFU 保留最频繁访问的对象，其命中率 H_LFU ≈ 1 - (1 - F_top)^β，F_top 为 top-K 对象的热

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

LFU 性能增益上限：在稳态下 LFU 保留最频繁访问的对象，其命中率 H_LFU ≈ 1 - (1 - F_top)^β，F_top 为 top-K 对象的热度累积占比

## Corrected Claim

LFU 性能增益上限：在稳态下 LFU 保留最频繁访问的对象，其命中率 H_LFU ≈ 1 - (1 - F_top)^β，F_top 为 top-K 对象的热度累积占比

## Evidence

父节点级核验未通过：不完备（父节点核心是LFU命中率公式 H_LFU ≈ 1 - (1 - F_top)^β，而子节点仅定义了输入参数 F_top 的计算方式及其在Pareto分布下的近似值。子节点缺失了父节点中关于命中率 H_LFU 本身的推导或定义，也未解释为何 LFU 命中率会呈现 1 - (1 - F_top)^β 的形式（即缓存命中逻辑与热度分布的映射关系），因此未覆盖父节点的关键方面。）

## Search Query

LFU vs LRU hit rate upper bound
