# N250: κ 对 Pareto 指数 α 的敏感性：当 α 从 1.1 增至 1.5（分布变轻）时，H_LRU_lower_bound 升至 0.80，H_LRU_act

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N86

## Claim

κ 对 Pareto 指数 α 的敏感性：当 α 从 1.1 增至 1.5（分布变轻）时，H_LRU_lower_bound 升至 0.80，H_LRU_actual 升至 0.85，κ 变为 0.85/0.80 ≈ 1.06，表明重尾程度减弱时下界估计更准确。

## Corrected Claim

κ 对 Pareto 指数 α 的敏感性：当 α 从 1.1 增至 1.5（分布变轻）时，H_LRU_lower_bound 升至 0.80，H_LRU_actual 升至 0.85，κ 变为 0.85/0.80 ≈ 1.06，表明重尾程度减弱时下界估计更准确。

## Evidence

先验知识/题面给定，逻辑校验通过：α增大意味着分布尾部变轻，LRU缓存命中率通常上升，且重尾分布中下界估计往往偏保守（κ>1），随着分布变轻，实际命中率与下界估计的差距缩小，κ趋近于1，符合直觉与逻辑。
