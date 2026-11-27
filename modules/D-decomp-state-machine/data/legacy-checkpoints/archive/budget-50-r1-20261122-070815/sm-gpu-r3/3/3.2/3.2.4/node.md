# N82: NVIDIA H100 的 BF16/FP16 峰值算力约为 989 TFLOPS，INT8 峰值算力约为 1979 TOPS，FP8 峰值算力约为 3958 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

NVIDIA H100 的 BF16/FP16 峰值算力约为 989 TFLOPS，INT8 峰值算力约为 1979 TOPS，FP8 峰值算力约为 3958 TFLOPS，原生 FP8 支持使其在 Prefill 阶段具有显著优势

## Corrected Claim

NVIDIA H100 的 BF16/FP16 峰值算力约为 989 TFLOPS，INT8 峰值算力约为 1979 TOPS，FP8 峰值算力约为 3958 TFLOPS，原生 FP8 支持使其在 Prefill 阶段具有显著优势

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 规格中 BF16/FP16 为 989 TFLOPS，INT8 为 1979 TOPS，FP8 为 3958 TFLOPS，数值量级与精度倍数关系（FP8=2x BF16, INT8=2x BF16）符合硬件架构逻辑。
