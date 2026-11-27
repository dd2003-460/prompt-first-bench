# N55: NVFP4/W4 精度下 Qwen3-27B 的总显存需求为 14.5GB (平均权重含开销) + 2.15GB (KV Cache) + 1.5GB (平均 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

NVFP4/W4 精度下 Qwen3-27B 的总显存需求为 14.5GB (平均权重含开销) + 2.15GB (KV Cache) + 1.5GB (平均 Overhead) = 18.15GB，因此候选硬件显存必须 ≥20GB 以留出安全余量 [knowledge: 基于 N44, N49/N50 和 N51 计算]

## Corrected Claim

NVFP4/W4 精度下 Qwen3-27B 的总显存需求为 14.5GB (平均权重含开销) + 2.15GB (KV Cache) + 1.5GB (平均 Overhead) = 18.15GB，因此候选硬件显存必须 ≥20GB 以留出安全余量 [knowledge: 基于 N44, N49/N50 和 N51 计算]

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在NVFP4(4bit)下权重约13.5GB，加上KV Cache和Overhead，总显存18.15GB量级合理，且20GB为合理的安全余量阈值。
