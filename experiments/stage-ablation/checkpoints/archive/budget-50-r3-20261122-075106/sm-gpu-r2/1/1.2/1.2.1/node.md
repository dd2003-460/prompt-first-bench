# N47: Qwen3-27B 在 32K 上下文长度下，KV Cache 的理论最大需求为 0.785 GB（假设 48 层，每层 48 个 KV 头，每头 128 维，

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Qwen3-27B 在 32K 上下文长度下，KV Cache 的理论最大需求为 0.785 GB（假设 48 层，每层 48 个 KV 头，每头 128 维，FP8 精度），需与权重显存叠加。

## Corrected Claim

Qwen3-27B 在 32K 上下文长度下，KV Cache 的理论最大需求为 0.785 GB（假设 48 层，每层 48 个 KV 头，每头 128 维，FP8 精度），需与权重显存叠加。
