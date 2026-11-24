# N684: 自建IDC等效电力成本上浮系数公式推导：C_uplift = (PUE_self / PUE_cloud - 1) × (C_elec_share_in_clo

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N284

## Claim

自建IDC等效电力成本上浮系数公式推导：C_uplift = (PUE_self / PUE_cloud - 1) × (C_elec_share_in_cloud_price / C_total_cloud_price)，其中C_elec_share_in_cloud_price需从N288的0.5%基础修正，若电力占比极低，则36%的上浮估算可能严重高估，需重新计算实际等效单价差异

## Corrected Claim

自建IDC等效电力成本上浮系数公式推导：C_uplift = (PUE_self / PUE_cloud - 1) × (C_elec_share_in_cloud_price / C_total_cloud_price)，其中C_elec_share_in_cloud_price需从N288的0.5%基础修正，若电力占比极低，则36%的上浮估算可能严重高估，需重新计算实际等效单价差异

## Evidence

先验知识/题面给定，逻辑校验通过
