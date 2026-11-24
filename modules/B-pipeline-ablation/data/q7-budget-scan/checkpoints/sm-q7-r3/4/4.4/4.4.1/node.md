# N83: 云对象存储全量恢复 500TB 数据在 1Gbps 带宽下的理论时间 T_rto_cloud_full = 500TB / 125MB/s ≈ 46.3 天，若

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

云对象存储全量恢复 500TB 数据在 1Gbps 带宽下的理论时间 T_rto_cloud_full = 500TB / 125MB/s ≈ 46.3 天，若采用 10Gbps 专线则缩短至 4.6 天，需根据实际网络带宽确定 RTO

## Corrected Claim

云对象存储全量恢复 500TB 数据在 1Gbps 带宽下的理论时间 T_rto_cloud_full = 500TB / 125MB/s ≈ 46.3 天，若采用 10Gbps 专线则缩短至 4.6 天，需根据实际网络带宽确定 RTO

## Evidence

父节点级核验未通过：有冗余（子节点分别描述了不同带宽等级下的恢复时间估算，虽然逻辑上互斥且覆盖了父节点提到的两个主要带宽场景及一个扩展场景，但它们本质上是同一个物理公式（T=V/B）在不同输入参数（带宽）下的实例化，属于同一维度的参数变体，而非独立的概念维度。）

## Search Query

cloud storage full recovery time calculation 500TB 1Gbps bandwidth
