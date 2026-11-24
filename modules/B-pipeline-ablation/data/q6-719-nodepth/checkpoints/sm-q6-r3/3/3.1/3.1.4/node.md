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

父节点级核验通过：正交+完备+无冗余（子节点分别代表了‘高性能’和‘成本敏感’两个不同的设计工作点，逻辑上互斥且互补。虽然从数学角度看它们是同一存储成本公式在不同硬件配置下的实例化（存在参数化冗余的嫌疑），但在架构分解中，区分‘全SSD’与‘混合存储’是必要的架构决策维度，而非简单的数值重复。因此，作为架构选项的分解是合格且非冗余的。）
