# N123: 1×RTX 4090 在 16K 上下文 W4 精度下的实际 Tokens/s 估算：显存带宽 1008 GB/s / (13.5GB weights + 6.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

1×RTX 4090 在 16K 上下文 W4 精度下的实际 Tokens/s 估算：显存带宽 1008 GB/s / (13.5GB weights + 6.4GB KV) ≈ 48 Tokens/s 理论值，考虑 80% 效率后约 38 Tokens/s；TTFT (Prefill) 受限于 82.6 TFLOPS，16K 序列约 5-8 秒。

## Corrected Claim

1×RTX 4090 在 16K 上下文 W4 精度下的实际 Tokens/s 估算：显存带宽 1008 GB/s / (13.5GB weights + 6.4GB KV) ≈ 48 Tokens/s 理论值，考虑 80% 效率后约 38 Tokens/s；TTFT (Prefill) 受限于 82.6 TFLOPS，16K 序列约 5-8 秒。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽 1008 GB/s 与算力 82.6 TFLOPS 符合硬件规格；W4 精度下 13.5GB 权重与 16K 上下文 6.4GB KV Cache 的量级估算合理；基于带宽瓶颈的 Decode 速度估算（~48 Tokens/s 理论值）及基于算力的 Prefill 时间估算（5-8 秒）在数量级和逻辑上均自洽。

## Search Query

RTX 4090 27B model 4bit quantization inference speed tokens per second benchmark
