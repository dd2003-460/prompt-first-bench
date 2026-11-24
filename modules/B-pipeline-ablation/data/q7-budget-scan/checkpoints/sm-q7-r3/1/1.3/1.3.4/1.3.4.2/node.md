# N143: 工作点B（单AZ/低成本）：采用S3标准存储-单AZ（若可用），冗余开销率约0%，有效容量 = 500TB，每TB有效成本最低，但可用性SLA从99.99%降至

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N38

## Claim

工作点B（单AZ/低成本）：采用S3标准存储-单AZ（若可用），冗余开销率约0%，有效容量 = 500TB，每TB有效成本最低，但可用性SLA从99.99%降至99.9%，故障恢复时间RTO增加，需权衡RTO代价。

## Corrected Claim

工作点B（单AZ/低成本）：采用S3标准存储-单AZ（若可用），冗余开销率约0%，有效容量 = 500TB，每TB有效成本最低，但可用性SLA从99.99%降至99.9%，故障恢复时间RTO增加，需权衡RTO代价。

## Evidence

先验知识/题面给定，逻辑校验通过：S3 One Zone-IA 或单AZ存储确实具有更低的冗余开销（接近0%）和更低的单位成本，但牺牲了多AZ的高可用性（SLA从99.99%降至99.9%左右），符合云存储基本架构原理。
