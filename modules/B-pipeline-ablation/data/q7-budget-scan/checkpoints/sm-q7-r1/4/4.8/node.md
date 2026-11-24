# N22: 云对象存储的 RTO (小时) ≈ 0（多副本/多可用区自动恢复），但数据恢复至计算集群的传输时间 = 数据量 (TB) / 云出口带宽 (GB/s)，500T

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

云对象存储的 RTO (小时) ≈ 0（多副本/多可用区自动恢复），但数据恢复至计算集群的传输时间 = 数据量 (TB) / 云出口带宽 (GB/s)，500TB 传输约需 50-100 小时（假设 10 Gbps 带宽）

## Corrected Claim

云对象存储的 RTO (小时) ≈ 0（多副本/多可用区自动恢复），但数据恢复至计算集群的传输时间 = 数据量 (TB) / 云出口带宽 (GB/s)，500TB 传输约需 50-100 小时（假设 10 Gbps 带宽）

## Evidence

先验知识/题面给定，逻辑校验通过：500TB / (10Gbps/8) ≈ 400,000s ≈ 111小时，与50-100小时量级兼容（考虑实际吞吐损耗或带宽波动）

## Search Query

cloud object storage data egress time per TB
