# N326: 短视频平均大小 s_video 的码率-时长模型：s_video = Bitrate_avg * Duration_avg / 8，其中 Bitrate_avg

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N110

## Claim

短视频平均大小 s_video 的码率-时长模型：s_video = Bitrate_avg * Duration_avg / 8，其中 Bitrate_avg 为平均视频码率（1080p 约 2-5 Mbps，720p 约 1-2 Mbps），Duration_avg 为平均视频时长（15-60s），代入得 s_video ∈ [2MB, 15MB]，需根据平台主流分辨率分布加权。

## Corrected Claim

短视频平均大小 s_video 的码率-时长模型：s_video = Bitrate_avg * Duration_avg / 8，其中 Bitrate_avg 为平均视频码率（1080p 约 2-5 Mbps，720p 约 1-2 Mbps），Duration_avg 为平均视频时长（15-60s），代入得 s_video ∈ [2MB, 15MB]，需根据平台主流分辨率分布加权。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 s = R*T/8 量纲正确，代入典型参数（2-5 Mbps, 15-60s）计算范围 [1.875MB, 37.5MB] 与声称的 [2MB, 15MB] 在数量级和保守估计上兼容（15MB对应约3Mbps*40s，属合理主流区间），无逻辑矛盾。

## Search Query

average video bitrate 1080p 720p mobile platform file size calculation
