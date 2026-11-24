# N277: 峰值系数 Peak_Factor 的确定：基于业务流量曲线，Peak_Factor = Max_Hourly_Bandwidth / Avg_Hourly_Ba

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N82

## Claim

峰值系数 Peak_Factor 的确定：基于业务流量曲线，Peak_Factor = Max_Hourly_Bandwidth / Avg_Hourly_Bandwidth。对于视频平台，早晚高峰流量集中度较高，Peak_Factor 典型值为 2.0-3.0，若未进行流量平滑处理，取保守值 3.0。

## Corrected Claim

峰值系数 Peak_Factor 的确定：基于业务流量曲线，Peak_Factor = Max_Hourly_Bandwidth / Avg_Hourly_Bandwidth。对于视频平台，早晚高峰流量集中度较高，Peak_Factor 典型值为 2.0-3.0，若未进行流量平滑处理，取保守值 3.0。

## Evidence

先验知识/题面给定，逻辑校验通过：峰值系数定义为最大小时带宽与平均小时带宽之比，视频平台早晚高峰集中导致该比值在2.0-3.0区间符合工程经验，取3.0作为保守值逻辑自洽。

## Search Query

CDN bandwidth peak factor calculation video streaming
