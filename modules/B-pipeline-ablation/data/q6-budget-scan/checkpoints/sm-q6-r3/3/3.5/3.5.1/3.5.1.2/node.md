# N328: 自建 IDC 上传带宽成本结构：p_upload_self = p_downlink_self * r_updown，其中 p_downlink_self 为下

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N111

## Claim

自建 IDC 上传带宽成本结构：p_upload_self = p_downlink_self * r_updown，其中 p_downlink_self 为下行带宽单价（¥0.05-0.15/GB），r_updown 为上行/下行价格比（通常 0.3-0.5，因上行带宽资源稀缺但需求低，运营商定价策略不同），故 p_upload_self ≈ ¥0.015-0.075/GB，需结合具体 IDC 合约条款。

## Corrected Claim

自建 IDC 上传带宽成本通常低于下行带宽，具体单价需依据实际 IDC 合约条款确定，一般上行价格约为下行的 30%-50%。

## Evidence

[质询]该陈述包含具体的经验性价格参数（¥0.05-0.15/GB）和比例系数（0.3-0.5），属于市场经验事实而非第一性原理可推导内容，且缺乏来源支持以确认其当前市场准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

IDC data center uplink bandwidth cost ratio to downlink price per GB
