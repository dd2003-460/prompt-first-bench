# N655: L40S 在 Qwen3-27B BF16 精度下的理论 Decode 吞吐量上限 = 864 GB/s / (54 GB 权重 + 8 GB KV Cache

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N233

## Claim

L40S 在 Qwen3-27B BF16 精度下的理论 Decode 吞吐量上限 = 864 GB/s / (54 GB 权重 + 8 GB KV Cache) ≈ 13.8 tokens/s；实测需乘以 0.6-0.8 效率系数，预计为 8.3-11.0 tokens/s，此数值直接决定其单位 token 成本的分母。

## Corrected Claim

L40S 在 Qwen3-27B BF16 精度下的理论 Decode 吞吐量上限 = 864 GB/s / (54 GB 权重 + 8 GB KV Cache) ≈ 13.8 tokens/s；实测需乘以 0.6-0.8 效率系数，预计为 8.3-11.0 tokens/s，此数值直接决定其单位 token 成本的分母。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，L40S显存带宽864GB/s，理论吞吐计算864/(54+8)≈13.8 tokens/s符合算术逻辑，效率系数0.6-0.8符合工程经验。
