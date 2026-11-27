# N133: 各候选硬件BF16 Prefill理论耗时：RTX 4090 (82.6 TFLOPS) ≈ 2.81e15 / 82.6e12 ≈ 34.0s; A100 8

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N26

## Claim

各候选硬件BF16 Prefill理论耗时：RTX 4090 (82.6 TFLOPS) ≈ 2.81e15 / 82.6e12 ≈ 34.0s; A100 80GB (312 TFLOPS) ≈ 9.0s; H100 80GB (989 TFLOPS) ≈ 2.84s; M3 Ultra (假设~30 TFLOPS BF16 [待核验]) ≈ 93.7s。

## Corrected Claim

各候选硬件BF16 Prefill理论耗时：RTX 4090 (82.6 TFLOPS) ≈ 2.81e15 / 82.6e12 ≈ 34.0s; A100 80GB (312 TFLOPS) ≈ 9.0s; H100 80GB (989 TFLOPS) ≈ 2.84s; M3 Ultra (假设~30 TFLOPS BF16 [待核验]) ≈ 93.7s。

## Evidence

[质询]M3 Ultra 的 BF16 算力假设值（~30 TFLOPS）可能偏低，实际 Apple Silicon 在矩阵运算上的峰值性能可能更高，导致耗时估算偏大；但作为‘假设’值，逻辑上自洽。 | 先验知识/题面给定，逻辑校验通过：耗时 = 总浮点运算量 / 理论峰值算力，数值量级与硬件规格匹配，计算过程无误。
