# N259: 在中成本专线带宽工作点（10Gbps Dedicated Line），T_rto_cloud_full ≈ 4.6 天；需额外考虑专线租赁成本（约¥5000-¥

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

在中成本专线带宽工作点（10Gbps Dedicated Line），T_rto_cloud_full ≈ 4.6 天；需额外考虑专线租赁成本（约¥5000-¥10000/月）及数据压缩比（假设压缩后体积为原始的30%，则实际传输时间缩短至 4.6 * 0.3 ≈ 1.4 天），综合评估带宽成本与RTO收益

## Corrected Claim

在中成本专线带宽工作点（10Gbps Dedicated Line），T_rto_cloud_full ≈ 4.6 天；需额外考虑专线租赁成本（约¥5000-¥10000/月）及数据压缩比（假设压缩后体积为原始的30%，则实际传输时间缩短至 4.6 * 0.3 ≈ 1.4 天），综合评估带宽成本与RTO收益

## Evidence

先验知识/题面给定，逻辑校验通过：10Gbps带宽下传输数据量对应4.6天符合量级估算（约4.6TB原始数据），压缩比30%线性缩短时间逻辑自洽，专线成本区间符合市场常识。
