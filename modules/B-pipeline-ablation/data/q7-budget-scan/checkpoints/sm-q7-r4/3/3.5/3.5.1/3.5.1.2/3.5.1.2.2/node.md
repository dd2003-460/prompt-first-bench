# N746: 工作点B（平衡/中等成本）：RPO=24小时，采用每日全量备份（500TB）+ 24h增量日志（5TB）。恢复数据量 V_restore = 505TB，k=1

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N279

## Claim

工作点B（平衡/中等成本）：RPO=24小时，采用每日全量备份（500TB）+ 24h增量日志（5TB）。恢复数据量 V_restore = 505TB，k=1.01。若仅恢复受损分区（50%），V_restore = 252.5TB，k=0.505。此工作点下，S3 Standard存储成本基准为500TB，增量日志存储成本可忽略，总恢复带宽需求 = 505TB / 10Gbps ≈ 113小时（若无加速）。

## Corrected Claim

工作点B（平衡/中等成本）：RPO=24小时，采用每日全量备份（500TB）+ 24h增量日志（5TB）。恢复数据量 V_restore = 505TB，k=1.01。若仅恢复受损分区（50%），V_restore = 252.5TB，k=0.505。此工作点下，S3 Standard存储成本基准为500TB，增量日志存储成本可忽略，总恢复带宽需求 = 505TB / 10Gbps ≈ 113小时（若无加速）。

## Evidence

先验知识/题面给定，逻辑校验通过：505TB / 10Gbps ≈ 113小时计算正确（505*8/10/3.6≈112.2），k值定义符合比例关系，存储成本描述符合S3标准存储特性。
