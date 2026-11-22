# N189: 折扣因子 D 在 T_evict >> T_update 极限下的值：当 T_evict/T_update → ∞（即缓存极小，驱逐极快），D → 1 - 0.

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

折扣因子 D 在 T_evict >> T_update 极限下的值：当 T_evict/T_update → ∞（即缓存极小，驱逐极快），D → 1 - 0.99 * 1 / (1+0) = 0.01，意味着命中率几乎归零，验证公式在极端低容量下的合理性。

## Corrected Claim

折扣因子 D 在 T_evict >> T_update 极限下的值：当 T_evict/T_update → ∞（即缓存极小，驱逐极快），D → 1 - 0.99 * 1 / (1+0) = 0.01，意味着命中率几乎归零，验证公式在极端低容量下的合理性。

## Evidence

先验知识/题面给定，逻辑校验通过：当 T_evict/T_update → ∞ 时，比值项 1/(1+T_evict/T_update) 趋近于 0，代入公式 D = 1 - 0.99 * (1/(1+0)) 计算得 0.01，数学推导自洽且符合极端低容量下命中率趋近于零的物理直觉。
