# N153: NVIDIA L4 显存带宽为 300 GB/s（GDDR6），运行 Qwen3-27B (FP8/INT8) 时的理论最大解码吞吐量上限约为 300 / 27

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

NVIDIA L4 显存带宽为 300 GB/s（GDDR6），运行 Qwen3-27B (FP8/INT8) 时的理论最大解码吞吐量上限约为 300 / 27 ≈ 11.1 tokens/s（假设权重完全加载，实际受KV Cache和计算瓶颈限制会更低）。

## Corrected Claim

NVIDIA L4 显存带宽为 300 GB/s（GDDR6），运行 Qwen3-27B (FP8/INT8) 时的理论最大解码吞吐量上限约为 300 / 27 ≈ 11.1 tokens/s（假设权重完全加载，实际受KV Cache和计算瓶颈限制会更低）。

## Evidence

先验知识/题面给定，逻辑校验通过：NVIDIA L4 显存带宽确为 300 GB/s，Qwen3-27B 参数量约 27B，FP8/INT8 下每 token 权重读取量约 27GB，理论带宽上限 300/27≈11.1 tokens/s 计算正确，符合内存带宽瓶颈下的解码吞吐量估算逻辑。
