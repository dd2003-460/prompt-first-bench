# N350: Qwen3-27B 的有效注意力层数 L_eff 具体数值需查阅模型 config.json 或 HuggingFace 模型卡确认；若采用混合架构，L_eff

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N124

## Claim

Qwen3-27B 的有效注意力层数 L_eff 具体数值需查阅模型 config.json 或 HuggingFace 模型卡确认；若采用混合架构，L_eff 仅为标准 MHA 层数，不含线性注意力层，导致 N124 公式计算出的 KV Cache 仅为总激活内存的一部分。

## Corrected Claim

Qwen3-27B 的有效注意力层数 L_eff 需查阅官方模型配置确认；若该模型采用混合注意力架构，L_eff 仅指代标准 MHA 层数，此时基于 L_eff 计算的 KV Cache 仅为总激活内存的一部分。

## Evidence

[质询]Qwen3-27B 的具体架构细节（是否采用混合注意力、具体层数分布）属于经验事实，且当前检索无可用来源，无法确认其是否真的采用了混合架构或 L_eff 的具体定义方式。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B config.json num_hidden_layers num_key_value_heads architecture hybrid attention
