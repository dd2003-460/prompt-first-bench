# N653: 云端故障概率P_f：基于AWS/GCP历史SLA数据，月度不可用时间约为1-5分钟，折算为单次请求故障概率P_f≈1e-5，用于计算冗余备份的期望成本

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N238, N239, N240

## Claim

云端故障概率P_f：基于AWS/GCP历史SLA数据，月度不可用时间约为1-5分钟，折算为单次请求故障概率P_f≈1e-5，用于计算冗余备份的期望成本

## Corrected Claim

云端故障概率P_f：基于AWS/GCP历史SLA数据，月度不可用时间约为1-5分钟，折算为单次请求故障概率P_f≈1e-5，用于计算冗余备份的期望成本

## Evidence

先验知识/题面给定，逻辑校验通过：月度不可用1-5分钟对应约0.002%-0.01%的月度故障率，假设请求均匀分布，单次请求故障概率量级确实在1e-5左右，符合工程估算惯例。

## Search Query

cloud provider SLA availability monthly downtime probability
