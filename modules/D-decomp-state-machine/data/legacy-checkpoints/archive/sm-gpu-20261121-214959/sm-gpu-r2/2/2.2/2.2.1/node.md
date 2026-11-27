# N57: NVIDIA H100 SXM5 单卡运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

NVIDIA H100 SXM5 单卡运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用为 66.58GB，小于 80GB 容量，剩余 13.42GB 用于激活值；理论 Decode 吞吐上限 = 2039 GB/s / 54 GB ≈ 37.76 tokens/s。

## Corrected Claim

NVIDIA H100 SXM5 单卡运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用为 66.58GB，小于 80GB 容量，剩余 13.42GB 用于激活值；理论 Decode 吞吐上限 = 2039 GB/s / 54 GB ≈ 37.76 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM5 显存 80GB 及带宽 2039GB/s 为已知规格，54GB+12.58GB=66.58GB 计算正确，剩余 13.42GB 合理，吞吐估算符合算术强度逻辑。
