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

父节点级核验未通过：有冗余（子节点本质上是同一个参数（带宽/网络配置）在不同取值下的计算结果和对应约束条件，属于同一维度的枚举而非正交的知识维度。虽然覆盖了从低成本到高成本的典型场景，但结构上存在高度冗余，应合并为一个包含多档参数的节点或表格。）

## Search Query

cloud storage full recovery time calculation 500TB 1Gbps bandwidth
