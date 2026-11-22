# N93: Qwen3-27B 的 KV Cache 在 32K 上下文下的精确显存占用为 6.144 GB，计算过程为 2 (K+V) × 64 (n_layers) ×

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N16

## Claim

Qwen3-27B 的 KV Cache 在 32K 上下文下的精确显存占用为 6.144 GB，计算过程为 2 (K+V) × 64 (n_layers) × 8 (n_kv_heads, GQA) × 128 (head_dim) × 32768 (S_ctx) × 2 (BF16 bytes) = 8,589,934,592 bytes

## Corrected Claim

Qwen3-27B 的 KV Cache 在 32K 上下文下，若 n_layers=64, n_kv_heads=8, head_dim=128, BF16，显存占用为 16 GB (17,179,869,184 bytes)。

## Evidence

[质询]数值计算错误：陈述中声称计算结果为 8,589,934,592 bytes（即 8 GB），但实际计算 2 × 64 × 8 × 128 × 32768 × 2 的结果为 17,179,869,184 bytes（即 16 GB）。陈述中的“6.144 GB”既不符合其列出的公式计算结果，也不符合常见的 Qwen3-27B 架构参数（若 n_kv_heads=8，显存占用应为 16GB；若显存占用为 6.144GB，则参数组合需大幅调整，如 n_kv_heads 或 head_dim 不同，但此时公式与结果不匹配）。 | 逻辑校验失败：公式各项乘积为 17,179,869,184 bytes (16 GB)，与陈述中的 8,589,934,592 bytes (8 GB) 及 6.144 GB 均矛盾，存在硬逻辑错误。

## Search Query

Qwen3-27B config.json n_layers n_kv_heads head_dim
