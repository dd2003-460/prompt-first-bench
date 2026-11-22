# N6: 稳态缓存容量约束：总对象数 N=100,000，内存 C=128GB，单对象大小服从 Pareto(α=1.1)，需计算 Pareto 分布的截断范围或归一化常

- **status**: pending
- **level**: L2
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

稳态缓存容量约束：总对象数 N=100,000，内存 C=128GB，单对象大小服从 Pareto(α=1.1)，需计算 Pareto 分布的截断范围或归一化常数，确保 E[size] 有限且 C/N 小于最大对象大小，否则缓存无法容纳所有对象，LRU 命中率上限为 100%。

## Corrected Claim

稳态缓存容量约束：总对象数 N=100,000，内存 C=128GB，单对象大小服从 Pareto(α=1.1)，需计算 Pareto 分布的截断范围或归一化常数，确保 E[size] 有限且 C/N 小于最大对象大小，否则缓存无法容纳所有对象，LRU 命中率上限为 100%。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 855)
