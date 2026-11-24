# N246: 单POP带宽瓶颈带宽上限 C_bw_pop = B_port * (1 - Reserved_For_Backhaul)，其中 B_port 为单POP出口物理

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

单POP带宽瓶颈带宽上限 C_bw_pop = B_port * (1 - Reserved_For_Backhaul)，其中 B_port 为单POP出口物理带宽（如 10Gbps 或 40Gbps 光模块），Reserved_For_Backhaul 为预留回源带宽比例（典型 20%-30%，用于缓存失效时回源）；若 B_port=10Gbps 且预留 25%，则 C_bw_pop = 10 * 0.75 = 7.5 Gbps。

## Corrected Claim

单POP带宽瓶颈带宽上限 C_bw_pop = B_port * (1 - Reserved_For_Backhaul)，其中 B_port 为单POP出口物理带宽（如 10Gbps 或 40Gbps 光模块），Reserved_For_Backhaul 为预留回源带宽比例（典型 20%-30%，用于缓存失效时回源）；若 B_port=10Gbps 且预留 25%，则 C_bw_pop = 10 * 0.75 = 7.5 Gbps。

## Evidence

先验知识/题面给定，逻辑校验通过：公式定义清晰，数值计算（10 * 0.75 = 7.5）准确，符合网络带宽规划的基本逻辑。

## Search Query

CDN POP edge node bandwidth reservation backhaul ratio best practice
