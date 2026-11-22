# N265: Qwen3-27B 的实际架构参数 n_layers=32, n_kv_heads=8, head_dim=128 (来源: Qwen3-27B config.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N89

## Claim

Qwen3-27B 的实际架构参数 n_layers=32, n_kv_heads=8, head_dim=128 (来源: Qwen3-27B config.json)，修正 N89 中错误的 n_layers=16 假设。

## Corrected Claim

Qwen3-27B 的架构参数 n_layers=32, n_kv_heads=8, head_dim=128 需进一步核实，当前缺乏直接来源支持。

## Evidence

[质询]具体架构参数（n_layers, n_kv_heads, head_dim）属于经验事实，无法从第一性原理推导，且当前无可用外部来源直接验证其数值准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B config.json n_layers n_kv_heads head_dim
