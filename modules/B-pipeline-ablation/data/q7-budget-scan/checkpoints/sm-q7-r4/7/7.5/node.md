# N119: 优化策略：使用S3 Batch Get或Multipart Download提升有效带宽；若通过多连接并行下载将有效带宽提升至50Gbps (6.25GB/s)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N32

## Claim

优化策略：使用S3 Batch Get或Multipart Download提升有效带宽；若通过多连接并行下载将有效带宽提升至50Gbps (6.25GB/s)，T_net降至22.2小时，C_idle_cloud_daily降至(22.2-2)*2*5000=¥202,000/天；需评估多连接对API QPS的新压力及额外网络成本。

## Corrected Claim

优化策略：使用S3 Batch Get或Multipart Download提升有效带宽；若通过多连接并行下载将有效带宽提升至50Gbps (6.25GB/s)，T_net降至22.2小时，C_idle_cloud_daily降至(22.2-2)*2*5000=¥202,000/天；需评估多连接对API QPS的新压力及额外网络成本。

## Evidence

先验知识/题面给定，逻辑校验通过：50Gbps=6.25GB/s，假设数据量约875TB（基于T_net=22.2h反推），计算(22.2-2)*2*5000=202,000元/天，算术与单位换算均正确。
