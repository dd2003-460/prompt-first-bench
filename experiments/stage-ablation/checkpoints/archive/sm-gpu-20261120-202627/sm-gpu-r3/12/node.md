# N150: 候选硬件筛选的显存容量下限阈值：基于 32K 上下文 + BF16/FP8 精度需求，单卡显存必须 ≥ 48GB (FP8) 或 ≥ 80GB (BF16)，或

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应计算基础（KV Cache）、阈值推导（总显存需求）和最终筛选结果（硬件清单），逻辑链条清晰且互不重叠，无矛盾或冗余。）
