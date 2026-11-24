# N689: 云对象存储99.99% SLA的物理实现机制解析：确认阿里云OSS是否采用3副本跨AZ（N_replica=3）还是纠删码（EC k=10, m=4, N=14

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N286

## Claim

云对象存储99.99% SLA的物理实现机制解析：确认阿里云OSS是否采用3副本跨AZ（N_replica=3）还是纠删码（EC k=10, m=4, N=14）？若为EC，则电力冗余系数k_power = N_logical / N_physical_effective，需计算实际物理存储放大因子

## Corrected Claim

阿里云OSS提供99.99% SLA，其底层数据持久性通常通过多副本或纠删码（EC）技术实现以跨越可用区，但具体采用3副本还是特定参数的EC（如k=10, m=4）需查阅最新官方技术文档确认，不同时期或区域可能存在差异。

## Evidence

[质询]该陈述包含具体的工程实现细节（如EC参数k=10, m=4或3副本），属于经验事实。由于缺乏官方技术白皮书或权威来源直接证实阿里云OSS当前底层具体采用哪种编码方案及确切参数，无法排除其随时间演进或不同区域配置不同的可能性，存在将特定版本/推测参数当作绝对事实的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体EC参数或副本策略）。

## Search Query

Alibaba Cloud OSS 99.99% SLA physical replica erasure coding architecture
