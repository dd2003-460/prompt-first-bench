# N435: 标准工作点（1080p H.265 @ 2 Mbps, 15s）的精确文件体积 s_video = (2 Mbps / 8) * 15 s = 3.75 MB，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N141

## Claim

标准工作点（1080p H.265 @ 2 Mbps, 15s）的精确文件体积 s_video = (2 Mbps / 8) * 15 s = 3.75 MB，加上容器开销约 0.25 MB，总计 4.0 MB；该值作为基准参考，用于计算传输延迟 L_transmission = 4.0MB / B_link 和带宽成本 C_bw = 4.0MB * P_bw。

## Corrected Claim

标准工作点（1080p H.265 @ 2 Mbps, 15s）的精确文件体积 s_video = (2 Mbps / 8) * 15 s = 3.75 MB，加上容器开销约 0.25 MB，总计 4.0 MB；该值作为基准参考，用于计算传输延迟 L_transmission = 4.0MB / B_link 和带宽成本 C_bw = 4.0MB * P_bw。

## Evidence

先验知识/题面给定，逻辑校验通过：2Mbps/8=0.25MB/s，0.25*15=3.75MB，3.75+0.25=4.0MB，计算无误且符合工程常识。
