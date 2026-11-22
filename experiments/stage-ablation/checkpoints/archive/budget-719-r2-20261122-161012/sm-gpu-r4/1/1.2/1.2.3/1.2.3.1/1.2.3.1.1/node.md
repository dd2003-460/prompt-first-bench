# N354: Qwen3-27B 的 num_hidden_layers 确认为 64 层，此数值来自 HuggingFace 模型配置文件 (config.json)；该层

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N147

## Claim

Qwen3-27B 的 num_hidden_layers 确认为 64 层，此数值来自 HuggingFace 模型配置文件 (config.json)；该层数是计算总 KV Cache 显存 (KV_Total = KV_Layer * 64) 和 Prefill FLOPs (FLOPs = 2 * Params * SeqLen * Layers/Params) 的关键乘数，任何层数误差将线性传播至最终显存和延迟估算

## Corrected Claim

Qwen3-27B 的 num_hidden_layers 通常被配置为 64 层（需以官方 config.json 为准），此数值是计算总 KV Cache 显存和 Prefill FLOPs 的关键乘数，层数误差将线性传播至最终估算。

## Evidence

[质询]该陈述包含具体的经验参数（Qwen3-27B 的 num_hidden_layers 为 64），属于经验事实，无法仅通过第一性原理推导得出，且当前无可用外部来源直接验证该具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法确认 Qwen3-27B 具体层数，但层数作为 KV Cache 和 FLOPs 计算乘数的逻辑关系正确）

## Search Query

Qwen3-27B config.json num_hidden_layers
