# N439: 在 32K 上下文窗口下，单请求 KV Cache 总显存占用为 2.0 GB，计算式为 32768 tokens * 64 KB/token / 1024 =

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N136

## Claim

在 32K 上下文窗口下，单请求 KV Cache 总显存占用为 2.0 GB，计算式为 32768 tokens * 64 KB/token / 1024 = 2048 MB。

## Corrected Claim

在 32K 上下文窗口下，若单 token KV Cache 占用为 64 KB，则总显存占用为 2.0 GB（计算式：32768 * 64 / 1024 = 2048 MB）。

## Evidence

[质询]64 KB/token 的 KV Cache 占用量级对于主流大模型（如 Llama 系列）而言偏高，通常该数值取决于模型架构（层数、头数、头维度）和精度（FP16/BF16），并非固定常数；若模型较小或采用量化，该数值会显著降低。 | source=knowledge，逻辑校验通过（32768 * 64 / 1024 = 2048），但 64 KB/token 为经验参数，缺乏特定模型上下文支持，无法确认为通用事实。
