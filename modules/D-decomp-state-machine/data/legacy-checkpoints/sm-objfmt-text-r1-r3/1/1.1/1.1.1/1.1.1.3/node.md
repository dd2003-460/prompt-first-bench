# N96: Qwen3-27B 的 n_kv_heads 确认为 8，n_heads 确认为 32，依据是 GQA 设计文档及 config.json 中 num_key_

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N25, N26, N27

## Claim

Qwen3-27B 的 n_kv_heads 确认为 8，n_heads 确认为 32，依据是 GQA 设计文档及 config.json 中 num_key_value_heads 字段，该比率 (4:1) 决定了 KV 头数减半带来的显存节省

## Corrected Claim

Qwen3-27B 采用 GQA 设计，其 n_kv_heads 通常小于 n_heads（例如 8 vs 32 的配置常见于该系列大模型），这种比率设计旨在通过减少 KV 缓存头数来显著降低推理时的显存占用。

## Evidence

[质询]具体数值（n_kv_heads=8, n_heads=32）属于特定模型版本的经验配置参数，无法从第一性原理推导，且当前无可用外部来源验证该具体版本的确切配置，存在版本迭代导致参数变更的风险。 | 经验事实，逻辑自洽（GQA机制下KV头少于Q头以节省显存符合基本原理，4:1比率计算无误）但缺来源支持。

## Search Query

Qwen3-27B num_key_value_heads GQA
