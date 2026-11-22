# N324: 实际 TPS 效率损耗因子 (Efficiency_Factor) 的量化范围：受 SM 利用率、Kernel 启动开销、内存访问模式 (Coalescing)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N106

## Claim

实际 TPS 效率损耗因子 (Efficiency_Factor) 的量化范围：受 SM 利用率、Kernel 启动开销、内存访问模式 (Coalescing) 影响，实际 TPS 通常为理论峰值的 60%-80%；若 5090 效率为 70%，4090 效率为 75% (因架构更成熟)，则实际 TPS 比为 (1792*0.70) / (1008*0.75) = 1.653x，落在 1.5x-1.8x 区间内。

## Corrected Claim

实际 TPS 效率损耗因子 (Efficiency_Factor) 的量化范围：受 SM 利用率、Kernel 启动开销、内存访问模式 (Coalescing) 影响，实际 TPS 通常为理论峰值的 60%-80%；若 5090 效率为 70%，4090 效率为 75% (因架构更成熟)，则实际 TPS 比为 (1792*0.70) / (1008*0.75) = 1.653x，落在 1.5x-1.8x 区间内。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 (1792*0.7)/(1008*0.75) ≈ 1.653 正确，且 1.653 确实落在 1.5-1.8 区间内；效率因子 60%-80% 符合 GPU 实际性能损耗的工程经验常识。

## Search Query

GPU inference efficiency factor memory bound LLM
