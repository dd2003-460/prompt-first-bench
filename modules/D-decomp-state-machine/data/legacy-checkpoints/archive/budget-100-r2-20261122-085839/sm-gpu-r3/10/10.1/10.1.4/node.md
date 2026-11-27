# N300: 2× RTX 3090 方案在 W4 量化下，若 KV Cache 为 BF16，总显存需求 = 13.55 GB (Weights) + 62.91 GB (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110, N111, N112

## Claim

2× RTX 3090 方案在 W4 量化下，若 KV Cache 为 BF16，总显存需求 = 13.55 GB (Weights) + 62.91 GB (KV Cache) + 1.02 GB (Overhead) = 77.48 GB，远大于 48 GB 容量，方案不可行

## Corrected Claim

2× RTX 3090 方案在 W4 量化下，若 KV Cache 为 BF16，总显存需求 = 13.55 GB (Weights) + 62.91 GB (KV Cache) + 1.02 GB (Overhead) = 77.48 GB，远大于 48 GB 容量，方案不可行

## Evidence

先验知识/题面给定，逻辑校验通过：2x RTX 3090 总显存为 48GB，计算得出的 77.48GB 需求远超容量，结论成立。
