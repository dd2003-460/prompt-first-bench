# N123: 1×RTX 4090 在 16K 上下文 W4 精度下的实际 Tokens/s 估算：显存带宽 1008 GB/s / (13.5GB weights + 6.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N31

## Claim

1×RTX 4090 在 16K 上下文 W4 精度下的实际 Tokens/s 估算：显存带宽 1008 GB/s / (13.5GB weights + 6.4GB KV) ≈ 48 Tokens/s 理论值，考虑 80% 效率后约 38 Tokens/s；TTFT (Prefill) 受限于 82.6 TFLOPS，16K 序列约 5-8 秒。

## Corrected Claim

1×RTX 4090 在 16K 上下文 W4 精度下的实际 Tokens/s 估算：显存带宽 1008 GB/s / (13.5GB weights + 6.4GB KV) ≈ 48 Tokens/s 理论值，考虑 80% 效率后约 38 Tokens/s；TTFT (Prefill) 受限于 82.6 TFLOPS，16K 序列约 5-8 秒。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别针对 Decode 阶段（带宽受限）和 Prefill 阶段（算力受限）进行独立估算，两者在物理机制上正交。覆盖性方面，父节点提到的 16K 上下文、W4 精度、显存带宽、算力峰值及最终性能指标（Tokens/s 和 TTFT）均在子节点中得到了具体拆解和验证。无冗余，因为两者涉及不同的硬件瓶颈（Memory Bandwidth vs Compute FLOPS）和不同的计算阶段。）

## Search Query

RTX 4090 27B model 4bit quantization inference speed tokens per second benchmark
