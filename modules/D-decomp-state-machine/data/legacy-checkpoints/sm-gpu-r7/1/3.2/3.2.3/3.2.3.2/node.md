# N143: INT8 量化精度下 32K 上下文 KV Cache 大小 = 2 * 64 * 4 * 128 * 32768 * 1 byte = 2,147,483,6

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

INT8 量化精度下 32K 上下文 KV Cache 大小 = 2 * 64 * 4 * 128 * 32768 * 1 byte = 2,147,483,648 bytes ≈ 2.0 GB，相比 BF16 减少 50%，显著降低显存占用

## Corrected Claim

INT8 量化精度下 32K 上下文 KV Cache 大小 = 2 * 64 * 4 * 128 * 32768 * 1 byte = 2,147,483,648 bytes ≈ 2.0 GB，相比 BF16 减少 50%，显著降低显存占用

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * 64 * 4 * 128 * 32768 * 1 计算结果为 2,147,483,648 bytes，即 2 GiB（约 2.0 GB），且 INT8 相比 BF16 减少 50% 符合量化原理。
