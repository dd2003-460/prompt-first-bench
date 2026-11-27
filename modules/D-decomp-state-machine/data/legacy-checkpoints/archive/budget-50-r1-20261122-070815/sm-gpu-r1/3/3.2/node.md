# N19: 计算密度（TFLOPS）影响 prefill 阶段速度，需对比各硬件在 FP16/BF16/INT8 下的峰值算力

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

计算密度（TFLOPS）影响 prefill 阶段速度，需对比各硬件在 FP16/BF16/INT8 下的峰值算力

## Corrected Claim

计算密度（TFLOPS）影响 prefill 阶段速度，需对比各硬件在 FP16/BF16/INT8 下的峰值算力

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill阶段为计算密集型（Compute-bound），其速度主要受限于硬件峰值算力（TFLOPS），且不同精度（FP16/BF16/INT8）对应不同的算力规格，需对比以评估性能。
