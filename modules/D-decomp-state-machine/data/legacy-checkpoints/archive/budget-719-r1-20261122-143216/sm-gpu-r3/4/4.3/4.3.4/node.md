# N109: Qwen3-27B 在 32K 上下文下的总显存占用量（BF16 精度），计算公式为 54 GB (权重) + 10.74 GB (KV Cache) + 1.

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

Qwen3-27B 在 32K 上下文下的总显存占用量（BF16 精度），计算公式为 54 GB (权重) + 10.74 GB (KV Cache) + 1.5 GB (激活值) = 66.24 GB

## Corrected Claim

Qwen3-27B 在 32K 上下文下的总显存占用量（BF16 精度），计算公式为 54 GB (权重) + 10.74 GB (KV Cache) + 1.5 GB (激活值) = 66.24 GB

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，BF16权重约54GB；32K上下文KV Cache约10.74GB（基于GQA/MLA架构估算合理）；激活值1.5GB量级合理；总和66.24GB计算无误。
