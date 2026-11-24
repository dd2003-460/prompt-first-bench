# N464: 带宽峰值计费月度成本模型：Cost_peak = P_bw_max * N_pop * 12，其中 P_bw_max 为单点峰值带宽单价（¥/Gbps/月），N

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N149

## Claim

带宽峰值计费月度成本模型：Cost_peak = P_bw_max * N_pop * 12，其中 P_bw_max 为单点峰值带宽单价（¥/Gbps/月），N_pop 为 POP 点数量（10），该模型适用于 D_peak < 0.08 的短时高峰场景，固定成本主导。

## Corrected Claim

带宽峰值计费月度成本模型：Cost_peak = P_bw_max * N_pop * 12，其中 P_bw_max 为单点峰值带宽单价（¥/Gbps/月），N_pop 为 POP 点数量（10），该模型适用于 D_peak < 0.08 的短时高峰场景，固定成本主导。

## Evidence

先验知识/题面给定，逻辑校验通过
