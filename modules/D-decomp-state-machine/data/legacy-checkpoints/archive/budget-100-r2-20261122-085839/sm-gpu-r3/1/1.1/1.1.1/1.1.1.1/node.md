# N121: Qwen3-27B 模型配置文件中 total_params 的精确数值（从 Hugging Face config.json 或 model_card 获取，

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N32

## Claim

Qwen3-27B 模型配置文件中 total_params 的精确数值（从 Hugging Face config.json 或 model_card 获取，通常精确到亿位，如 27.15B 或 27.2B），用于替代估算值 27.1B 以消除权重存储计算的基数误差。

## Corrected Claim

Qwen3-27B 模型配置文件中 total_params 的精确数值需从 Hugging Face config.json 或 model_card 获取，通常约为 27.1B 至 27.2B 之间，用于替代估算值以消除权重存储计算的基数误差。

## Evidence

[质询]具体数值（如27.15B vs 27.2B）属于经验事实，且无来源支持，无法确认精确到小数点后两位的准确值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B Hugging Face config.json total_params
