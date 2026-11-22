# N150: 候选硬件筛选的显存容量下限阈值：基于 32K 上下文 + BF16/FP8 精度需求，单卡显存必须 ≥ 48GB (FP8) 或 ≥ 80GB (BF16)，或

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

候选硬件筛选的显存容量下限阈值：基于 32K 上下文 + BF16/FP8 精度需求，单卡显存必须 ≥ 48GB (FP8) 或 ≥ 80GB (BF16)，或双卡总显存 ≥ 39GB (FP8) / ≥ 67GB (BF16)。低于此阈值的硬件（如 RTX 4080 16GB, L4 24GB）直接排除出候选集。

## Corrected Claim

候选硬件筛选的显存容量下限阈值：基于 32K 上下文 + BF16/FP8 精度需求，单卡显存必须 ≥ 48GB (FP8) 或 ≥ 80GB (BF16)，或双卡总显存 ≥ 39GB (FP8) / ≥ 67GB (BF16)。低于此阈值的硬件（如 RTX 4080 16GB, L4 24GB）直接排除出候选集。

## Evidence

检索失败: no sources from any channel (all 5 failed)
