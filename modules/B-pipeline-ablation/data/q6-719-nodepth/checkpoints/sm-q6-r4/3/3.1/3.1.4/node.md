# N69: 单GB存储月成本 C_storage 的类型区分：C_storage = C_ssd_if_hot + C_hdd_if_cold，其中 C_ssd_if_ho

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

单GB存储月成本 C_storage 的类型区分：C_storage = C_ssd_if_hot + C_hdd_if_cold，其中 C_ssd_if_hot 为SSD成本（¥0.5-1.0/GB/月，因边缘节点需高IOPS和低延迟，通常使用NVMe SSD），C_hdd_if_cold 为HDD成本（¥0.1-0.2/GB/月，仅用于非实时回源缓存或日志存储）；鉴于边缘节点对延迟敏感，主要成本由SSD主导，取 C_storage ≈ ¥0.8/GB/月 作为基准。

## Corrected Claim

单GB存储月成本 C_storage 的类型区分：C_storage = C_ssd_if_hot + C_hdd_if_cold，其中 C_ssd_if_hot 为SSD成本（¥0.5-1.0/GB/月，因边缘节点需高IOPS和低延迟，通常使用NVMe SSD），C_hdd_if_cold 为HDD成本（¥0.1-0.2/GB/月，仅用于非实时回源缓存或日志存储）；鉴于边缘节点对延迟敏感，主要成本由SSD主导，取 C_storage ≈ ¥0.8/GB/月 作为基准。

## Evidence

父节点级核验未通过：有冗余（子节点实质上是同一参数（存储介质配比/单位成本）的两个不同取值（100% SSD vs 80/20 混合），属于典型的参数化冗余，而非正交的功能维度分解；同时父节点定义的基准值（¥0.8）未在子节点中明确体现或作为第三个工作点，导致覆盖略有偏差。）
