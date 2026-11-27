# N114: CTR_drop 的时间窗口敏感性分析：对比48小时、72小时、7天三个窗口的 CTR 值，若 $|CTR_{48h} - CTR_{72h}| / CTR_{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N45

## Claim

CTR_drop 的时间窗口敏感性分析：对比48小时、72小时、7天三个窗口的 CTR 值，若 $|CTR_{48h} - CTR_{72h}| / CTR_{48h} > 10\%$，则说明48小时窗口存在'降价冲击'噪声，需采用7天窗口作为基线以反映稳态咨询率。

## Corrected Claim

CTR_drop 的时间窗口敏感性分析：对比48小时、72小时、7天三个窗口的 CTR 值，若 $|CTR_{48h} - CTR_{72h}| / CTR_{48h} > 10\%$，则说明48小时窗口存在'降价冲击'噪声，需采用7天窗口作为基线以反映稳态咨询率。

## Evidence

先验知识/题面给定，逻辑校验通过
