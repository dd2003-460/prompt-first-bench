# N176: Qwen3-27B 的总参数量精确值为 27.3B (27,300,000,000)，此数值已包含 Embedding 层和 LM Head，无需额外增加 1-

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

Qwen3-27B 的总参数量精确值为 27.3B (27,300,000,000)，此数值已包含 Embedding 层和 LM Head，无需额外增加 1-2 GB 显存估算；来源为 Hugging Face 模型卡或官方 GitHub 仓库 config.json 中的 num_parameters 字段。

## Corrected Claim

Qwen3-27B 的总参数量约为 27.3B，通常包含 Embedding 层和 LM Head，具体精确值需以官方 config.json 为准。

## Evidence

[质询]具体参数量数值（27.3B）及是否包含 Embedding/LM Head 属于经验事实，且不同模型架构或版本可能存在细微差异，缺乏来源直接证实该精确数值及包含关系。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B huggingface config.json num_parameters exact value
