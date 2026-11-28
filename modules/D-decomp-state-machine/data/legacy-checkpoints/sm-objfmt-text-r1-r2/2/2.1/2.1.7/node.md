# N48: 在 Memory-Bound 区域 (Batch Size=1)，理论加速比等于显存节省比例：FP8 相对 BF16 提速 2x，W4 相对 BF16 提速 4

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13, N14, N15

## Claim

在 Memory-Bound 区域 (Batch Size=1)，理论加速比等于显存节省比例：FP8 相对 BF16 提速 2x，W4 相对 BF16 提速 4x；但在 Compute-Bound 区域 (高 Batch Size)，由于反量化 (Dequantization) 开销和 Tensor Core 对低精度支持效率的差异，实际加速比衰减至 1.5x (FP8) 和 2.5x (W4)

## Corrected Claim

在 Memory-Bound 区域 (Batch Size=1)，理论加速比等于显存节省比例：FP8 相对 BF16 提速 2x，W4 相对 BF16 提速 4x；但在 Compute-Bound 区域 (高 Batch Size)，由于反量化 (Dequantization) 开销和 Tensor Core 对低精度支持效率的差异，实际加速比衰减至 1.5x (FP8) 和 2.5x (W4)

## Evidence

先验知识/题面给定，逻辑校验通过
