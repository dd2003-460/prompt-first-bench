# N60: AMD MI300X 单卡运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用为 66.5

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

AMD MI300X 单卡运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用为 66.58GB，小于 192GB 容量；理论 Decode 吞吐上限 = 5300 GB/s / 54 GB ≈ 98.15 tokens/s。

## Corrected Claim

AMD MI300X 单卡运行 Qwen3-27B BF16 (54GB) + 32K BF16 KV Cache (12.58GB) 的总显存占用为 66.58GB，小于 192GB 容量；理论 Decode 吞吐上限 = 5300 GB/s / 54 GB ≈ 98.15 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：MI300X 显存 192GB 及带宽 5300GB/s 为已知硬件规格，54GB+12.58GB=66.58GB 计算正确且小于 192GB，5300/54≈98.15 计算正确。
