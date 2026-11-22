# N155: Mac Studio M2 Ultra 的统一内存带宽为 800 GB/s，运行 Qwen3-27B (BF16) 时的理论最大解码吞吐量上限约为 800 / 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N44

## Claim

Mac Studio M2 Ultra 的统一内存带宽为 800 GB/s，运行 Qwen3-27B (BF16) 时的理论最大解码吞吐量上限约为 800 / 54 ≈ 14.8 tokens/s（假设权重完全加载且无计算瓶颈，实际受CPU/GPU协同调度影响）。

## Corrected Claim

Mac Studio M2 Ultra 的统一内存带宽为 800 GB/s，运行 Qwen3-27B (BF16) 时的理论最大解码吞吐量上限约为 800 / 54 ≈ 14.8 tokens/s（假设权重完全加载且无计算瓶颈，实际受CPU/GPU协同调度影响）。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 统一内存带宽确为 800 GB/s，Qwen3-27B BF16 权重约 54 GB，理论带宽上限计算 800/54 ≈ 14.8 tokens/s 符合算术逻辑。
