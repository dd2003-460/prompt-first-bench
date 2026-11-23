# N232: 衰减系数k_decay的标定：k_decay反映缓存替换算法效率与对象大小方差的影响。对于LRU算法，k_decay≈1.0；对于LFU或加权算法，k_deca

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

衰减系数k_decay的标定：k_decay反映缓存替换算法效率与对象大小方差的影响。对于LRU算法，k_decay≈1.0；对于LFU或加权算法，k_decay可降至0.5-0.8。若k_decay=1.0且C_match=0.5，则H_actual = H_ideal * (1 - e^-0.5) ≈ H_ideal * 0.39，命中率损失显著；若k_decay=0.5，H_actual ≈ H_ideal * 0.22。

## Corrected Claim

衰减系数k_decay的标定：k_decay反映缓存替换算法效率与对象大小方差的影响。对于LRU算法，k_decay≈1.0；对于LFU或加权算法，k_decay可降至0.5-0.8。若k_decay=1.0且C_match=0.5，则H_actual = H_ideal * (1 - e^-0.5) ≈ H_ideal * 0.39，命中率损失显著；若k_decay=0.5，H_actual ≈ H_ideal * 0.22。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算正确（1-e^-0.5≈0.393, 1-e^-0.25≈0.221），且符合缓存理论中LRU通常优于LFU/加权算法导致衰减系数更小的直觉。
