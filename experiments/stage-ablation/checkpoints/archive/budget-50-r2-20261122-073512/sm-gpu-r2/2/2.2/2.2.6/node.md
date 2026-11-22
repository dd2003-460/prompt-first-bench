# N86: NVIDIA H100 80GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/seq) + Ove

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

NVIDIA H100 80GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/seq) + Overhead (2GB) ≈ 56.1GB < 80GB，显存可行，支持多并发。

## Corrected Claim

NVIDIA H100 80GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/seq) + Overhead (2GB) ≈ 56.1GB < 80GB，显存可行，支持多并发。

## Evidence

[质询]KV Cache 128MB/seq 的估算可能偏低（取决于上下文长度和并发数），但作为单卡可行性下限估算，逻辑上未导致总显存超过80GB，不构成硬伤。 | 先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，加上少量KV Cache和Overhead，总显存占用约56GB，小于H100 80GB显存，计算自洽。
