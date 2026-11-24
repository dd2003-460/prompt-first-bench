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

父节点级核验未通过：非正交, 有冗余（子节点4与父节点及子节点1存在逻辑矛盾（带宽成本增量计算不一致，父节点称100%，子节点4称75%且逻辑推导有误）；子节点1和子节点4均涉及带宽成本/传输延迟的计算，存在内容重叠。）
