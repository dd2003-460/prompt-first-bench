# N184: FP8/INT8 总显存下限修正值：基于 N151 (29.1 GB, 含 Embedding BF16) 和 N156 (8.59 GB) 和 N157 (1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

FP8/INT8 总显存下限修正值：基于 N151 (29.1 GB, 含 Embedding BF16) 和 N156 (8.59 GB) 和 N157 (10 GB)，总显存 = 29.1 + 8.59 + 10 = 47.69 GB。此值高于 N43 原始估算的 38.4 GB。意味着单卡 48GB (L40S) 处于临界状态（需极度优化），单卡 24GB (RTX 4090) 不可行，2x RTX 3090 (48GB) 或 1x L40S (48GB) 可能可行，但需验证碎片化影响。

## Corrected Claim

FP8/INT8 总显存下限修正值：基于 N151 (29.1 GB, 含 Embedding BF16) 和 N156 (8.59 GB) 和 N157 (10 GB)，总显存 = 29.1 + 8.59 + 10 = 47.69 GB。此值高于 N43 原始估算的 38.4 GB。意味着单卡 48GB (L40S) 处于临界状态（需极度优化），单卡 24GB (RTX 4090) 不可行，2x RTX 3090 (48GB) 或 1x L40S (48GB) 可能可行，但需验证碎片化影响。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 29.1 + 8.59 + 10 = 47.69 正确，且 47.69 > 38.4 符合逻辑，硬件容量对比（48GB vs 47.69GB）量级合理。

## Search Query

48GB GPU LLM inference memory fragmentation limit
