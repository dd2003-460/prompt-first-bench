# N91: NVIDIA A100 80GB (PCIe) 的显存带宽为 2039 GB/s，Qwen3-27B FP8 权重 27GB，理论最大解码吞吐量为 2039 /

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

NVIDIA A100 80GB (PCIe) 的显存带宽为 2039 GB/s，Qwen3-27B FP8 权重 27GB，理论最大解码吞吐量为 2039 / 27 ≈ 75.5 tokens/s（假设无其他瓶颈）。

## Corrected Claim

NVIDIA A100 80GB (PCIe) 的显存带宽为 2039 GB/s，Qwen3-27B FP8 权重 27GB，理论最大解码吞吐量为 2039 / 27 ≈ 75.5 tokens/s（假设无其他瓶颈）。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB PCIe 显存带宽确为 2039 GB/s，Qwen3-27B FP8 权重约 27GB，算术推导 2039/27 ≈ 75.5 tokens/s 正确，符合内存带宽瓶颈下的理论最大解码吞吐量计算逻辑。
