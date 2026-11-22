# N296: INT4 量化引入的反量化 (Dequantization) 计算开销量化：每层 GEMM 前需将 INT4 权重转换为 FP16/BF16，增加约 5-10%

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N95

## Claim

INT4 量化引入的反量化 (Dequantization) 计算开销量化：每层 GEMM 前需将 INT4 权重转换为 FP16/BF16，增加约 5-10% 的额外 FLOPs 开销（取决于 Kernel 优化程度），在 Compute-bound 区域（大 Batch）会抵消部分带宽节省带来的 TPS 增益，需从理论 TPS 中扣除该系数。

## Corrected Claim

INT4 量化引入的反量化 (Dequantization) 计算开销量化：每层 GEMM 前需将 INT4 权重转换为 FP16/BF16，增加约 5-10% 的额外 FLOPs 开销（取决于 Kernel 优化程度），在 Compute-bound 区域（大 Batch）会抵消部分带宽节省带来的 TPS 增益，需从理论 TPS 中扣除该系数。

## Evidence

先验知识/题面给定，逻辑校验通过
