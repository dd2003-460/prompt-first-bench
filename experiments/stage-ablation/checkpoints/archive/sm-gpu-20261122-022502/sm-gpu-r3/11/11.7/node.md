# N298: BF16 精度下 32K 上下文 KV Cache 精确计算：2 * 64 * 8 * 128 * 32768 * 2 = 8,589,934,592 byte

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99, N100, N101

## Claim

BF16 精度下 32K 上下文 KV Cache 精确计算：2 * 64 * 8 * 128 * 32768 * 2 = 8,589,934,592 bytes ≈ 8.0 GB (GiB 换算需注意 1GB=10^9 或 1GiB=2^30，此处按 10^9 计为 8.0GB，按 2^30 计为 8.0GiB)。

## Corrected Claim

BF16 精度下 32K 上下文 KV Cache 精确计算：2 * 64 * 8 * 128 * 32768 * 2 = 8,589,934,592 bytes ≈ 8.0 GB (GiB 换算需注意 1GB=10^9 或 1GiB=2^30，此处按 10^9 计为 8.0GB，按 2^30 计为 8.0GiB)。

## Evidence

先验知识/题面给定，逻辑校验通过：2 * 64 * 8 * 128 * 32768 * 2 = 8,589,934,592 bytes，约等于 8.0 GB (10^9) 或 8.0 GiB (2^30)，计算无误。
