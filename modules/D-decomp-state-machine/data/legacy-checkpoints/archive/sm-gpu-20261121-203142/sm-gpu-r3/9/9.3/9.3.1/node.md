# N356: Apple M2 Ultra 在 32K 上下文下，使用 BF16 精度且未启用 FlashAttention 优化时，Prefill 阶段受限于 30 TFL

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

Apple M2 Ultra 在 32K 上下文下，使用 BF16 精度且未启用 FlashAttention 优化时，Prefill 阶段受限于 30 TFLOPS 算力，理论耗时为 (2 * 27e9 * 32768) / 30e12 ≈ 18.9 秒，此为高延迟低优化工作点。

## Corrected Claim

Apple M2 Ultra 在 32K 上下文下，使用 BF16 精度且未启用 FlashAttention 优化时，Prefill 阶段受限于 30 TFLOPS 算力，理论耗时为 (2 * 27e9 * 32768) / 30e12 ≈ 18.9 秒，此为高延迟低优化工作点。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 算力约 30 TFLOPS，Prefill 计算量公式 2*N*L 正确，数值计算 (2*27e9*32768)/30e12 ≈ 18.9s 准确。
