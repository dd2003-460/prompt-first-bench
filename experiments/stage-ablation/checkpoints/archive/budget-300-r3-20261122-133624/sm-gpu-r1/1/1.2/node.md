# N7: Qwen3-27B 在 32K 上下文长度下，GQA 架构（假设 4 KV heads, 128 head_dim）的 KV Cache 显存占用约为 4.09

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N1

## Claim

Qwen3-27B 在 32K 上下文长度下，GQA 架构（假设 4 KV heads, 128 head_dim）的 KV Cache 显存占用约为 4.09GB（2 × 4 × 128 × 32768 × 2 bytes）

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下，GQA 架构（假设 4 KV heads, 128 head_dim）的 KV Cache 显存占用约为 4.09GB（2 × 4 × 128 × 32768 × 2 bytes）

## Search Query

Qwen3-27B architecture GQA KV heads head dimension
