# N128: Qwen3-27B 的 num_hidden_layers 确认为 64 层，而非 32 层或 48 层，此参数线性影响 KV Cache 总大小及 Prefi

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

Qwen3-27B 的 num_hidden_layers 确认为 64 层，而非 32 层或 48 层，此参数线性影响 KV Cache 总大小及 Prefill 计算量

## Corrected Claim

Qwen3-27B 的 num_hidden_layers 通常为 64 层（需具体配置确认），此参数线性影响 KV Cache 总大小及 Prefill 计算量

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（num_hidden_layers=64），属于经验事实。虽然Qwen3-27B确实存在且层数可能为64，但缺乏直接来源支持，且不同版本或变体可能存在差异，无法仅凭逻辑推导确认具体数值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B num_hidden_layers 64
