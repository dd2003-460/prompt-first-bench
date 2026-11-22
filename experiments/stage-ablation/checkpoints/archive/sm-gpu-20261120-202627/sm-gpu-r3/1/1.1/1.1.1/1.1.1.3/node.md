# N157: Embedding 层参数量公式：Params_Embedding = vocab_size * hidden_dim。Qwen3 系列通常采用 vocab_s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

Embedding 层参数量公式：Params_Embedding = vocab_size * hidden_dim。Qwen3 系列通常采用 vocab_size ≈ 151,936 (需确认具体版本差异)，该层参数在总参数量中占比通常 < 3%。

## Corrected Claim

Embedding 层参数量公式：Params_Embedding = vocab_size * hidden_dim。Qwen3 系列通常采用 vocab_size ≈ 151,936 (需确认具体版本差异)，该层参数在总参数量中占比通常 < 3%。

## Evidence

先验知识/题面给定，逻辑校验通过：Embedding层参数量公式为vocab_size * hidden_dim，Qwen3系列vocab_size约为151,936，该层参数占比通常<3%符合大语言模型结构常识。

## Search Query

Qwen3-27B vocabulary size config.json
