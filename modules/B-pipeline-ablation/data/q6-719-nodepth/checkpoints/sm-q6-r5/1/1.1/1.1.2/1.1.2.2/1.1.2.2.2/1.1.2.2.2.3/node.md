# N1277: 标准工作点在弱网环境（平均带宽 5 Mbps）下的缓冲比 Buffer_Ratio_weak = (s_video_total / B_weak) / T_vi

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N436

## Claim

标准工作点在弱网环境（平均带宽 5 Mbps）下的缓冲比 Buffer_Ratio_weak = (s_video_total / B_weak) / T_video = (4.0MB / 0.625MB/s) / 15s ≈ 0.427，表示需缓冲 42.7% 的视频时长，可能出现卡顿风险。

## Corrected Claim

标准工作点在弱网环境（平均带宽 5 Mbps）下的缓冲比 Buffer_Ratio_weak = (s_video_total / B_weak) / T_video = (4.0MB / 0.625MB/s) / 15s ≈ 0.427，表示需缓冲 42.7% 的视频时长，可能出现卡顿风险。

## Evidence

先验知识/题面给定，逻辑校验通过：4.0MB / 0.625MB/s = 6.4s，6.4s / 15s ≈ 0.427，计算无误且量级合理。
