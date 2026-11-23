# N29: Qwen3-27B 的架构参数确认：Layer_Count=32, Hidden_Size=4096, KV_Heads=8, Head_Dim=128, GQ

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

Qwen3-27B 的架构参数确认：Layer_Count=32, Hidden_Size=4096, KV_Heads=8, Head_Dim=128, GQA_Ratio=8:1 (即 32 Q-heads 共享 8 KV-heads)。

## Corrected Claim

Qwen3-27B 的架构参数疑似为：Layer_Count=32, Hidden_Size=4096, KV_Heads=8, Head_Dim=128, GQA_Ratio=8:1，但需进一步核实。

## Evidence

[质询]具体架构参数（如Layer_Count, Hidden_Size等）属于经验事实，无法从第一性原理推导，且当前无可用外部来源支持，存在参数记忆错误或版本混淆的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B model architecture config.json num_hidden_layers num_key_value_heads
