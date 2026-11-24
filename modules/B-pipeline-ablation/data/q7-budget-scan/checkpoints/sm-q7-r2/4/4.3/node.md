# N21: 云对象存储（S3/OSS）无本地重建概念，RTO 定义为数据可用性恢复时间；标准存储 RTO≈0（高可用），但跨区域复制场景 RTO = T_replicati

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

云对象存储（S3/OSS）无本地重建概念，RTO 定义为数据可用性恢复时间；标准存储 RTO≈0（高可用），但跨区域复制场景 RTO = T_replication_lag + T_failover，典型值为 5-30 分钟 [待核验]；若发生区域灾难，需从备份桶恢复，T_RTO_Cloud = T_cross_region_copy(500TB) ≈ 500TB/10Gbps ≈ 417 小时（带宽受限） [knowledge]

## Corrected Claim

云对象存储无本地重建概念，RTO定义为数据可用性恢复时间；标准存储高可用RTO接近0，跨区域复制RTO取决于复制延迟和故障切换时间；区域灾难恢复耗时取决于跨区带宽和数据量，例如500TB数据在10Gbps理想带宽下理论传输时间约为114小时，实际受限于网络拥塞和并发度可能更长。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点完全偏离了父节点的核心主题。父节点明确讨论的是‘云对象存储（S3/OSS）’的RTO定义、跨区域复制及带宽受限下的恢复时间；而所有4个子节点均在讨论‘HDD/SSD RAID6/EC重建’，这是传统块存储或本地磁盘阵列的概念，与云对象存储的分布式数据管理模型（无固定本地重建概念，依赖副本/纠删码分布）在底层逻辑上存在根本冲突。此外，子节点之间存在大量冗余，后三个子节点本质上是在计算同一类参数（带宽/盘数/时间），只是介质不同，缺乏对云存储特有机制（如跨区域延迟、故障切换逻辑）的覆盖。）

## Search Query

AWS S3 cross-region replication failover RTO disaster recovery time 500TB

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2037820584256607993&rut=649de5d4a64cec414c3fc83a34ac8f715eb3556cb1e347d6b906d47f47ba0911', 'type': 'ddg', 'title': '一文搞懂 Oss 对象存储：标准 / 低频 / 归档 / 冷归档 + 本地 / 同城冗余全解析 - 知乎'}
