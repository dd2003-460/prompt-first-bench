# N299: 2× RTX 3090 方案在 W4 量化下，若 KV Cache 为 FP8，总显存需求 = 13.55 GB (Weights) + 31.46 GB (K

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N110, N111, N112

## Claim

2× RTX 3090 方案在 W4 量化下，若 KV Cache 为 FP8，总显存需求 = 13.55 GB (Weights) + 31.46 GB (KV Cache) + 1.02 GB (Overhead) = 46.03 GB，小于 48 GB 容量，方案可行

## Corrected Claim

2× RTX 3090 方案在 W4 量化下，若 KV Cache 为 FP8，总显存需求 = 13.55 GB (Weights) + 31.46 GB (KV Cache) + 1.02 GB (Overhead) = 46.03 GB，小于 48 GB 容量，方案可行

## Evidence

先验知识/题面给定，逻辑校验通过：13.55 + 31.46 + 1.02 = 46.03 GB，且 46.03 < 48，算术与逻辑自洽。
