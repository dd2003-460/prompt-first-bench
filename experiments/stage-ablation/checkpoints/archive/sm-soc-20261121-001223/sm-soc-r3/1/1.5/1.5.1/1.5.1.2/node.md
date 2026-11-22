# N120: 时间窗口对 k_consult_base 的影响：定义 k_consult_base 为每小时咨询概率。若买家平均浏览停留时间为 10 分钟，则单次曝光的咨询概

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

时间窗口对 k_consult_base 的影响：定义 k_consult_base 为每小时咨询概率。若买家平均浏览停留时间为 10 分钟，则单次曝光的咨询概率 P_consult = k_consult_base * (10/60)。对于 k_consult_base=0.1，单次曝光咨询率仅为 1.67%。

## Corrected Claim

时间窗口对 k_consult_base 的影响：定义 k_consult_base 为每小时咨询概率。若买家平均浏览停留时间为 10 分钟，则单次曝光的咨询概率 P_consult = k_consult_base * (10/60)。对于 k_consult_base=0.1，单次曝光咨询率仅为 1.67%。

## Evidence

先验知识/题面给定，逻辑校验通过：0.1 * (10/60) = 0.01666... ≈ 1.67%，计算无误且量纲一致。
