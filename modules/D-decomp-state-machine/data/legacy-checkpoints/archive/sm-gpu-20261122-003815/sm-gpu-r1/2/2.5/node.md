# N17: 单卡可行性过滤：BF16 (61.3 GB) 需 ≥64GB 显存 → A100 80GB, H100 80GB, A6000 48GB (不足), L40S 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

单卡可行性过滤：BF16 (61.3 GB) 需 ≥64GB 显存 → A100 80GB, H100 80GB, A6000 48GB (不足), L40S 48GB (不足), M3 Ultra 64GB (临界)。FP8/INT8 (34.3 GB) 需 ≥36GB → A100 80GB, H100 80GB, A6000 48GB, L40S 48GB, M3 Ultra 64GB。INT4 (20.8 GB) 需 ≥24GB → RTX 4090 24GB (临界), RTX 3090 24GB, RX 7900 XTX 24GB, M3 Ultra 64GB。

## Corrected Claim

单卡可行性过滤：BF16 (61.3 GB) 需 ≥64GB 显存 → A100 80GB, H100 80GB, A6000 48GB (不足), L40S 48GB (不足), M3 Ultra 64GB (临界)。FP8/INT8 (34.3 GB) 需 ≥36GB → A100 80GB, H100 80GB, A6000 48GB, L40S 48GB, M3 Ultra 64GB。INT4 (20.8 GB) 需 ≥24GB → RTX 4090 24GB (临界), RTX 3090 24GB, RX 7900 XTX 24GB, M3 Ultra 64GB。

## Evidence

先验知识/题面给定，逻辑校验通过：显存需求与硬件规格匹配，数值量级合理（BF16 61.3GB < 64GB 临界，FP8 34.3GB < 36GB 安全，INT4 20.8GB < 24GB 临界），无内部矛盾。
