# N68: 工作点A（RTO=4h, 本地NVMe）：故障卷重建时间 T_rebuild = 50TB / 100GB/h = 500h >> 4h，超出SLA时长 Δt 

- **status**: pending
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

父节点级核验未通过：非正交（子节点2（快照/备份恢复）和子节点3（合规性差距/热备）存在逻辑重叠。子节点3中提到的'热备策略'本质上是一种特殊的'快速恢复路径'，其核心成本（硬件CapEx）与子节点2中的'额外CapEx购买备份存储'属于同一维度的资本支出，且两者都在解决'RTO不足'的问题。此外，子节点1讨论的是'在线重建'的干扰，而子节点2和3讨论的是'非在线重建'的替代方案，分类标准不统一（一个是机制内部代价，一个是替代方案代价），导致正交性受损。）
