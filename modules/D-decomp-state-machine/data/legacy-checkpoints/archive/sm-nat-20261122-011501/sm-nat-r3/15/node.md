# N194: 基于通用理论记忆（Recall）：LRU 在稳态下等效于保留访问间隔最短的对象集合；对于 Zipf/Pareto 分布负载，LRU 的字节命中率下界可通过缓存容

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

基于通用理论记忆（Recall）：LRU 在稳态下等效于保留访问间隔最短的对象集合；对于 Zipf/Pareto 分布负载，LRU 的字节命中率下界可通过缓存容量占总数据量的比例 C_ratio 的幂律关系 H ∝ C_ratio^γ 估算，其中 γ 通常介于 0.5-1.0 之间，具体取决于分布的尾指数。

## Corrected Claim

基于通用理论记忆（Recall）：LRU 在稳态下等效于保留访问间隔最短的对象集合；对于 Zipf/Pareto 分布负载，LRU 的字节命中率下界可通过缓存容量占总数据量的比例 C_ratio 的幂律关系 H ∝ C_ratio^γ 估算，其中 γ 通常介于 0.5-1.0 之间，具体取决于分布的尾指数。

## Evidence

检索失败: no sources from any channel (all 5 failed)
