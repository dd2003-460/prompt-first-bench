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

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1定义净数据量，节点2定义容器开销及总大小（依赖节点1），节点3和4分别基于总大小计算延迟和成本。虽然节点3和4都依赖于节点2的结果，但它们的计算目标（时间 vs 金钱）和输入参数（带宽 vs 单价）不同，属于正交的子任务，不构成冗余。所有关键方面（大小、延迟、成本）均已覆盖。）
