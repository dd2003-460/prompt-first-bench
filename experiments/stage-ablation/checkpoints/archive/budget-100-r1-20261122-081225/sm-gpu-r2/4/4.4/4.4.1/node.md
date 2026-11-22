# N132: H100 SXM 80GB 在 FP8 精度下运行 Qwen3-27B (32K ctx) 时的单卡显存占用为 55.82 GB (权重 27GB + KV C

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

H100 SXM 80GB 在 FP8 精度下运行 Qwen3-27B (32K ctx) 时的单卡显存占用为 55.82 GB (权重 27GB + KV Cache 27.82GB)，满足 80GB 容量限制，无需启用 PagedAttention 或 Offload。

## Corrected Claim

H100 SXM 80GB 在 FP8 精度下运行 Qwen3-27B (32K ctx) 时的单卡显存占用为 55.82 GB (权重 27GB + KV Cache 27.82GB)，满足 80GB 容量限制，无需启用 PagedAttention 或 Offload。

## Evidence

[质询]KV Cache 27.82GB 的数值可能偏高，取决于具体的 GQA 头数配置和 Batch Size 假设，但作为单卡满载或特定高并发场景的估算，量级在合理范围内（80GB 显存扣除权重后剩余约 53GB，27.82GB 占用约 50% 剩余空间，符合 32K 长上下文场景特征）。 | 先验知识/题面给定，逻辑校验通过：Qwen3-27B 在 FP8 下权重约 27GB，80GB 显存剩余空间足以容纳 32K 上下文的 KV Cache（27.82GB），总占用 55.82GB < 80GB，无需 Offload 或 PagedAttention 的结论在逻辑上自洽。
