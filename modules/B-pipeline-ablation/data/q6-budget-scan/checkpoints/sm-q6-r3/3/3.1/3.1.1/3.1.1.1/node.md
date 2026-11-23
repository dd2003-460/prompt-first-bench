# N193: 工作点 A（高并发低成本）：采用高内存低 CPU 服务器（如 64GB RAM / 8 vCPU），单服务器并发能力 $C_{srv} \approx 15,0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

工作点 A（高并发低成本）：采用高内存低 CPU 服务器（如 64GB RAM / 8 vCPU），单服务器并发能力 $C_{srv} \approx 15,000$，在 $C_{peak}=50,000$ 时 $N_{servers}=4$，单服务器成本约 8,000 元/月，总成本 32,000 元/月。

## Corrected Claim

工作点 A（高并发低成本）：采用高内存低 CPU 服务器（如 64GB RAM / 8 vCPU），单服务器并发能力 $C_{srv} \approx 15,000$，在 $C_{peak}=50,000$ 时 $N_{servers}=4$，单服务器成本约 8,000 元/月，总成本 32,000 元/月。

## Evidence

先验知识/题面给定，逻辑校验通过：4台服务器 * 15,000并发/台 = 60,000 > 50,000峰值需求，满足容量要求；4 * 8,000元 = 32,000元，成本计算无误。
