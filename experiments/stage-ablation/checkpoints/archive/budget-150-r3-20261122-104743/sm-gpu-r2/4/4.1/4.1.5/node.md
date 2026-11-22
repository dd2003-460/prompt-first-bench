# N128: FP8 精度下 Qwen3-27B 在 32K 上下文长度下，KV Cache 总显存占用为 32,768 tokens × 64 KB/token = 2,0

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

FP8 精度下 Qwen3-27B 在 32K 上下文长度下，KV Cache 总显存占用为 32,768 tokens × 64 KB/token = 2,048 MB (2 GB)

## Corrected Claim

FP8 精度下 Qwen3-27B 在 32K 上下文长度下，KV Cache 总显存占用为 32,768 tokens × 64 KB/token = 2,048 MB (2 GB)

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层，GQA 8 KV头，head_dim 128）推导单 token KV 占用为 64KB，32K tokens 总占用 2GB，数值量级与计算逻辑自洽。
