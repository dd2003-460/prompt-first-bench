# N158: 在容量受限（高成本/低准确性）工作点下，假设 E[S]=1MB 导致 K_cap=131072 < 10^5，此时 T_avg ≈ K_cap/λ_total 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N74

## Claim

在容量受限（高成本/低准确性）工作点下，假设 E[S]=1MB 导致 K_cap=131072 < 10^5，此时 T_avg ≈ K_cap/λ_total ≈ 131072 / 578.7 ≈ 226 秒，该值仅反映驱逐周期，未包含对象更新失效，需结合 P_inval 计算有效命中率

## Corrected Claim

在容量受限（高成本/低准确性）工作点下，假设 E[S]=1MB 导致 K_cap=131072 < 10^5，此时 T_avg ≈ K_cap/λ_total ≈ 131072 / 578.7 ≈ 226 秒，该值仅反映驱逐周期，未包含对象更新失效，需结合 P_inval 计算有效命中率

## Evidence

先验知识/题面给定，逻辑校验通过：1MB=131072KB，131072/578.7≈226.5，数值量级与计算逻辑自洽，且明确指出了该指标仅反映驱逐周期而未包含失效概率的局限性，符合缓存理论分析规范。
