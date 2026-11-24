# N1266: 低码率工作点（720p H.265 @ 1 Mbps, 15s）的精确文件体积 s_video_low = (1 Mbps / 8) * 15 s = 1.87

- **status**: verified
- **level**: L6
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N434

## Claim

低码率工作点（720p H.265 @ 1 Mbps, 15s）的精确文件体积 s_video_low = (1 Mbps / 8) * 15 s = 1.875 MB，加上容器开销约 0.15 MB，总计 2.025 MB，作为低码率基准参考。

## Corrected Claim

低码率工作点（720p H.265 @ 1 Mbps, 15s）的精确文件体积 s_video_low = (1 Mbps / 8) * 15 s = 1.875 MB，加上容器开销约 0.15 MB，总计 2.025 MB，作为低码率基准参考。

## Evidence

先验知识/题面给定，逻辑校验通过：1 Mbps 带宽下 15 秒数据量为 1.875 MB，加上约 0.15 MB 容器开销，总计 2.025 MB，计算准确且符合工程常识。
