# N258: 在低成本共享带宽工作点（1Gbps公网），T_rto_cloud_full ≈ 46.3 天；此时间远超任何本地方案，主要受限于ISP带宽瓶颈及潜在QoS限制，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N83

## Claim

在低成本共享带宽工作点（1Gbps公网），T_rto_cloud_full ≈ 46.3 天；此时间远超任何本地方案，主要受限于ISP带宽瓶颈及潜在QoS限制，适用于对RTO无严格要求的归档恢复场景

## Corrected Claim

在低成本共享带宽工作点（1Gbps公网），T_rto_cloud_full ≈ 46.3 天；此时间远超任何本地方案，主要受限于ISP带宽瓶颈及潜在QoS限制，适用于对RTO无严格要求的归档恢复场景

## Evidence

先验知识/题面给定，逻辑校验通过：1Gbps带宽下传输约40TB数据需约46天，量级合理且符合物理直觉
