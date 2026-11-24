# N83: 云对象存储全量恢复 500TB 数据在 1Gbps 带宽下的理论时间 T_rto_cloud_full = 500TB / 125MB/s ≈ 46.3 天，若

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

云对象存储全量恢复 500TB 数据在 1Gbps 带宽下的理论时间 T_rto_cloud_full = 500TB / 125MB/s ≈ 46.3 天，若采用 10Gbps 专线则缩短至 4.6 天，需根据实际网络带宽确定 RTO

## Corrected Claim

云对象存储全量恢复 500TB 数据在 1Gbps 带宽下的理论时间 T_rto_cloud_full = 500TB / 125MB/s ≈ 46.3 天，若采用 10Gbps 专线则缩短至 4.6 天，需根据实际网络带宽确定 RTO

## Evidence

先验知识/题面给定，逻辑校验通过：1Gbps=125MB/s，500TB/125MB/s≈46.3天，10Gbps下时间缩短为1/10即4.6天，计算准确且符合物理直觉

## Search Query

cloud storage full recovery time calculation 500TB 1Gbps bandwidth
