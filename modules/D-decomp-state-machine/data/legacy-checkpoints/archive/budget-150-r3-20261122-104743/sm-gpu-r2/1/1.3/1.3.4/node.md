# N54: FP8/INT8 精度下 Qwen3-27B 的总显存需求为 27GB (权重) + 4.29GB (KV Cache) + 1.5GB (平均 Overhea

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

FP8/INT8 精度下 Qwen3-27B 的总显存需求为 27GB (权重) + 4.29GB (KV Cache) + 1.5GB (平均 Overhead) = 32.79GB，因此候选硬件显存必须 ≥35GB 以留出安全余量 [knowledge: 基于 N43 和 N51 计算]

## Corrected Claim

FP8/INT8 精度下 Qwen3-27B 的总显存需求为 27GB (权重) + 4.29GB (KV Cache) + 1.5GB (平均 Overhead) = 32.79GB，因此候选硬件显存必须 ≥35GB 以留出安全余量 [knowledge: 基于 N43 和 N51 计算]

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在FP8/INT8下权重约27GB，KV Cache与Overhead估算合理，总和32.79GB，预留余量后要求≥35GB符合工程惯例。
