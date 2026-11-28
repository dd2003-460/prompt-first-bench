# N191: 4卡并行集群的总有效算力 F_total = F_single * N_gpus * η_parallel，其中 η_parallel 为并行效率因子，受 Al

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N56

## Claim

4卡并行集群的总有效算力 F_total = F_single * N_gpus * η_parallel，其中 η_parallel 为并行效率因子，受 AllReduce 通信开销影响，在 TP=4 且 NVLink 互联下，η_parallel ≈ 0.85-0.90，故 F_total ≈ 6.28e12 * 4 * 0.875 ≈ 2.198e13 FLOPs/s

## Corrected Claim

4卡并行集群的总有效算力 F_total = F_single * N_gpus * η_parallel，其中 η_parallel 为并行效率因子，受 AllReduce 通信开销影响，在 TP=4 且 NVLink 互联下，η_parallel ≈ 0.85-0.90，故 F_total ≈ 6.28e12 * 4 * 0.875 ≈ 2.198e13 FLOPs/s

## Evidence

先验知识/题面给定，逻辑校验通过：TP=4在NVLink下并行效率0.85-0.90符合工程常识，算术计算 6.28e12 * 4 * 0.875 = 2.198e13 准确无误。
