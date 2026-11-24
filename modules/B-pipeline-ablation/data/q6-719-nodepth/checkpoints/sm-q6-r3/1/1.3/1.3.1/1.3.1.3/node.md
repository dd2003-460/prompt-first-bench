# N164: T_transfer_edge（边缘到用户传输时间）= Object_Size / Effective_Bandwidth，其中 Effective_Bandw

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N46

## Claim

T_transfer_edge（边缘到用户传输时间）= Object_Size / Effective_Bandwidth，其中 Effective_Bandwidth 受限于用户侧最后一公里带宽（典型 4G/WiFi 为 5-50Mbps）而非边缘节点出口带宽；对于 5MB 短视频，在 10Mbps 用户带宽下 T_transfer_edge ≈ 4000ms，这是 P99 延迟的主要贡献项

## Corrected Claim

T_transfer_edge（边缘到用户传输时间）= Object_Size / Effective_Bandwidth，其中 Effective_Bandwidth 受限于用户侧最后一公里带宽（典型 4G/WiFi 为 5-50Mbps）而非边缘节点出口带宽；对于 5MB 短视频，在 10Mbps 用户带宽下 T_transfer_edge ≈ 4000ms，这是 P99 延迟的主要贡献项

## Evidence

先验知识/题面给定，逻辑校验通过：5MB * 8 / 10Mbps = 4000ms，计算正确且符合网络传输基本物理规律
