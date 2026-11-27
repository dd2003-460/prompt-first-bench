# N98: 基于修正后的架构参数（64层, 8 KV heads, head_dim 128），BF16 下 32K tokens 的 KV Cache 总大小为 32,7

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

基于修正后的架构参数（64层, 8 KV heads, head_dim 128），BF16 下 32K tokens 的 KV Cache 总大小为 32,768 * 256 KB = 8,388,608 KB = 8 GB。总显存需求 = 54 GB (Weights) + 8 GB (KV) = 62 GB。

## Corrected Claim

基于修正后的架构参数（64层, 8 KV heads, head_dim 128），BF16 下 32K tokens 的 KV Cache 总大小为 32,768 * 256 KB = 8,388,608 KB = 8 GB。总显存需求 = 54 GB (Weights) + 8 GB (KV) = 62 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 大小计算正确（32768 tokens * 64 layers * 2 (K+V) * 8 heads * 128 dim * 2 bytes = 8,589,934,592 bytes = 8 GB），总显存需求 54GB + 8GB = 62GB 符合算术逻辑。
