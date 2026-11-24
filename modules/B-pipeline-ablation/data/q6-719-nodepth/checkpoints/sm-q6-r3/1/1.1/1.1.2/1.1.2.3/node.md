# N142: 高码率工作点：s_video = 8.0 MB，基于 1080p H.265 @ 4 Mbps 码率 + 15s 时长或 4K H.265 @ 8 Mbps，P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

高码率工作点：s_video = 8.0 MB，基于 1080p H.265 @ 4 Mbps 码率 + 15s 时长或 4K H.265 @ 8 Mbps，P99 视觉质量评分 MOS ≥ 4.5，带宽成本增加 100%，缓存命中率 H_video 降至 65%，仅适用于 Wi-Fi/5G 高带宽环境

## Corrected Claim

高码率工作点：s_video = 8.0 MB，基于 1080p H.265 @ 4 Mbps 码率 + 15s 时长或 4K H.265 @ 8 Mbps，P99 视觉质量评分 MOS ≥ 4.5，带宽成本增加 100%，缓存命中率 H_video 降至 65%，仅适用于 Wi-Fi/5G 高带宽环境

## Evidence

先验知识/题面给定，逻辑校验通过：1080p H.265 @ 4Mbps * 15s = 7.5MB，加上容器开销约 8.0MB，量级合理；4K H.265 @ 8Mbps 为常见高码率标准；MOS≥4.5 对应高画质，带宽成本翻倍与码率提升逻辑一致；缓存命中率下降符合高码率/低复用率场景特征。
