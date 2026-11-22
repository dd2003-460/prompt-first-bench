# N429: Qwen3-27B的num_attention_heads和num_key_value_heads具体数值需从HuggingFace官方config.json中

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N138

## Claim

Qwen3-27B的num_attention_heads和num_key_value_heads具体数值需从HuggingFace官方config.json中提取，预期num_attention_heads约为32，num_key_value_heads约为8（GQA 4:1比例），该值直接决定KV Cache每层的head数和通信量。

## Corrected Claim

Qwen3-27B的num_attention_heads和num_key_value_heads具体数值需从HuggingFace官方config.json中提取，预期采用GQA机制（如4:1比例），该值直接决定KV Cache每层的head数和通信量。

## Evidence

[质询]具体数值（32/8）属于经验事实，且无来源支持，存在与官方配置不符的风险（例如实际可能是64/8或其他比例）。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B config.json num_attention_heads num_key_value_heads
