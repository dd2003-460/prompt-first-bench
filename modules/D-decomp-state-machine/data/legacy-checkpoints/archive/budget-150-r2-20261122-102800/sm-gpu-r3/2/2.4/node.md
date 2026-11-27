# N16: 单卡最小显存门槛：BF16需≥64 GB单卡（如A100-80GB, H100-80GB, M3 Ultra 96GB+）；FP8/INT8需≥36 GB单卡（

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

单卡最小显存门槛：BF16需≥64 GB单卡（如A100-80GB, H100-80GB, M3 Ultra 96GB+）；FP8/INT8需≥36 GB单卡（如A6000 48GB, L40S 48GB, M2 Ultra 128GB）；NVFP4/W4需≥24 GB单卡（如RTX 4090 24GB, RTX 3090 24GB, A6000 48GB）

## Corrected Claim

单卡最小显存门槛：BF16需≥64 GB单卡（如A100-80GB, H100-80GB, M3 Ultra 96GB+）；FP8/INT8需≥36 GB单卡（如A6000 48GB, L40S 48GB, M2 Ultra 128GB）；NVFP4/W4需≥24 GB单卡（如RTX 4090 24GB, RTX 3090 24GB, A6000 48GB）

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点1侧重于修正后的具体显存数值门槛，子节点2侧重于显存余量（Headroom）对稳定性的影响及具体案例验证，两者维度不同（数值规格 vs 稳定性机制），互不重叠且无矛盾。虽然子节点2包含部分数值，但其核心在于解释‘为什么’需要余量，与子节点1的‘是多少’互补。）

## Search Query

minimum VRAM for 27B LLM inference BF16 FP8 INT8 NVFP4 W4 single GPU
