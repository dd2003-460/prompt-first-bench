# N192: Qwen3-27B 的 MoE 稀疏激活比例（Sparsity Ratio）为 12.1%（计算式: 3.3B 激活参数 / 27.18B 总参数），这意味着在

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N59

## Claim

Qwen3-27B 的 MoE 稀疏激活比例（Sparsity Ratio）为 12.1%（计算式: 3.3B 激活参数 / 27.18B 总参数），这意味着在 BF16 下，每生成一个 token 实际仅需读取 6.6GB 权重数据，而非 54.36GB，该比例是计算有效带宽需求的唯一关键变量。

## Corrected Claim

Qwen3-27B 的 MoE 稀疏激活比例（Sparsity Ratio）为 12.1%（计算式: 3.3B 激活参数 / 27.18B 总参数），这意味着在 BF16 下，每生成一个 token 实际仅需读取 6.6GB 权重数据，而非 54.36GB，该比例是计算有效带宽需求的唯一关键变量。

## Evidence

先验知识/题面给定，逻辑校验通过：3.3/27.18≈12.1%，27.18B*2bytes≈54.36GB，3.3B*2bytes≈6.6GB，计算自洽且符合MoE稀疏激活原理。
