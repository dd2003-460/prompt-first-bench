# N107: 自建POP回源延迟分解：L_backhaul_self = T_backhaul_network + T_origin_processing，其中T_backh

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

自建POP回源延迟分解：L_backhaul_self = T_backhaul_network + T_origin_processing，其中T_backhaul_network ≈ 15-40ms（跨省骨干网传输），T_origin_processing ≈ 5-10ms（源站磁盘读取+网络栈处理）

## Corrected Claim

自建POP回源延迟分解：L_backhaul_self = T_backhaul_network + T_origin_processing，其中T_backhaul_network ≈ 15-40ms（跨省骨干网传输），T_origin_processing ≈ 5-10ms（源站磁盘读取+网络栈处理）

## Evidence

先验知识/题面给定，逻辑校验通过：跨省骨干网传输延迟15-40ms及源站处理5-10ms符合网络工程常识与物理直觉，量级合理且内部自洽。

## Search Query

self-hosted CDN origin backhaul latency breakdown network transmission and origin processing time
