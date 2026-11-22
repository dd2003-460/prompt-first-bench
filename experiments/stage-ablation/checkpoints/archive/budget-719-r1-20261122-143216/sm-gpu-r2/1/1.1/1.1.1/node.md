# N36: Qwen3-27B 的精确参数量（billions）需从 Hugging Face 模型卡或 config.json 的 hidden_size/interme

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

Qwen3-27B 的精确参数量（billions）需从 Hugging Face 模型卡或 config.json 的 hidden_size/intermediate_size/num_layers 推导，以验证 27B 是否为近似值（如 27.2B 或 26.8B），直接影响权重 GB 数计算精度（误差 < 2%）。

## Corrected Claim

Qwen3-27B 的精确参数量需从 Hugging Face 模型卡或 config.json 推导以验证 27B 是否为近似值，进而影响权重 GB 数计算精度。

## Evidence

[质询]该陈述包含具体的经验性数值断言（如误差<2%、具体参数量范围），属于经验事实，无法仅从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B exact parameter count config.json hidden_size num_layers
