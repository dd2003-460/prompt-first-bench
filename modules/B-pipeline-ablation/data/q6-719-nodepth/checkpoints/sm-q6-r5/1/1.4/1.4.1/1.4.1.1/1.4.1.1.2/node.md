# N463: D_peak 分布形态修正对带宽租赁策略的影响：若采用 95th 峰值计费，带宽租赁成本 C_bw_95 = B_95 * P_bw_95 * D_95 * 7

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N148

## Claim

D_peak 分布形态修正对带宽租赁策略的影响：若采用 95th 峰值计费，带宽租赁成本 C_bw_95 = B_95 * P_bw_95 * D_95 * 720h，其中 B_95 为 95th 分位带宽；对比最大峰值计费 C_bw_peak = B_peak * P_bw_peak * D_peak * 720h，由于 B_95 < B_peak 且 D_95 < D_peak，混合策略下自建部分应优先采用 95th 峰值计费以降低成本，公有云部分因按量付费无此差异。

## Corrected Claim

D_peak 分布形态修正对带宽租赁策略的影响：若采用 95th 峰值计费，带宽租赁成本 C_bw_95 = B_95 * P_bw_95 * D_95 * 720h，其中 B_95 为 95th 分位带宽；对比最大峰值计费 C_bw_peak = B_peak * P_bw_peak * D_peak * 720h，由于 B_95 < B_peak 且 D_95 < D_peak，混合策略下自建部分应优先采用 95th 峰值计费以降低成本，公有云部分因按量付费无此差异。

## Evidence

先验知识/题面给定，逻辑校验通过：95th分位带宽及持续时间通常小于最大峰值，因此基于95th分位的计费成本在数学上低于基于最大峰值的计费成本，符合带宽租赁的一般经济逻辑。
