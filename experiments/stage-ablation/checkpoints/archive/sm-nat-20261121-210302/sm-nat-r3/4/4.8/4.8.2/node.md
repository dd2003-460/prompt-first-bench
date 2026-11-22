# N67: LRU 有效命中率折扣因子 D 的精确计算：D = 1 - (1 - 0.01) * (T_evict / T_update) / (1 + T_evict /

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N16

## Claim

LRU 有效命中率折扣因子 D 的精确计算：D = 1 - (1 - 0.01) * (T_evict / T_update) / (1 + T_evict / T_update)，基于 Markov 链稳态概率推导

## Corrected Claim

在特定Markov链稳态假设下，LRU有效命中率折扣因子D可表示为 D = 1 - (1 - 0.01) * (T_evict / T_update) / (1 + T_evict / T_update)，该公式依赖于具体的更新与驱逐事件概率模型。

## Evidence

父节点级核验未通过：不完备（子节点仅覆盖了公式在两个特定极限/工况下的数值验证（T_evict >> T_update 和 T_evict ≈ T_update），未能覆盖父节点中提到的核心推导逻辑（基于 Markov 链稳态概率推导）。父节点强调的是‘精确计算’及其‘推导基础’，而子节点缺失了对推导过程或一般性数学性质的分解，导致内容不完备。）
