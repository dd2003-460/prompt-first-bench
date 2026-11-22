# N126: Qwen3-27B 在 HuggingFace 官方 config.json 中定义的参数量 (num_parameters) 确认为 27.2B (27,20

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N35

## Claim

Qwen3-27B 在 HuggingFace 官方 config.json 中定义的参数量 (num_parameters) 确认为 27.2B (27,200,000,000)，非 27.0B 或 27.5B，此数值直接决定 BF16 权重显存基线

## Corrected Claim

Qwen3-27B 在 HuggingFace 官方 config.json 中定义的参数量约为 27.2B，此数值直接决定 BF16 权重显存基线

## Evidence

[质询]具体参数量数值（27.2B vs 27.0B/27.5B）属于经验事实，且缺乏来源支持，无法排除实际配置文件中数值略有不同（如27.1B或27.3B）的可能性。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据验证具体数值）

## Search Query

Qwen3-27B huggingface config.json num_parameters
