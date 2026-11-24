# N1275: 标准工作点在 4G 环境（平均带宽 10 Mbps）下的缓冲比 Buffer_Ratio_4G = (s_video_total / B_4G) / T_vid

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N436

## Claim

标准工作点在 4G 环境（平均带宽 10 Mbps）下的缓冲比 Buffer_Ratio_4G = (s_video_total / B_4G) / T_video = (4.0MB / 1.25MB/s) / 15s ≈ 0.213，表示只需缓冲 21.3% 的视频时长即可无缝播放。

## Corrected Claim

标准工作点在 4G 环境（平均带宽 10 Mbps）下的缓冲比 Buffer_Ratio_4G = (s_video_total / B_4G) / T_video = (4.0MB / 1.25MB/s) / 15s ≈ 0.213，表示只需缓冲 21.3% 的视频时长即可无缝播放。

## Evidence

先验知识/题面给定，逻辑校验通过：10 Mbps = 1.25 MB/s，4.0 MB / 1.25 MB/s = 3.2 s，3.2 s / 15 s ≈ 0.213，计算无误且符合流媒体缓冲原理。
