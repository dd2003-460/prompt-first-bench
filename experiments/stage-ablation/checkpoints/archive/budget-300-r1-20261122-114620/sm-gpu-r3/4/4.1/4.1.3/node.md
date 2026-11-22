# N103: RTX 4090 (24GB) 单卡方案总硬件成本 C_single_4090 为 $1900-$2050，计算公式为 P_gpu_4090 ($1600) +

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

RTX 4090 (24GB) 单卡方案总硬件成本 C_single_4090 为 $1900-$2050，计算公式为 P_gpu_4090 ($1600) + C_infra_4090 ($300-$450)，注意 RTX 4090 显存仅 24GB，无法容纳 BF16 权重的 54GB，因此该节点实际指向的是量化后或不可行状态，需修正为 RTX 3090 或 A100 对比

## Corrected Claim

RTX 4090 (24GB) 单卡方案总硬件成本 C_single_4090 为 $1900-$2050，计算公式为 P_gpu_4090 ($1600) + C_infra_4090 ($300-$450)，注意 RTX 4090 显存仅 24GB，无法容纳 BF16 权重的 54GB，因此该节点实际指向的是量化后或不可行状态，需修正为 RTX 3090 或 A100 对比

## Evidence

父节点级核验未通过：不完备（子节点在逻辑上是正交的（分别讨论可行性边界、不可行证明和TCO对比），且无冗余。但完备性存在缺陷：父节点核心结论指出“无法容纳BF16权重需修正为对比”，而子节点仅分析了W4和INT8，完全缺失了对BF16（原生精度）不可行性的直接验证，也未包含父节点建议的“RTX 3090或A100对比”中的A100方案，导致未完全覆盖父节点指出的关键修正方向。）

## Search Query

RTX 4090 24GB vs Qwen3 27B BF16 memory requirement feasibility
