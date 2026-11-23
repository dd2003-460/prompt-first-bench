# N155: 源站存储读取延迟 t_read 的具体数值取决于存储介质类型与对象大小，对于 NVMe SSD 读取 1MB 对象，t_read ≈ 0.1-0.5ms；对于 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N48

## Claim

源站存储读取延迟 t_read 的具体数值取决于存储介质类型与对象大小，对于 NVMe SSD 读取 1MB 对象，t_read ≈ 0.1-0.5ms；对于 HDD，t_read ≈ 5-15ms；需根据源站实际存储配置确定。

## Corrected Claim

源站存储读取延迟 t_read 的具体数值取决于存储介质类型与对象大小，对于 NVMe SSD 读取 1MB 对象，t_read ≈ 0.1-0.5ms；对于 HDD，t_read ≈ 5-15ms；需根据源站实际存储配置确定。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe SSD read latency 1MB object
