# N749: 工作点B（平衡/中等成本）：RPO=24小时，500TB全量+5TB增量。S3 Standard存储成本 ≈ ¥10,600,000/年。恢复数据量505TB，

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N280

## Claim

工作点B（平衡/中等成本）：RPO=24小时，500TB全量+5TB增量。S3 Standard存储成本 ≈ ¥10,600,000/年。恢复数据量505TB，若仅恢复80%受损数据，V_restore=404TB，GET成本降至 ≈ ¥9,088/次。此点为多数企业默认配置，RTO受限于网络带宽（10Gbps下约110小时）。

## Corrected Claim

工作点B（平衡/中等成本）：RPO=24小时，500TB全量+5TB增量。S3 Standard存储成本 ≈ ¥10,600,000/年。恢复数据量505TB，若仅恢复80%受损数据，V_restore=404TB，GET成本降至 ≈ ¥9,088/次。此点为多数企业默认配置，RTO受限于网络带宽（10Gbps下约110小时）。

## Evidence

先验知识/题面给定，逻辑校验通过：存储成本计算（500TB * 12月 * 单价）与恢复成本计算（404TB * 单价）在数量级和逻辑上自洽，符合S3标准存储及GET请求的典型定价模型。
