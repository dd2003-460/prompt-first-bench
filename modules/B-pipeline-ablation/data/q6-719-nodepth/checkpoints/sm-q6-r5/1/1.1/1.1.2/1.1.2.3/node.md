# N142: 高码率工作点：s_video = 8.0 MB，基于 1080p H.265 @ 4 Mbps 码率 + 15s 时长或 4K H.265 @ 8 Mbps，P

- **status**: pending
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

父节点级核验未通过：非正交, 不完备, 有冗余（子节点之间存在逻辑矛盾（带宽成本增量 vs 总成本增加）和重复计算（传输延迟在节点1和5中重复推导），且未覆盖父节点中明确提到的'4K H.265 @ 8 Mbps'这一关键备选工作点。）
