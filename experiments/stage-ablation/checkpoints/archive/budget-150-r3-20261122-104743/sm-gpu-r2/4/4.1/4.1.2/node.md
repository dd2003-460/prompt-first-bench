# N125: Qwen3-27B 在 32K (32,768) 上下文长度下，BF16 精度的 KV Cache 总显存占用为 32,768 tokens × 128 KB/

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

Qwen3-27B 在 32K (32,768) 上下文长度下，BF16 精度的 KV Cache 总显存占用为 32,768 tokens × 128 KB/token = 4,096 MB (4 GB)

## Corrected Claim

Qwen3-27B 在 32K (32,768) 上下文长度下，BF16 精度的 KV Cache 总显存占用为 32,768 tokens × 128 KB/token = 4,096 MB (4 GB)

## Evidence

先验知识/题面给定，逻辑校验通过：32,768 tokens × 128 KB/token = 4,194,304 KB = 4,096 MB = 4 GB，计算无误且量级合理。
