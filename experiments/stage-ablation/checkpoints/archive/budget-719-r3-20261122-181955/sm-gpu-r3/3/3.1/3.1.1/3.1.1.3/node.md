# N267: 基于修正参数的 32K FP8 KV Cache 精确计算式: 2 * 32 * 8 * 128 * 32768 * 1 byte = 2.147 GB，修正 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N89

## Claim

基于修正参数的 32K FP8 KV Cache 精确计算式: 2 * 32 * 8 * 128 * 32768 * 1 byte = 2.147 GB，修正 N89 原估算 16.38 GB 的错误。

## Corrected Claim

基于修正参数的 32K FP8 KV Cache 精确计算式: 2 * 32 * 8 * 128 * 32768 * 1 byte = 2.147 GB，修正 N89 原估算 16.38 GB 的错误。

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 32 * 8 * 128 * 32768 * 1 = 2,147,483,648 bytes = 2.147 GB，计算准确且量纲合理。
