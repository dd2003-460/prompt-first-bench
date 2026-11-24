# N28: 公有云CDN的缓存层级为两级：L1边缘节点（高并发低容量）和L2中间层节点（低并发高容量），回源路径为 L1 Miss -> L2 -> 源站，L2命中率为 H

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

公有云CDN的缓存层级为两级：L1边缘节点（高并发低容量）和L2中间层节点（低并发高容量），回源路径为 L1 Miss -> L2 -> 源站，L2命中率为 H_L2。

## Corrected Claim

公有云CDN的缓存层级为两级：L1边缘节点（高并发低容量）和L2中间层节点（低并发高容量），回源路径为 L1 Miss -> L2 -> 源站，L2命中率为 H_L2。

## Evidence

先验知识/题面给定，逻辑校验通过
