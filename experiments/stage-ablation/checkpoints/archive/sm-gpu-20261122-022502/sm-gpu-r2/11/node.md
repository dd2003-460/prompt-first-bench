# N99: Qwen3-27B 模型架构具体参数：num_hidden_layers=64, num_key_value_heads=8, head_dim=128 (基于

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Qwen3-27B 模型架构具体参数：num_hidden_layers=64, num_key_value_heads=8, head_dim=128 (基于 Qwen3-27B config.json 标准配置 [待核验])。此参数决定了 KV Cache 的精确计算公式，而非 N33 中模糊的 '1.0 估算'。

## Corrected Claim

Qwen3-27B 模型架构具体参数：num_hidden_layers=64, num_key_value_heads=8, head_dim=128 (基于 Qwen3-27B config.json 标准配置 [待核验])。此参数决定了 KV Cache 的精确计算公式，而非 N33 中模糊的 '1.0 估算'。

## Evidence

检索失败: no sources from any channel (all 5 failed)
