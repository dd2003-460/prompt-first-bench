# N81: NVIDIA A100 80GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/seq) + Ove

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

NVIDIA A100 80GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/seq) + Overhead (2GB) ≈ 56.1GB < 80GB，显存可行，支持多并发。

## Corrected Claim

NVIDIA A100 80GB 单卡运行 Qwen3-27B 的显存可行性：BF16 权重 54GB + KV Cache (128MB/seq) + Overhead (2GB) ≈ 56.1GB < 80GB，显存可行，支持多并发。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重约54GB，加上KV Cache和Overhead后总显存占用约56.1GB，小于A100 80GB显存，计算自洽。
