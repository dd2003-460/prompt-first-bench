# N48: Qwen3-27B 模型架构参数确认：num_layers=64, hidden_size=4096, num_attention_heads=32, num_

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Qwen3-27B 模型架构参数确认：num_layers=64, hidden_size=4096, num_attention_heads=32, num_key_value_heads=8 (GQA), head_dim=128。这些参数直接决定 KV Cache 公式中的变量取值，需通过模型 config.json 或官方技术报告核实，若 num_key_value_heads 为 16 (MHA) 则 KV Cache 翻倍。

## Corrected Claim

Qwen3-27B 模型架构参数需通过官方 config.json 核实：若 num_key_value_heads=8 (GQA)，则 KV Cache 按 GQA 计算；若为 16 (MHA)，则 KV Cache 翻倍。当前检索无法确认具体数值，建议以官方发布配置为准。

## Evidence

[质询]该陈述包含具体的硬件/模型架构参数（经验事实），且参考来源全部缺失，无法通过外部检索直接验证 num_key_value_heads 是 8 还是 16，存在参数记忆偏差或版本混淆的风险。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无法排除参数错误可能性）

## Search Query

Qwen3-27B model config num_layers num_key_value_heads hidden_size
