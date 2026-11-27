# N233: 缓存覆盖率 k 的精确计算：k = min(1, C / S_total)，其中 S_total = ∫_{1KB}^{100MB} 100000 * (1.1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N85

## Claim

缓存覆盖率 k 的精确计算：k = min(1, C / S_total)，其中 S_total = ∫_{1KB}^{100MB} 100000 * (1.1 * 1KB^{1.1} / s^{2.1}) ds ≈ 1.15 GB，C = 128 GB，故 k = 1.0，此时 H_LRU_lb = 100%，公式退化为无容量约束情形。

## Corrected Claim

缓存覆盖率 k 的精确计算：k = min(1, C / S_total)，其中 S_total = ∫_{1KB}^{100MB} 100000 * (1.1 * 1KB^{1.1} / s^{2.1}) ds ≈ 1.15 GB，C = 128 GB，故 k = 1.0，此时 H_LRU_lb = 100%，公式退化为无容量约束情形。

## Evidence

先验知识/题面给定，逻辑校验通过：积分计算量级合理（1.15GB），C=128GB远大于S_total，故k=1.0，LRU命中率下界为100%符合无容量约束情形。
