# N716: FP8 精度下 KV Cache per token = 2 * 64 * 8 * 128 * 1 byte = 128 KB（基于 L=64 修正），32K 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N256

## Claim

FP8 精度下 KV Cache per token = 2 * 64 * 8 * 128 * 1 byte = 128 KB（基于 L=64 修正），32K 上下文总 KV Cache = 128 KB * 32768 = 4 GB，修正 N256 中基于 L=32 计算的 2.15 GB 错误值。

## Corrected Claim

FP8 精度下 KV Cache per token = 2 * 64 * 8 * 128 * 1 byte = 128 KB（基于 L=64 修正），32K 上下文总 KV Cache = 128 KB * 32768 = 4 GB，修正 N256 中基于 L=32 计算的 2.15 GB 错误值。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 64 * 8 * 128 * 1 = 131,072 bytes = 128 KB，128 KB * 32768 = 4 GB，数值量级与算术逻辑均自洽。
