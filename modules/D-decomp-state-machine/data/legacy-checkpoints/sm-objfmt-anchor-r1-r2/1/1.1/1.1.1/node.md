# N33: Qwen3-27B 采用 GQA (Grouped Query Attention) 架构，具体参数为：num_key_value_heads=4 (或根据最新

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

Qwen3-27B 采用 GQA (Grouped Query Attention) 架构，具体参数为：num_key_value_heads=4 (或根据最新规格确认，通常为 head_dim 的整数倍分组), hidden_size=4096, num_layers=32。

## Corrected Claim

Qwen3-27B 采用 GQA (Grouped Query Attention) 架构，具体参数需查阅官方技术报告或模型配置文件以确认精确数值（如 num_key_value_heads, hidden_size, num_layers 等）。

## Evidence

[质询]具体架构参数（如 num_key_value_heads=4, hidden_size=4096, num_layers=32）属于经验事实，且不同版本或变体可能存在差异，缺乏权威来源直接确认具体数值，存在参数记忆偏差或混淆的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体参数值）

## Search Query

Qwen3-27B config.json num_key_value_heads hidden_size num_layers
