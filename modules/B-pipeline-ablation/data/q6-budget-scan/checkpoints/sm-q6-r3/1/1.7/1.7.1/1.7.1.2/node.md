# N161: 边缘节点内部处理与 IO 延迟 t_processing 的具体数值取决于硬件配置与对象大小，对于 NVMe SSD 读取 1MB 对象，t_processin

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N50

## Claim

边缘节点内部处理与 IO 延迟 t_processing 的具体数值取决于硬件配置与对象大小，对于 NVMe SSD 读取 1MB 对象，t_processing ≈ 1-2ms；对于 HDD 读取 1MB 对象，t_processing ≈ 5-10ms；需根据实际硬件配置确定。

## Corrected Claim

边缘节点内部处理与 IO 延迟 t_processing 的具体数值取决于硬件配置与对象大小，对于 NVMe SSD 读取 1MB 对象，t_processing ≈ 1-2ms；对于 HDD 读取 1MB 对象，t_processing ≈ 5-10ms；需根据实际硬件配置确定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge node internal processing IO latency
