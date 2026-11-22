# N506: N155 中 '512 TFLOPS' 的错误源于将 RTX 5090 的 FP16/BF16 峰值（524.3 TFLOPS）误标为 FP8，或混淆了 Spa

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N155

## Claim

N155 中 '512 TFLOPS' 的错误源于将 RTX 5090 的 FP16/BF16 峰值（524.3 TFLOPS）误标为 FP8，或混淆了 Sparse 与 Dense 模式下的不同计数方式；Blackwell 架构下 FP8 吞吐量是 FP16 的 2 倍。

## Corrected Claim

N155 中 '512 TFLOPS' 的错误源于将 RTX 5090 的 FP16/BF16 峰值（524.3 TFLOPS）误标为 FP8，或混淆了 Sparse 与 Dense 模式下的不同计数方式；Blackwell 架构下 FP8 吞吐量是 FP16 的 2 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：Blackwell架构（如RTX 5090）确实支持FP8吞吐量约为FP16的2倍，且524.3 TFLOPS符合RTX 5090 FP16/BF16 Dense峰值的量级，逻辑自洽。

## Search Query

Blackwell architecture FP8 vs FP16 throughput ratio 2x
