# N108: 公有云CDN回源延迟分解：L_backhaul_cloud = T_backhaul_network_cloud + T_origin_processing_c

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

公有云CDN回源延迟分解：L_backhaul_cloud = T_backhaul_network_cloud + T_origin_processing_cloud，其中T_backhaul_network_cloud ≈ 5-20ms（同区域云内高速网络），T_origin_processing_cloud ≈ 3-8ms（云原生存储优化）

## Corrected Claim

公有云CDN回源延迟分解：L_backhaul_cloud = T_backhaul_network_cloud + T_origin_processing_cloud，其中T_backhaul_network_cloud ≈ 5-20ms（同区域云内高速网络），T_origin_processing_cloud ≈ 3-8ms（云原生存储优化）

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

cloud CDN origin backhaul latency breakdown same-region high-speed network and cloud storage optimization
