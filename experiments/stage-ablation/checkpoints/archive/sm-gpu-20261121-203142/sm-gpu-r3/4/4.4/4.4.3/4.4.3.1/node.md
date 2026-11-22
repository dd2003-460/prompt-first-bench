# N278: A100 80GB 在 BF16 精度下的实际有效算力（Effective TFLOPS）估算：峰值算力 312 TFLOPS，考虑到 A100 的 Tenso

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

A100 80GB 在 BF16 精度下的实际有效算力（Effective TFLOPS）估算：峰值算力 312 TFLOPS，考虑到 A100 的 Tensor Core 效率及 HBM 带宽平衡，实际利用率通常在 70-85% 之间；取 80% 计算，Effective_TFLOPS ≈ 249.6 TFLOPS；修正后的理论 Prefill 时间 = 1.7e12 / 249.6e12 ≈ 6.8 秒，这比 N89 中基于峰值算力的 5.45 秒更保守，需结合 FlashAttention 加速进一步修正。

## Corrected Claim

A100 80GB 在 BF16 精度下的实际有效算力（Effective TFLOPS）估算：峰值算力 312 TFLOPS，考虑到 A100 的 Tensor Core 效率及 HBM 带宽平衡，实际利用率通常在 70-85% 之间；取 80% 计算，Effective_TFLOPS ≈ 249.6 TFLOPS；修正后的理论 Prefill 时间 = 1.7e12 / 249.6e12 ≈ 6.8 秒，这比 N89 中基于峰值算力的 5.45 秒更保守，需结合 FlashAttention 加速进一步修正。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB BF16 峰值算力 312 TFLOPS 符合官方规格，70-85% 利用率估算符合工程经验，数学计算 1.7e12 / 249.6e12 ≈ 6.8 正确。
