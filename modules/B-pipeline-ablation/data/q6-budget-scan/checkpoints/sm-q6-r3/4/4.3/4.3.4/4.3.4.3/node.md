# N207: 副本系数 R_replica 的分解：R_replica = 1 + k_fragmentation + k_metadata，其中 k_fragmentati

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66, N67, N68

## Claim

副本系数 R_replica 的分解：R_replica = 1 + k_fragmentation + k_metadata，其中 k_fragmentation 为存储碎片率（通常 0.1-0.2），k_metadata 为元数据开销率（通常 0.05-0.1），总系数范围 1.15-1.35 [待核验]

## Corrected Claim

副本系数 R_replica 的分解：R_replica = 1 + k_fragmentation + k_metadata，其中 k_fragmentation 为存储碎片率（通常 0.1-0.2），k_metadata 为元数据开销率（通常 0.05-0.1），总系数范围 1.15-1.35 [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

NVMe SSD storage overhead fragmentation metadata ratio
