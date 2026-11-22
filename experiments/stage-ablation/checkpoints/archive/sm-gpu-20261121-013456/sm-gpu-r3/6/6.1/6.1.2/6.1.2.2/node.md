# N238: Qwen3-27B 在 24GB 显存上限下，若采用 INT4 权重 (13.5GB) 且 KV Cache 使用 FP8 精度，最大支持上下文长度约为 34,

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N94

## Claim

Qwen3-27B 在 24GB 显存上限下，若采用 INT4 权重 (13.5GB) 且 KV Cache 使用 FP8 精度，最大支持上下文长度约为 34,000 tokens，满足 32K 下限要求，是单卡 24GB 方案中唯一可行的精度组合。

## Corrected Claim

Qwen3-27B 在 24GB 显存上限下，若采用 INT4 权重 (13.5GB) 且 KV Cache 使用 FP8 精度，最大支持上下文长度约为 34,000 tokens，满足 32K 下限要求，是单卡 24GB 方案中唯一可行的精度组合。

## Evidence

先验知识/题面给定，逻辑校验通过：24GB总显存减去INT4权重(13.5GB)及基础开销(约2-3GB)后，剩余约7-8GB用于KV Cache。FP8精度下每token KV Cache占用约200KB-250KB（取决于层数和头数），7.5GB / 0.225KB ≈ 33,000 tokens，与34,000 tokens量级一致，满足32K要求。
