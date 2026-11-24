# N1276: 标准工作点在 5G 环境（平均带宽 20 Mbps）下的缓冲比 Buffer_Ratio_5G = (s_video_total / B_5G) / T_vid

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N436

## Claim

标准工作点在 5G 环境（平均带宽 20 Mbps）下的缓冲比 Buffer_Ratio_5G = (s_video_total / B_5G) / T_video = (4.0MB / 2.5MB/s) / 15s ≈ 0.107，表示只需缓冲 10.7% 的视频时长即可无缝播放。

## Corrected Claim

标准工作点在 5G 环境（平均带宽 20 Mbps）下的缓冲比 Buffer_Ratio_5G = (s_video_total / B_5G) / T_video = (4.0MB / 2.5MB/s) / 15s ≈ 0.107，表示只需缓冲 10.7% 的视频时长即可无缝播放。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (4.0 / 2.5) / 15 ≈ 0.1067 与陈述一致，量纲与物理直觉合理。
