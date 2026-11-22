# N391: Qwen3-27B 的 hidden_dim 确切数值为 4096，来源为 HuggingFace 官方模型卡 config.json，用于通信量公式的维度乘数

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N139, N140, N141

## Claim

Qwen3-27B 的 hidden_dim 确切数值为 4096，来源为 HuggingFace 官方模型卡 config.json，用于通信量公式的维度乘数。

## Corrected Claim

Qwen3-27B 的 hidden_dim 数值需以 HuggingFace 官方模型卡 config.json 为准，通常量级在 3000-5000 之间，用于通信量公式的维度乘数。

## Evidence

[质询]具体数值（4096）属于经验事实/模型配置参数，无法从第一性原理推导，且当前无可用来源直接证实该特定版本的 hidden_dim 确为 4096（不同变体或版本可能存在差异，如 3584 或 5120 等常见维度）。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法验证具体数值）

## Search Query

Qwen3-27B config.json hidden_size
