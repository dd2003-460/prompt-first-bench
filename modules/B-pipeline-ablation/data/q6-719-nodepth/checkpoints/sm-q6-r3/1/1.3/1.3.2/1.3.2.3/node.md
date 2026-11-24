# N167: T_transfer_origin（源站到边缘传输时间）= Object_Size / Bandwidth_to_origin，其中 Bandwidth_to_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N47

## Claim

T_transfer_origin（源站到边缘传输时间）= Object_Size / Bandwidth_to_origin，其中 Bandwidth_to_origin 为源站与边缘节点间的内网带宽（通常 10Gbps-100Gbps）；对于 5MB 对象，在 10Gbps 内网带宽下 T_transfer_origin ≈ 5MB / (10Gbps/8) ≈ 4ms

## Corrected Claim

T_transfer_origin（源站到边缘传输时间）= Object_Size / Bandwidth_to_origin，其中 Bandwidth_to_origin 为源站与边缘节点间的内网带宽（通常 10Gbps-100Gbps）；对于 5MB 对象，在 10Gbps 内网带宽下 T_transfer_origin ≈ 5MB / (10Gbps/8) ≈ 4ms

## Evidence

先验知识/题面给定，逻辑校验通过：5MB / (10Gbps/8) = 5 * 8 / 10000 s = 0.004s = 4ms，计算正确且量级合理。
