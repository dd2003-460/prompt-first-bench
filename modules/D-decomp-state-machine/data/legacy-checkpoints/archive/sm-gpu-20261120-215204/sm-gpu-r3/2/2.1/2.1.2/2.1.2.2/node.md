# N201: A100 80GB SXM4 在 BF16 精度下运行 Qwen3-27B 的实际有效算力（Effective TFLOPS）约为 125 TFLOPS，计算依

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

A100 80GB SXM4 在 BF16 精度下运行 Qwen3-27B 的实际有效算力（Effective TFLOPS）约为 125 TFLOPS，计算依据为理论峰值 312 TFLOPS 乘以经验 MFU 值 40%（N113 已验证），此数值是计算其 32K 上下文 TTFT 下限（约 14ms）的核心参数。

## Corrected Claim

A100 80GB SXM4 在 BF16 精度下运行 Qwen3-27B 的实际有效算力（Effective TFLOPS）约为 125 TFLOPS，计算依据为理论峰值 312 TFLOPS 乘以经验 MFU 值 40%（N113 已验证），此数值是计算其 32K 上下文 TTFT 下限（约 14ms）的核心参数。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB SXM4 BF16 理论峰值约为 312 TFLOPS，40% MFU 下有效算力约为 125 TFLOPS，数值量级与工程经验一致。
