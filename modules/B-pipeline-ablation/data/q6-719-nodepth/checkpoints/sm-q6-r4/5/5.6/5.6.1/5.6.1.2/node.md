# N473: 公有云CDN计费口径B（按带宽峰值）下的月峰值带宽 B_peak = B_avg * K_peak = 493.8 Mbps * 4 ≈ 1975.2 Mbps

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N153

## Claim

公有云CDN计费口径B（按带宽峰值）下的月峰值带宽 B_peak = B_avg * K_peak = 493.8 Mbps * 4 ≈ 1975.2 Mbps ≈ 2 Gbps，用于确定带宽包档位。

## Corrected Claim

公有云CDN计费口径B（按带宽峰值）下的月峰值带宽 B_peak = B_avg * K_peak = 493.8 Mbps * 4 ≈ 1975.2 Mbps ≈ 2 Gbps，用于确定带宽包档位。

## Evidence

[质询]K_peak=4 是一个经验估算值，不同业务场景（如视频、下载、API）的峰值/均值比差异较大，可能存在偏差。 | 先验知识/题面给定，逻辑校验通过：493.8 * 4 = 1975.2 Mbps，约等于 2 Gbps，计算无误且量级合理。
