# N299: FP8 精度下 32K 上下文 KV Cache 精确计算：2 * 64 * 8 * 128 * 32768 * 1 = 4,294,967,296 bytes

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99, N100, N101

## Claim

FP8 精度下 32K 上下文 KV Cache 精确计算：2 * 64 * 8 * 128 * 32768 * 1 = 4,294,967,296 bytes ≈ 4.0 GB，相比 BF16 节省 4.0 GB 显存。

## Corrected Claim

FP8 精度下 32K 上下文 KV Cache 精确计算：2 * 64 * 8 * 128 * 32768 * 1 = 4,294,967,296 bytes ≈ 4.0 GB，相比 BF16 节省 4.0 GB 显存。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8为8位（1字节），BF16为16位（2字节）。计算式 2 * 64 * 8 * 128 * 32768 * 1 中，2代表K和V，64为层数，8为KV头数，128为头维度，32768为序列长度，1为FP8字节数。乘积为 4,294,967,296 bytes，即 4 GiB (4.0 GB)。相比BF16（字节数为2），节省的显存即为FP8占用的全部显存 4.0 GB。数值量级与逻辑均正确。
