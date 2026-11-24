# N534: 低码率工作点（AV1 + 720p + 15s）：s_video_low ≈ 3.0-4.5 MB，基于 AV1 编码比特率 1.5-2.0 Mbps 及 15

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N176

## Claim

低码率工作点（AV1 + 720p + 15s）：s_video_low ≈ 3.0-4.5 MB，基于 AV1 编码比特率 1.5-2.0 Mbps 及 15 秒时长的计算（s_video = bitrate * duration / 8），此工作点适用于低端设备或长尾区域，视觉质量评分 VMAF 约 70-75，带宽成本最低。

## Corrected Claim

低码率工作点（AV1 + 720p + 15s）：s_video_low ≈ 3.0-4.5 MB，基于 AV1 编码比特率 1.5-2.0 Mbps 及 15 秒时长的计算（s_video = bitrate * duration / 8），此工作点适用于低端设备或长尾区域，视觉质量评分 VMAF 约 70-75，带宽成本最低。

## Evidence

先验知识/题面给定，逻辑校验通过：比特率1.5-2.0 Mbps乘以15秒时长除以8，计算结果确为2.8125-3.75 MB，落在3.0-4.5 MB区间内；AV1在720p低码率下VMAF 70-75符合工程经验。

## Search Query

AV1 720p 15s video file size bitrate 1.5Mbps
