# N46: FP8推理对TTFT/TPOT的提升系数：相比BF16，权重体积减半使得每token读取字节数减少，理论TPOT降低约50%，但需扣除FP8 GEMM算子效率损

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10

## Claim

FP8推理对TTFT/TPOT的提升系数：相比BF16，权重体积减半使得每token读取字节数减少，理论TPOT降低约50%，但需扣除FP8 GEMM算子效率损失（通常FP8 Tensor Core效率略低于BF16，需查具体硬件加速比）。

## Corrected Claim

FP8推理对TTFT/TPOT的提升系数：相比BF16，权重体积减半使得每token读取字节数减少，理论TPOT降低约50%，但需扣除FP8 GEMM算子效率损失（通常FP8 Tensor Core效率略低于BF16，需查具体硬件加速比）。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8相比BF16位宽减半，理论带宽需求减半，TPOT理论降低约50%符合物理直觉；同时正确指出了需扣除算子效率损失这一关键工程约束，逻辑自洽。

## Search Query

FP8 tensor core efficiency vs BF16 inference speedup ratio
