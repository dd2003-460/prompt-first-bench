# N17: 单卡可行性过滤：BF16 (61.3 GB) 需 ≥64GB 显存 → A100 80GB, H100 80GB, A6000 48GB (不足), L40S 

- **status**: pending
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

父节点级核验未通过：不完备, 有冗余（子节点存在明显的结构冗余，且未完全覆盖父节点中提到的特定硬件（如RTX 3090, RX 7900 XTX）。父节点将M3 Ultra标记为64GB，但子节点3分析的是192GB版本，存在事实不一致。）
