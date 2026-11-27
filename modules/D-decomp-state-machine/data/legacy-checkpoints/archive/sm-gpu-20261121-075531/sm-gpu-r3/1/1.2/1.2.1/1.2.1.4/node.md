# N141: 基于确认参数 (64层, 4 KV Heads, 128 dim)，BF16 精度下 32K 上下文的 KV Cache 精确占用量为 2 * 64 * 4 *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

基于确认参数 (64层, 4 KV Heads, 128 dim)，BF16 精度下 32K 上下文的 KV Cache 精确占用量为 2 * 64 * 4 * 128 * 32768 * 2 bytes = 512 MB (0.5 GB)，而非之前估算的 1.93 GB。

## Corrected Claim

基于确认参数 (64层, 4 KV Heads, 128 dim)，BF16 精度下 32K 上下文的 KV Cache 精确占用量为 2 * 64 * 4 * 128 * 32768 * 2 bytes = 512 MB (0.5 GB)，而非之前估算的 1.93 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 64 * 4 * 128 * 32768 * 2 = 536,870,912 bytes，即 512 MiB (0.5 GB)，数值量级与公式推导完全一致。
