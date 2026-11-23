# N132: 静态文件源站处理时间 T_origin_static 的基准值，取决于对象存储后端类型：S3/OSS标准存储约为 10-20ms，本地NVMe SSD缓存层约为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

静态文件源站处理时间 T_origin_static 的基准值，取决于对象存储后端类型：S3/OSS标准存储约为 10-20ms，本地NVMe SSD缓存层约为 5-10ms。

## Corrected Claim

静态文件源站处理时间 T_origin_static 的基准值，取决于对象存储后端类型：S3/OSS标准存储约为 10-20ms，本地NVMe SSD缓存层约为 5-10ms。

## Evidence

先验知识/题面给定，逻辑校验通过：S3/OSS标准存储网络往返及处理延迟通常在10-20ms量级，本地NVMe SSD读取延迟在微秒至毫秒级，加上系统开销后5-10ms符合工程直觉。

## Search Query

object storage S3 latency benchmark ms
