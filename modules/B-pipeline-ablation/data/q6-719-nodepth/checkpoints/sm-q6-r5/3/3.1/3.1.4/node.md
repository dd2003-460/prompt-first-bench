# N69: 单GB存储月成本 C_storage 的类型区分：C_storage = C_ssd_if_hot + C_hdd_if_cold，其中 C_ssd_if_ho

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点分别描述了高性能（全SSD）和成本敏感（混合存储）两个不同的工作点，彼此互斥且无重叠（正交）。父节点的核心逻辑是成本随存储介质类型变化，子节点覆盖了从纯高性能到混合成本优化的主要场景，符合完备性要求。虽然子节点在结构上相似（都是特定配置下的成本计算），但它们代表的是不同的工程权衡（Trade-off）而非单纯的参数取值重复，因此不构成冗余。）
