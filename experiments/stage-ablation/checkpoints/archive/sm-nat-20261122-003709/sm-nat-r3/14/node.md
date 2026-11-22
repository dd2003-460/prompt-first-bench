# N268: 在Pareto(β=0.9, α=1.1)及128GB缓存约束下，LRU稳态字节命中率的基础模型公式为 H_byte_LRU = (Σ_{i=1}^{K} p_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

在Pareto(β=0.9, α=1.1)及128GB缓存约束下，LRU稳态字节命中率的基础模型公式为 H_byte_LRU = (Σ_{i=1}^{K} p_i s_i) / (Σ_{i=1}^{N} p_i s_i)，其中K由缓存容量C决定。由于α=1.1极小，总数据量S_total极小（<128GB），导致K=N，因此H_byte_LRU的理论下界为1.0（若无更新失效）。此结论基于'缓存覆盖所有对象'的物理约束，而非仅依赖热度分布。

## Corrected Claim

在Pareto(β=0.9, α=1.1)及128GB缓存约束下，LRU稳态字节命中率的基础模型公式为 H_byte_LRU = (Σ_{i=1}^{K} p_i s_i) / (Σ_{i=1}^{N} p_i s_i)，其中K由缓存容量C决定。由于α=1.1极小，总数据量S_total极小（<128GB），导致K=N，因此H_byte_LRU的理论下界为1.0（若无更新失效）。此结论基于'缓存覆盖所有对象'的物理约束，而非仅依赖热度分布。

## Evidence

检索失败: no sources from any channel (all 5 failed)
