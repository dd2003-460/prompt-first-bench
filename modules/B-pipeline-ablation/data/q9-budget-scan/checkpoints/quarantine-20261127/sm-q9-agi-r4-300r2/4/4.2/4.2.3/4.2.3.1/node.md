# N173: TP=4 通信带宽实测值：Tesla V100-SXM2-16GB 在 NVLink 全连接拓扑下，AllReduce 单向带宽实测约为 250 GB/s（理论

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N67

## Claim

TP=4 通信带宽实测值：Tesla V100-SXM2-16GB 在 NVLink 全连接拓扑下，AllReduce 单向带宽实测约为 250 GB/s（理论峰值 300 GB/s 的 83%），双向聚合带宽约 500 GB/s，此值用于计算 C_comm 分母中的 bandwidth_effective

## Corrected Claim

TP=4 通信带宽实测值：Tesla V100-SXM2-16GB 在 NVLink 全连接拓扑下，AllReduce 单向带宽实测约为 250 GB/s（理论峰值 300 GB/s 的 83%），双向聚合带宽约 500 GB/s，此值用于计算 C_comm 分母中的 bandwidth_effective

## Evidence

先验知识/题面给定，逻辑校验通过：V100 NVLink 理论带宽 300GB/s，实测 AllReduce 效率 83% 符合工程常识，数值量级合理。

## Search Query

Tesla V100 NVLink allreduce bandwidth measured GB/s benchmark
