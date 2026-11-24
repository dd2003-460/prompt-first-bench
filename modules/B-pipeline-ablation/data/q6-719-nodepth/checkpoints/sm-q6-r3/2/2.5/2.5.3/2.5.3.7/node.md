# N208: 工作点 1（高性低成）：Utilization_target = 70%，Server_BW_capacity = 25Gbps，N_servers = cei

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N64, N65, N66

## Claim

工作点 1（高性低成）：Utilization_target = 70%，Server_BW_capacity = 25Gbps，N_servers = ceil(69.3 * 24 / (25 * 0.7)) = ceil(69.3 * 24 / 17.5) = ceil(94.9) = 95 台

## Corrected Claim

工作点 1（高性低成）：Utilization_target = 70%，Server_BW_capacity = 25Gbps，N_servers = ceil(69.3 * 24 / (25 * 0.7)) = ceil(69.3 * 24 / 17.5) = ceil(94.9) = 95 台

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 69.3 * 24 / (25 * 0.7) = 1663.2 / 17.5 ≈ 94.98，向上取整为 95，数值与逻辑均正确。
