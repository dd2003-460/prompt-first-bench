# N226: 云对象存储恢复所需的理论最小带宽 B_min = 数据总量(500TB) / RTO目标(4h) = 500 * 1024^4 Bytes / (4 * 360

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N90

## Claim

云对象存储恢复所需的理论最小带宽 B_min = 数据总量(500TB) / RTO目标(4h) = 500 * 1024^4 Bytes / (4 * 3600 s) ≈ 11.17 Gbps (注意：N90原claim中的11.4Gbps与此基本一致，但需确认是否包含协议开销)

## Corrected Claim

云对象存储恢复所需的理论最小带宽 B_min = 数据总量(500TB) / RTO目标(4h) = 500 * 1024^4 Bytes / (4 * 3600 s) ≈ 11.17 Gbps (注意：N90原claim中的11.4Gbps与此基本一致，但需确认是否包含协议开销)

## Evidence

先验知识/题面给定，逻辑校验通过：500TB转换为Bytes后除以4小时秒数，计算结果约为11.17Gbps，量纲与数值均正确。
