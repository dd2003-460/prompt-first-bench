# N535: 中码率工作点（H.265 + 1080p + 30s）：s_video_mid ≈ 7.5-11.25 MB，基于 H.265 编码比特率 2.0-3.0 Mb

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N176

## Claim

中码率工作点（H.265 + 1080p + 30s）：s_video_mid ≈ 7.5-11.25 MB，基于 H.265 编码比特率 2.0-3.0 Mbps 及 30 秒时长的计算，此工作点为当前短视频平台主流默认设置，视觉质量 VMAF 约 85-90，带宽成本为低码率点的 2-3 倍。

## Corrected Claim

中码率工作点（H.265 + 1080p + 30s）：s_video_mid ≈ 7.5-11.25 MB，基于 H.265 编码比特率 2.0-3.0 Mbps 及 30 秒时长的计算，此工作点为当前短视频平台主流默认设置，视觉质量 VMAF 约 85-90，带宽成本为低码率点的 2-3 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：2.0-3.0 Mbps * 30s / 8 = 7.5-11.25 MB，计算无误；H.265 1080p 30fps 在 2-3 Mbps 下 VMAF 85-90 符合工程经验；中码率带宽成本约为低码率（通常 1-1.5 Mbps）的 2-3 倍，逻辑自洽。

## Search Query

H.265 1080p 30s video file size bitrate 2-3Mbps
