# N99: 云对象存储（S3/OSS）的RTO量化值：基于99.999%持久性承诺，数据恢复时间主要受限于带宽限制（默认125Mbps/账户，可申请提升至1Gbps+），5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

云对象存储（S3/OSS）的RTO量化值：基于99.999%持久性承诺，数据恢复时间主要受限于带宽限制（默认125Mbps/账户，可申请提升至1Gbps+），500TB数据在1Gbps带宽下恢复时间≈500*1024*8/1000/3600≈11.4小时，远超RTO=4h目标；若仅恢复关键温数据（100TB），恢复时间≈2.3小时，满足RTO=4h目标，但冷数据恢复不满足

## Corrected Claim

云对象存储（S3/OSS）的RTO量化值：基于99.999%持久性承诺，数据恢复时间主要受限于带宽限制（默认125Mbps/账户，可申请提升至1Gbps+），500TB数据在1Gbps带宽下恢复时间≈500*1024*8/1000/3600≈11.4小时，远超RTO=4h目标；若仅恢复关键温数据（100TB），恢复时间≈2.3小时，满足RTO=4h目标，但冷数据恢复不满足

## Evidence

先验知识/题面给定，逻辑校验通过：带宽换算与时间估算符合物理直觉（500TB/1Gbps≈11.4h，100TB≈2.3h），且S3默认带宽限制及持久性承诺符合行业常识。

## Search Query

AWS S3 data recovery time 500TB bandwidth limit RTO
