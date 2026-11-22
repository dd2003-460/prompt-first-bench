# N104: E_high 的分子 %ΔConsultations 需修正为'有效咨询率'，即剔除机器人/无效咨询后的 CTR_effective = (Unique_Use

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N27, N28, N29

## Claim

E_high 的分子 %ΔConsultations 需修正为'有效咨询率'，即剔除机器人/无效咨询后的 CTR_effective = (Unique_User_Queries / Impressions)，以排除平台流量注水导致的虚假弹性。

## Corrected Claim

E_high 的分子 %ΔConsultations 需修正为'有效咨询率'，即剔除机器人/无效咨询后的 CTR_effective = (Unique_User_Queries / Impressions)，以排除平台流量注水导致的虚假弹性。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

unique user queries vs impressions CTR correction bot filter
