# N149: NVIDIA L40S 显存带宽为 864 GB/s（HBM2e），运行 Qwen3-27B (FP8/INT8) 时的理论最大解码吞吐量上限约为 864 / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

NVIDIA L40S 显存带宽为 864 GB/s（HBM2e），运行 Qwen3-27B (FP8/INT8) 时的理论最大解码吞吐量上限约为 864 / 27 ≈ 32 tokens/s（假设权重完全加载且无KV Cache瓶颈，实际需扣除KV Cache占用后的可用带宽）。

## Corrected Claim

NVIDIA L40S 显存带宽为 864 GB/s（HBM2e），运行 Qwen3-27B (FP8/INT8) 时的理论最大解码吞吐量上限约为 864 / 27 ≈ 32 tokens/s（假设权重完全加载且无KV Cache瓶颈，实际需扣除KV Cache占用后的可用带宽）。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA L40S 显存带宽确为 864 GB/s，Qwen3-27B 参数量约 27B，FP8/INT8 下权重体积约 27GB，理论带宽上限 864/27 ≈ 32 tokens/s 符合算术逻辑。
