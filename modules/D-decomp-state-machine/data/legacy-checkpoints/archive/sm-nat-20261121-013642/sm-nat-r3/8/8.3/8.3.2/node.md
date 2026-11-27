# N249: κ 对缓存容量 C 的敏感性：当 C 从 128GB 降至 64GB 时，H_LRU_lower_bound 降至 0.55，H_LRU_actual 降至 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

κ 对缓存容量 C 的敏感性：当 C 从 128GB 降至 64GB 时，H_LRU_lower_bound 降至 0.55，H_LRU_actual 降至 0.68，κ 变为 0.68/0.55 ≈ 1.24，表明容量减半时下界估计的偏差略有增大。

## Corrected Claim

κ 对缓存容量 C 的敏感性：当 C 从 128GB 降至 64GB 时，H_LRU_lower_bound 降至 0.55，H_LRU_actual 降至 0.68，κ 变为 0.68/0.55 ≈ 1.24，表明容量减半时下界估计的偏差略有增大。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 0.68/0.55 ≈ 1.236 四舍五入为 1.24 正确，且符合缓存容量减小导致命中率下降及偏差增大的物理直觉。
