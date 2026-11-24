# N22: 云对象存储的 RTO (小时) ≈ 0（多副本/多可用区自动恢复），但数据恢复至计算集群的传输时间 = 数据量 (TB) / 云出口带宽 (GB/s)，500T

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N4

## Claim

云对象存储的 RTO (小时) ≈ 0（多副本/多可用区自动恢复），但数据恢复至计算集群的传输时间 = 数据量 (TB) / 云出口带宽 (GB/s)，500TB 传输约需 50-100 小时（假设 10 Gbps 带宽）

## Corrected Claim

云对象存储的 RTO (小时) ≈ 0（多副本/多可用区自动恢复），但数据恢复至计算集群的传输时间 = 数据量 (TB) / 云出口带宽 (GB/s)，500TB 传输约需 50-100 小时（假设 10 Gbps 带宽）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了带宽限制、API限速和多可用区延迟三个独立维度，正交性好；涵盖了父节点中传输时间计算的关键瓶颈（带宽、API、延迟），完备性高；各子节点描述的是不同的物理/逻辑约束，不存在冗余。）

## Search Query

cloud object storage data egress time per TB
