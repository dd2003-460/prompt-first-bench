# N1289: 高码率视频（1080p, 4Mbps）在 4G 低带宽（5Mbps）下的缓冲比 Buffer_Ratio_4G = 8.0MB / (5Mbps * 2s) =

- **status**: degraded
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N440

## Claim

高码率视频（1080p, 4Mbps）在 4G 低带宽（5Mbps）下的缓冲比 Buffer_Ratio_4G = 8.0MB / (5Mbps * 2s) = 8.0，远高于 1.0，表明在 4G 环境下完全不可行，必须依赖边缘缓存命中或预加载机制。

## Corrected Claim

高码率视频（1080p, 4Mbps）在 4G 低带宽（5Mbps）下，若需缓冲 8.0MB 数据，所需时间为 16s（8MB / 0.5MB/s），远超 2s 的缓冲窗口，缓冲比（需求/供给）为 8.0，表明在 4G 环境下实时流媒体体验极差，必须依赖边缘缓存命中或预加载机制。

## Evidence

[质询]数值计算存在量纲错误：8.0MB / (5Mbps * 2s) 的结果应为 0.32（即 8MB / 10MB），而非 8.0。此外，'完全不可行'的结论过于绝对，虽然缓冲比小于1意味着无法持续播放，但通常仍可通过预加载少量数据实现短暂播放，而非绝对不可行。 | 先验知识/题面给定，逻辑校验发现数值计算错误（8MB/10Mbps/2s = 0.32，非8.0），且结论表述过于绝对。
