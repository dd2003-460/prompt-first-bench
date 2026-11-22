# N172: Qwen3-27B 的 hidden_dim (d_model) 为 4096，该参数是计算激活值显存的基础维度，需从 config.json 确认。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N41

## Claim

Qwen3-27B 的 hidden_dim (d_model) 为 4096，该参数是计算激活值显存的基础维度，需从 config.json 确认。

## Corrected Claim

Qwen3-27B 的 hidden_dim (d_model) 通常为 4096（需从具体版本的 config.json 确认），该参数是计算激活值显存的基础维度。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（hidden_dim=4096），属于经验事实。虽然 Qwen3-27B 的 hidden_dim 确实通常为 4096（基于 Qwen2.5-32B 等类似规模模型的常见配置推断），但缺乏直接来源支持，且不同版本或微调变体可能存在差异，存在口径混淆或版本不匹配的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法直接验证具体数值）

## Search Query

Qwen3-27B config.json hidden_size 4096
