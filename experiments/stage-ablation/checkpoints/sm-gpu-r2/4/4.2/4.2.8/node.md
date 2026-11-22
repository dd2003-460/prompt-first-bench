# N92: NVIDIA H100 80GB (SXM) 的显存带宽为 3350 GB/s，Qwen3-27B FP8 权重 27GB，理论最大解码吞吐量为 3350 / 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

NVIDIA H100 80GB (SXM) 的显存带宽为 3350 GB/s，Qwen3-27B FP8 权重 27GB，理论最大解码吞吐量为 3350 / 27 ≈ 124.1 tokens/s（假设无其他瓶颈）。

## Corrected Claim

NVIDIA H100 80GB (SXM) 的显存带宽为 3350 GB/s，Qwen3-27B FP8 权重 27GB，理论最大解码吞吐量为 3350 / 27 ≈ 124.1 tokens/s（假设无其他瓶颈）。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM 80GB 显存带宽确为 3.35 TB/s (3350 GB/s)，Qwen3-27B FP8 权重约 27GB，算术推导 3350/27 ≈ 124.1 正确，符合单卡解码带宽瓶颈理论。
