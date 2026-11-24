# N68: 工作点A（RTO=4h, 本地NVMe）：故障卷重建时间 T_rebuild = 50TB / 100GB/h = 500h >> 4h，超出SLA时长 Δt 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

工作点A（RTO=4h, 本地NVMe）：故障卷重建时间 T_rebuild = 50TB / 100GB/h = 500h >> 4h，超出SLA时长 Δt = 496h，RTO代价 C_rto = 496h × ¥5000/h = ¥2,480,000；需依赖快照/备份实现快速恢复而非在线重建

## Corrected Claim

工作点A（RTO=4h, 本地NVMe）：故障卷重建时间 T_rebuild = 50TB / 100GB/h = 500h >> 4h，超出SLA时长 Δt = 496h，RTO代价 C_rto = 496h × ¥5000/h = ¥2,480,000；需依赖快照/备份实现快速恢复而非在线重建

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（50000GB/100GB/h=500h, 500-4=496h, 496*5000=2,480,000），量纲一致，结论符合存储恢复逻辑。
