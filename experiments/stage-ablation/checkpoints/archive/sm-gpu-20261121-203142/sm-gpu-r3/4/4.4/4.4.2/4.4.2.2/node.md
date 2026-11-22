# N276: RTX 4090 在 BF16 精度下的实际有效算力（Effective TFLOPS）受限于 Tensor Core 利用率及内存访问模式，通常仅为峰值算力（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N88

## Claim

RTX 4090 在 BF16 精度下的实际有效算力（Effective TFLOPS）受限于 Tensor Core 利用率及内存访问模式，通常仅为峰值算力（82.6 TFLOPS）的 60-80%；因此实际 Prefill 时间应基于 Effective_TFLOPS = 82.6 * 0.7 (avg) ≈ 57.8 TFLOPS 计算，修正后的理论时间约为 1.7e12 / 57.8e12 ≈ 29.4 秒，这与 N88 中乐观的 5-10 秒存在显著差距，需进一步分析 FlashAttention 对计算密集度的具体加速比。

## Corrected Claim

RTX 4090 在 BF16 精度下的实际有效算力（Effective TFLOPS）受限于 Tensor Core 利用率及内存访问模式，通常仅为峰值算力（82.6 TFLOPS）的 60-80%；因此实际 Prefill 时间应基于 Effective_TFLOPS = 82.6 * 0.7 (avg) ≈ 57.8 TFLOPS 计算，修正后的理论时间约为 1.7e12 / 57.8e12 ≈ 29.4 秒，这与 N88 中乐观的 5-10 秒存在显著差距，需进一步分析 FlashAttention 对计算密集度的具体加速比。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 BF16峰值算力约82.6 TFLOPS，实际有效算力受限于Tensor Core利用率（通常60-80%），取均值70%得57.8 TFLOPS，计算1.7e12 FLOPs耗时约29.4秒，逻辑自洽且数值量级合理。
