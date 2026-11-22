# N552: Qwen3-27B 的架构参数需确认以计算 KV Cache：若为 GQA 8 KV heads, head_dim=128, layers=32, 则 32K

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N229

## Claim

Qwen3-27B 的架构参数需确认以计算 KV Cache：若为 GQA 8 KV heads, head_dim=128, layers=32, 则 32K 上下文下 KV Cache 大小 = 2 * 32 * 8 * 128 * 32768 * 1 byte (FP8) ≈ 2.15 GB；若为 MHA (32 KV heads)，则 ≈ 8.6 GB。当前 N229 中的 1.2 GB 数值与常见架构参数不匹配，需依据 Qwen3-27B 官方模型卡确认 KV heads 数量及是否启用 KV 量化。

## Corrected Claim

Qwen3-27B 的 KV Cache 大小取决于其具体架构参数（如 KV heads 数量、是否启用量化等）。若假设其为 GQA 8 KV heads, head_dim=128, layers=32, 则 32K 上下文下 KV Cache 大小约为 2.15 GB (FP8)；若为 MHA (32 KV heads)，则约为 8.6 GB。当前 N229 中的 1.2 GB 数值需依据官方模型卡确认架构参数后重新计算。

## Evidence

[质询]该陈述包含具体的经验性架构参数（如 Qwen3-27B 的 KV heads 数量、层数、head_dim 等），这些属于特定模型的具体规格，无法从第一性原理推导，且当前无可用外部来源验证其准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B model architecture GQA KV heads num_layers head_dim technical report
