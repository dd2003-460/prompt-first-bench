# N53: 泊松失效模型中的一致性未命中率具体数值：M_invalidation = 1 - exp(-0.01 * T_resident_days)，其中 T_resid

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

泊松失效模型中的一致性未命中率具体数值：M_invalidation = 1 - exp(-0.01 * T_resident_days)，其中 T_resident_days 为以天为单位的驻留时间。若 T_resident ≈ 0.5 天（示例值，需由 N29 计算确认），则 M_invalidation ≈ 0.005。

## Corrected Claim

泊松失效模型中的一致性未命中率具体数值：M_invalidation = 1 - exp(-0.01 * T_resident_days)，其中 T_resident_days 为以天为单位的驻留时间。若 T_resident ≈ 0.5 天（示例值，需由 N29 计算确认），则 M_invalidation ≈ 0.005。

## Evidence

先验知识/题面给定，逻辑校验通过：泊松分布失效概率公式 P=1-exp(-λt) 在 λ=0.01, t=0.5 时计算结果 1-exp(-0.005)≈0.0049875，四舍五入为 0.005，数值量级与逻辑自洽。
