# N38: Qwen3-27B 的层数（num_hidden_layers）为 64，这是计算 KV Cache 和激活值的基础架构参数。

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Qwen3-27B 的层数（num_hidden_layers）为 64，这是计算 KV Cache 和激活值的基础架构参数。

## Corrected Claim

Qwen3-27B 的层数（num_hidden_layers）为 64（待核实），这是计算 KV Cache 和激活值的基础架构参数。

## Evidence

[质询]具体层数（64层）属于经验事实/具体参数值，无法从第一性原理推导，且当前无可用来源支持，存在数值错误的可能性（如实际为48层或其他值）。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B config.json num_hidden_layers
