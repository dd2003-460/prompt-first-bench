# N140: Perplexity (困惑度) 基准测试的量化计算定义：PPL = exp(Σ(-log p(token_i)) / N_tokens)，在 WikiText

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

Perplexity (困惑度) 基准测试的量化计算定义：PPL = exp(Σ(-log p(token_i)) / N_tokens)，在 WikiText-2 数据集上计算，数值越低表示语言建模能力越强；量化后 PPL 增加量 ΔPPL = PPL_quantized - PPL_BF16。

## Corrected Claim

Perplexity (困惑度) 基准测试的量化计算定义：PPL = exp(Σ(-log p(token_i)) / N_tokens)，在 WikiText-2 数据集上计算，数值越低表示语言建模能力越强；量化后 PPL 增加量 ΔPPL = PPL_quantized - PPL_BF16。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

Perplexity calculation formula WikiText-2 HuggingFace evaluate
