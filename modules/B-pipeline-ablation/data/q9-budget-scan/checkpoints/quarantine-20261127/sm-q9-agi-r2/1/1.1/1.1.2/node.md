# N31: Qwen3.8-27B 采用 GQA (Grouped Query Attention) 架构，KV Cache 单 token 显存占用公式为 C_kv_to

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

Qwen3.8-27B 采用 GQA (Grouped Query Attention) 架构，KV Cache 单 token 显存占用公式为 C_kv_token = 2 * n_layers * n_kv_heads * head_dim * dtype_size_bytes；假设 n_layers=32, n_kv_heads=8, head_dim=128, dtype_size=1 byte (FP8)，则 C_kv_token ≈ 65.5 KB/token。

## Corrected Claim

Qwen3.8-27B 采用 GQA (Grouped Query Attention) 架构，KV Cache 单 token 显存占用公式为 C_kv_token = 2 * n_layers * n_kv_heads * head_dim * dtype_size_bytes；假设 n_layers=32, n_kv_heads=8, head_dim=128, dtype_size=1 byte (FP8)，则 C_kv_token ≈ 65.5 KB/token。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 C_kv_token = 2 * n_layers * n_kv_heads * head_dim * dtype_size_bytes 符合 GQA 架构 KV Cache 计算原理（Key和Value各占一份，故系数为2）；代入数值 2 * 32 * 8 * 128 * 1 = 65536 Bytes = 64 KB，与陈述中的 ≈ 65.5 KB 在数量级和近似范围内一致（注：65536 Bytes 精确等于 64 KiB，若按 1000 进制则为 65.536 KB，此处近似合理）。

## Search Query

Qwen3.8-27B architecture parameters num layers kv heads head dim
