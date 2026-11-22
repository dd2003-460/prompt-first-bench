# N36: Qwen3-27B 在 Hugging Face 官方仓库中记录的精确参数量（total_params）为 27,184,588,288，而非简化的 27e9，

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N7

## Claim

Qwen3-27B 在 Hugging Face 官方仓库中记录的精确参数量（total_params）为 27,184,588,288，而非简化的 27e9，该数值直接决定权重文件大小的分子。

## Corrected Claim

Qwen3-27B 在 Hugging Face 官方仓库中记录的参数量约为 27.18B（具体数值需查阅官方仓库确认），而非简化的 27e9。

## Evidence

[质询]具体参数量数值（27,184,588,288）属于经验事实，无法从第一性原理推导，且缺乏来源直接支持该精确数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B huggingface config.json num_parameters or total_params
