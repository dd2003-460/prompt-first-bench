# N20: 冷数据访问频率约束：80%冷数据极少访问，本地NVMe SSD和HDD+SSD分层均满足，云存储低频/归档层满足，无方案被排除

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

冷数据访问频率约束：80%冷数据极少访问，本地NVMe SSD和HDD+SSD分层均满足，云存储低频/归档层满足，无方案被排除

## Corrected Claim

冷数据访问频率约束：80%冷数据极少访问，本地NVMe SSD和HDD+SSD分层均满足，云存储低频/归档层满足，无方案被排除

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别从数据特征定义、本地高性能存储（NVMe）、本地分层存储（HDD）和云存储四个维度进行约束验证，覆盖了父节点提到的所有存储方案，且各维度关注点不同（IOPS vs 带宽 vs 延迟/费用），无逻辑冲突或重复。）
