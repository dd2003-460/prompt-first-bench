# N324: 短期置信度阈值判定：若观察到的 δc_48h < 0.1 * c_0（即咨询率提升小于10%），且 δcvr_48h < 0.05 * cvr_0，则 C_pr

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110, N112, N113

## Claim

短期置信度阈值判定：若观察到的 δc_48h < 0.1 * c_0（即咨询率提升小于10%），且 δcvr_48h < 0.05 * cvr_0，则 C_profit,short < 0.3，判定逐利假设在短期不成立；若 δc_48h > 0.3 * c_0，则 C_profit,short > 0.7，判定逐利假设主导。

## Corrected Claim

短期置信度阈值判定：若观察到的 δc_48h < 0.1 * c_0（即咨询率提升小于10%），且 δcvr_48h < 0.05 * cvr_0，则 C_profit,short < 0.3，判定逐利假设在短期不成立；若 δc_48h > 0.3 * c_0，则 C_profit,short > 0.7，判定逐利假设主导。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

threshold criteria seller profit motivation short term operational scale
