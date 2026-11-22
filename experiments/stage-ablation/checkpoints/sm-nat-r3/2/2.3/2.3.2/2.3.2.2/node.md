# N156: N53子节点：S_cache 在 N_cache=50,000（半量缓存）典型工作点的数值解，S_cache = F_S^{-1}(0.5)，对于 Pareto

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

N53子节点：S_cache 在 N_cache=50,000（半量缓存）典型工作点的数值解，S_cache = F_S^{-1}(0.5)，对于 Pareto(α=1.1, x_min=1KB)，S_cache = x_min * (1 - 0.5)^{-1/1.1} ≈ 1KB * 2.09 ≈ 2.09KB，量化了缓存对象数减半时截断点大小约翻倍的特征。

## Corrected Claim

N53子节点：S_cache 在 N_cache=50,000（半量缓存）典型工作点的数值解，S_cache = F_S^{-1}(0.5)，对于 Pareto(α=1.1, x_min=1KB)，S_cache = x_min * (1 - 0.5)^{-1/1.1} ≈ 1KB * 2.09 ≈ 2.09KB，量化了缓存对象数减半时截断点大小约翻倍的特征。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布逆CDF公式 S = x_min * (1-p)^(-1/α) 代入 p=0.5, α=1.1 计算得 2.09KB，数学推导正确且量级合理。
