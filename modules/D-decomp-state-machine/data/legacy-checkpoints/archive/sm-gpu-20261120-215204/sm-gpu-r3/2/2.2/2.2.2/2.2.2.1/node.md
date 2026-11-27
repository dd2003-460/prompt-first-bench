# N206: H100 SXM5 在 FP8 精度下的理论峰值算力为 3958 TFLOPS，而在 BF16 精度下为 1979 TFLOPS，FP8 算力是 BF16 的 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

H100 SXM5 在 FP8 精度下的理论峰值算力为 3958 TFLOPS，而在 BF16 精度下为 1979 TFLOPS，FP8 算力是 BF16 的 2.0 倍，这是 N72 中吞吐量提升上限的理论基础。

## Corrected Claim

H100 SXM5 在 FP8 精度下的理论峰值算力为 3958 TFLOPS，而在 BF16 精度下为 1979 TFLOPS，FP8 算力是 BF16 的 2.0 倍，这是 N72 中吞吐量提升上限的理论基础。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 FP8 (3958 TFLOPS) 与 BF16 (1979 TFLOPS) 数值符合 NVIDIA 官方规格，且 3958/1979 ≈ 2.0，逻辑自洽。
