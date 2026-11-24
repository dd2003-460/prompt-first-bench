# N245: 单POP计算瓶颈带宽上限 C_comp_pop = N_cores * C_core_bw * Efficiency，其中 N_cores 为单服务器核心数（典

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

单POP计算瓶颈带宽上限 C_comp_pop = N_cores * C_core_bw * Efficiency，其中 N_cores 为单服务器核心数（典型 32-64核），C_core_bw 为单核处理带宽能力（典型 100-200 Mbps/core，取决于CPU型号与软件栈优化），Efficiency 为CPU利用率上限（典型 0.6-0.8）；计算得 C_comp_pop ≈ 64 * 150Mbps * 0.7 = 6.72 Gbps，需与带宽瓶颈 6.93Gbps 取 min。

## Corrected Claim

单POP计算瓶颈带宽上限 C_comp_pop = N_cores * C_core_bw * Efficiency，其中 N_cores 为单服务器核心数（典型 32-64核），C_core_bw 为单核处理带宽能力（典型 100-200 Mbps/core，取决于CPU型号与软件栈优化），Efficiency 为CPU利用率上限（典型 0.6-0.8）；计算得 C_comp_pop ≈ 64 * 150Mbps * 0.7 = 6.72 Gbps，需与带宽瓶颈 6.93Gbps 取 min。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CDN edge server single core throughput bandwidth limit Mbps
