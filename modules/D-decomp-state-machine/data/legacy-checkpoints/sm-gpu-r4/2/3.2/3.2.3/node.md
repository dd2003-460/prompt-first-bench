# N40: BF16 精度下 32K 上下文 KV Cache 大小：2 * 64 * 4 * 128 * 32768 * 2 bytes = 4,294,967,296 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N6

## Claim

BF16 精度下 32K 上下文 KV Cache 大小：2 * 64 * 4 * 128 * 32768 * 2 bytes = 4,294,967,296 bytes ≈ 4 GB（注意：原计算 1.25 GB 可能遗漏了 K/V 双份或层数/头数错误）

## Corrected Claim

BF16 精度下 32K 上下文 KV Cache 大小：2 * 64 * 4 * 128 * 32768 * 2 bytes = 4,294,967,296 bytes ≈ 4 GB（注意：原计算 1.25 GB 可能遗漏了 K/V 双份或层数/头数错误）

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2(K/V) * 64(层) * 4(头) * 128(维) * 32768(长) * 2(BF16字节) = 4,294,967,296 bytes ≈ 4 GB，计算无误且量级合理。
