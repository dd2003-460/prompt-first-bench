# N144: FP8 量化精度下 32K 上下文 KV Cache 大小 = 2 * 64 * 4 * 128 * 32768 * 1 byte = 2,147,483,64

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

FP8 量化精度下 32K 上下文 KV Cache 大小 = 2 * 64 * 4 * 128 * 32768 * 1 byte = 2,147,483,648 bytes ≈ 2.0 GB，与 INT8 相同，但需注意 FP8 的动态范围特性对长序列精度影响可能不同

## Corrected Claim

FP8 量化精度下 32K 上下文 KV Cache 大小 = 2 * 64 * 4 * 128 * 32768 * 1 byte = 2,147,483,648 bytes ≈ 2.0 GB，与 INT8 相同，但需注意 FP8 的动态范围特性对长序列精度影响可能不同

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 2 * 64 * 4 * 128 * 32768 * 1 = 2,147,483,648 bytes 正确，且 2^31 bytes 等于 2 GiB，量级与单位换算合理。
