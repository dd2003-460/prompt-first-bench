# N43: 不同上下文长度下的 KV Cache 显存占用：4K=16 MB, 8K=32 MB, 16K=64 MB, 32K=128 MB, 64K=256 MB (单

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

不同上下文长度下的 KV Cache 显存占用：4K=16 MB, 8K=32 MB, 16K=64 MB, 32K=128 MB, 64K=256 MB (单序列 BF16)

## Corrected Claim

不同上下文长度下的 KV Cache 显存占用：4K=16 MB, 8K=32 MB, 16K=64 MB, 32K=128 MB, 64K=256 MB (单序列 BF16)

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 显存占用与上下文长度呈线性关系，数值量级符合 BF16 精度下典型大语言模型（如 7B-13B 参数规模）的单序列缓存估算。
