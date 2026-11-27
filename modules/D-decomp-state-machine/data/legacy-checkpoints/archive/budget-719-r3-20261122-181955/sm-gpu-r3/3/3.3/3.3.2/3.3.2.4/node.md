# N298: Qwen3-27B 实际架构参数核验：需确认 Qwen3-27B 是否采用 GQA (Grouped Query Attention)。若 n_kv_heads

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98, N100, N101

## Claim

Qwen3-27B 实际架构参数核验：需确认 Qwen3-27B 是否采用 GQA (Grouped Query Attention)。若 n_kv_heads=8 (GQA, 4:1 ratio)，则 KV Cache 大小计算为 2 * 16 layers * 8 kv_heads * 128 head_dim * 32768 seq_len * 2 bytes / 1e9 = 5.37 GB。此值显著低于 N100 中假设 n_kv_heads=32 时的 8.59 GB (或 N89 中的 32.77 GB 错误值)。

## Corrected Claim

若 Qwen3-27B 采用 GQA 且 n_kv_heads=8、layers=16、head_dim=128，则 KV Cache 大小计算为 5.37 GB。此值显著低于假设 n_kv_heads=32 时的 8.59 GB。

## Evidence

[质询]该陈述包含具体的模型架构参数（n_kv_heads=8, layers=16, head_dim=128），属于经验事实。虽然数学计算逻辑自洽，但缺乏外部来源直接证实 Qwen3-27B 的具体架构配置（如层数、KV头数等）是否准确，存在参数假设错误的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体架构参数）

## Search Query

Qwen3-27B architecture n_kv_heads GQA config.json
