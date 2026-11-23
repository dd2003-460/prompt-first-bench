# N80: 预热对 P99 延迟的改善：ΔP99_warm = P99_base - P99_warm ≈ p_miss_base * t_origin * (1 - e^

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

预热对 P99 延迟的改善：ΔP99_warm = P99_base - P99_warm ≈ p_miss_base * t_origin * (1 - e^(-K/N_unique_hot))，其中 K 为预热对象数

## Corrected Claim

预热对 P99 延迟的改善：ΔP99_warm = P99_base - P99_warm ≈ p_miss_base * t_origin * (1 - e^(-K/N_unique_hot))，其中 K 为预热对象数

## Evidence

父节点级核验未通过：不完备（子节点正交性良好，分别探讨了优化方向（K的关系）、适用边界（H_base阈值）和模型假设（分布验证）。但完备性不足，父节点公式中包含变量 N_unique_hot（热对象唯一数量），其变化对 P99 改善的影响（如缓存碎片化或工作集大小变化）未被单独作为子节点覆盖，仅隐含在子节点1的分母中，缺乏对其独立性的分析。）
