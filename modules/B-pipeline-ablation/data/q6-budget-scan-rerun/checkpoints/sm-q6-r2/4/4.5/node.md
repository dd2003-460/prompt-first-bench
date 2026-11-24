# N21: 全自建策略的弹性伸缩系数：弹性系数 E_self = (C_total_self - B_avg) / B_avg，自建节点的弹性伸缩依赖预置冗余容量，响应时间

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

全自建策略的弹性伸缩系数：弹性系数 E_self = (C_total_self - B_avg) / B_avg，自建节点的弹性伸缩依赖预置冗余容量，响应时间 T_scale_self 为小时级至天级（需手动扩容或自动化脚本触发），弹性成本体现为闲置容量成本 C_idle = (C_total_self - B_avg) × unit_cost_per_Mbps_month / 1000，需量化为每千请求的摊销成本。

## Corrected Claim

全自建策略的弹性伸缩系数：弹性系数 E_self = (C_total_self - B_avg) / B_avg，自建节点的弹性伸缩依赖预置冗余容量，响应时间 T_scale_self 为小时级至天级（需手动扩容或自动化脚本触发），弹性成本体现为闲置容量成本 C_idle = (C_total_self - B_avg) × unit_cost_per_Mbps_month / 1000，需量化为每千请求的摊销成本。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

self-hosted CDN elastic scaling manual provisioning idle capacity cost amortization per request
