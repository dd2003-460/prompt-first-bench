# N36: 有效命中率折损的精确公式：H_effective = H_steady * (1 - p_invalid * f_refill * hit_prob_updat

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N11

## Claim

有效命中率折损的精确公式：H_effective = H_steady * (1 - p_invalid * f_refill * hit_prob_update)，其中 hit_prob_update ≈ 0.975，p_invalid = 0.01，f_refill ≈ 0.0021，折损 ≈ 0.01 * 0.0021 * 0.975 ≈ 0.0000205

## Corrected Claim

有效命中率折损的精确公式：H_effective = H_steady * (1 - p_invalid * f_refill * hit_prob_update)，其中 hit_prob_update ≈ 0.975，p_invalid = 0.01，f_refill ≈ 0.0021，折损 ≈ 0.01 * 0.0021 * 0.975 ≈ 0.0000205

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合缓存命中率折损的线性近似逻辑，数值计算 0.01 * 0.0021 * 0.975 = 0.000020475 ≈ 0.0000205 准确无误，量级合理。

## Search Query

cache hit rate decay update invalidation refill failure probability formula
