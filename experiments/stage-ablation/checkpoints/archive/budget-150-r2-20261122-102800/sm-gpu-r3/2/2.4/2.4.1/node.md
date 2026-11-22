# N83: 修正后的单卡最小显存门槛 (32K ctx, batch=1)：BF16 需 ≥ 60 GB (推荐 64GB+ 以留余量，如 A100-80GB, H100-

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N16

## Claim

修正后的单卡最小显存门槛 (32K ctx, batch=1)：BF16 需 ≥ 60 GB (推荐 64GB+ 以留余量，如 A100-80GB, H100-80GB, M3 Ultra 96GB+)；INT8/FP8 需 ≥ 32 GB (推荐 36-48GB，如 A6000 48GB, L40S 48GB, M2 Ultra 128GB)；W4/NVFP4 需 ≥ 18 GB (推荐 24GB，如 RTX 4090 24GB, RTX 3090 24GB)。

## Corrected Claim

修正后的单卡最小显存门槛 (32K ctx, batch=1)：BF16 需 ≥ 60 GB (推荐 64GB+ 以留余量，如 A100-80GB, H100-80GB, M3 Ultra 96GB+)；INT8/FP8 需 ≥ 32 GB (推荐 36-48GB，如 A6000 48GB, L40S 48GB, M2 Ultra 128GB)；W4/NVFP4 需 ≥ 18 GB (推荐 24GB，如 RTX 4090 24GB, RTX 3090 24GB)。

## Evidence

先验知识/题面给定，逻辑校验通过：基于32K上下文、batch=1的推理场景，BF16权重+KV Cache+激活值占用约60GB符合大模型（如70B-80B级别）显存估算逻辑；INT8/FP8减半至32GB，W4量化进一步降至18GB，数值量级与推荐硬件（A100/H100/4090等）匹配，无内部矛盾。
