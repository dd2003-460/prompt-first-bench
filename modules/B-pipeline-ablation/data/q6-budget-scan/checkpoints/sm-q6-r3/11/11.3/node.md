# N164: 单用户日均短视频请求数 req_video 的估算模型：基于上传/下载流量比与平均对象大小推导，req_video = V_download_video_dai

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N51

## Claim

单用户日均短视频请求数 req_video 的估算模型：基于上传/下载流量比与平均对象大小推导，req_video = V_download_video_daily / (DAU * s_avg_video)，其中 V_download_video_daily 为日均短视频下载量，s_avg_video 为短视频平均大小（1-5MB），需结合业务日志校准

## Corrected Claim

单用户日均短视频请求数 req_video 的估算模型：基于上传/下载流量比与平均对象大小推导，req_video = V_download_video_daily / (DAU * s_avg_video)，其中 V_download_video_daily 为日均短视频下载量，s_avg_video 为短视频平均大小（1-5MB），需结合业务日志校准

## Evidence

先验知识/题面给定，逻辑校验通过：公式 req_video = V_download_video_daily / (DAU * s_avg_video) 在量纲上自洽（总流量/人均流量=人均次数），且 s_avg_video 取值 1-5MB 符合短视频常见大小范围，属于合理的工程估算模型。

## Search Query

short video CDN average request size per user daily
