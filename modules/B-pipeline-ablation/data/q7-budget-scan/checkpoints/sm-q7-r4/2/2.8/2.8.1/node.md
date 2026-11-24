# N84: S3 Standard 年存储费 = 500 TB * 1024 GB/TB * $0.023/GB/月 * 12 月 * 7.2 ¥/$ = ¥108,595

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

S3 Standard 年存储费 = 500 TB * 1024 GB/TB * $0.023/GB/月 * 12 月 * 7.2 ¥/$ = ¥108,595/年

## Corrected Claim

S3 Standard 年存储费 = 500 TB * 1024 GB/TB * $0.023/GB/月 * 12 月 * 7.2 ¥/$ = ¥108,595/年

## Evidence

父节点级核验未通过：非正交, 不完备（子节点之间存在逻辑包含关系导致非正交：第三个子节点（冷数据分层优化）实际上是对第一个子节点（存储费计算基础）的替代方案而非独立维度，两者在最终成本汇总时会发生冲突（是选A还是选B，不能同时计入）。此外，完备性不足：忽略了数据上传/下载流量费（Data Transfer Out），这是S3成本的重要组成部分，且通常比请求费更显著。）
