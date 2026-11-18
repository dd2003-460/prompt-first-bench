# N137: Qwen3-27B 的 num_key_value_heads 参数值为 4，需从 Hugging Face 官方 config.json 或 Model Ca

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N38

## Claim

Qwen3-27B 的 num_key_value_heads 参数值为 4，需从 Hugging Face 官方 config.json 或 Model Card 确认，以验证 N38 中 H_kv=4 的假设

## Corrected Claim

Qwen3-27B 的 num_key_value_heads 参数值需从 Hugging Face 官方 config.json 或 Model Card 确认，以验证 N38 中 H_kv=4 的假设

## Evidence

[质询]参考来源与事实主题完全无关，无法提供外部证据支持该具体参数值。 | 经验事实，逻辑自洽但缺来源支持（来源[1]为物理材料学论文，与LLM架构参数无关）

## Search Query

Qwen3-27B config.json num_key_value_heads 4

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/1303.4033v1', 'type': 'arxiv', 'title': 'Two-dimensional magnetic interactions in LaFeAsO'}
