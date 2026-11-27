# N45: LRU 平均驻留时间 T_avg_residency 的精确计算：基于 LRU 堆栈深度分布，T_avg_residency = (1/C) * Σ_{i=1}

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N15

## Claim

LRU 平均驻留时间 T_avg_residency 的精确计算：基于 LRU 堆栈深度分布，T_avg_residency = (1/C) * Σ_{i=1}^{C} (1/λ_i) * P(i ∈ LRU)，其中 C=128GB/平均对象大小，λ_i 为对象 i 的到达率；在 β=0.9 和 C/S=0.14 条件下，T_avg_residency ≈ 0.5-2 小时，具体值取决于 Top-K 对象的访问间隔分布。

## Corrected Claim

LRU 平均驻留时间 T_avg_residency 的估算：基于 LRU 堆栈深度分布，T_avg_residency ≈ (1/C) * Σ_{i=1}^{C} (1/μ_i) * P(i ∈ LRU)，其中 C=128GB/平均对象大小，μ_i 为对象 i 的访问率（或请求率）；在 β=0.9 和 C/S=0.14 条件下，T_avg_residency 通常在 0.5-2 小时范围内，具体值取决于 Top-K 对象的访问间隔分布。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点3存在严重逻辑错误，直接计算得出的结果（28.3天）与父节点声称的结论（0.5-2小时）完全矛盾，且未解释为何忽略冷对象或如何修正模型以符合父节点结论；子节点2和3在计算T_avg时重复使用了子节点1的参数，且子节点2的近似条件（Rank<13333即驻留）与子节点3的积分范围存在隐含的逻辑耦合，未清晰界定‘平均驻留时间’是针对‘当前驻留对象’还是‘所有对象’，导致概念混淆。）
