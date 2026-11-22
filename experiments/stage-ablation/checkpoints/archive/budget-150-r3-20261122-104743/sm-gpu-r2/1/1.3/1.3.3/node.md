# N53: BF16 精度下 Qwen3-27B 的总显存需求为 54GB (权重) + 8.59GB (KV Cache) + 1.5GB (平均 Overhead) =

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

BF16 精度下 Qwen3-27B 的总显存需求为 54GB (权重) + 8.59GB (KV Cache) + 1.5GB (平均 Overhead) = 64.09GB，因此候选硬件显存必须 ≥65GB 以留出安全余量 [knowledge: 基于 N42 和 N51 计算]

## Corrected Claim

BF16 精度下 Qwen3-27B 的总显存需求为 54GB (权重) + 8.59GB (KV Cache) + 1.5GB (平均 Overhead) = 64.09GB，因此候选硬件显存必须 ≥65GB 以留出安全余量 [knowledge: 基于 N42 和 N51 计算]

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在BF16下权重约54GB，KV Cache与Overhead估算合理，总和64.09GB，建议显存≥65GB符合工程安全余量惯例。
