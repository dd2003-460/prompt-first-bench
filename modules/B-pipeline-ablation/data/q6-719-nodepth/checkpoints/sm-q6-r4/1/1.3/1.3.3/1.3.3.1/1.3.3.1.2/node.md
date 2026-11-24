# N500: 短视频类对象（占比 10%）的平均大小 s_video 高度依赖编码码率与时长，假设平均时长 15s、码率 2Mbps，则 s_video_avg = 2Mbp

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N168

## Claim

短视频类对象（占比 10%）的平均大小 s_video 高度依赖编码码率与时长，假设平均时长 15s、码率 2Mbps，则 s_video_avg = 2Mbps × 15s / 8 ≈ 3.75MB，而非 10MB 的粗略估计

## Corrected Claim

短视频类对象（占比 10%）的平均大小 s_video 高度依赖编码码率与时长，假设平均时长 15s、码率 2Mbps，则 s_video_avg = 2Mbps × 15s / 8 ≈ 3.75MB，而非 10MB 的粗略估计

## Evidence

先验知识/题面给定，逻辑校验通过：2Mbps × 15s / 8 = 3.75MB，计算无误且符合物理直觉

## Search Query

short video average file size bitrate duration calculation 2Mbps 15s
