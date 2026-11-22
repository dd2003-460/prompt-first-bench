# N40: Qwen3-27B 的 KV 头数（num_key_value_heads）为 8，采用 GQA（Grouped Query Attention）机制，该值直接

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

Qwen3-27B 的 KV 头数（num_key_value_heads）为 8，采用 GQA（Grouped Query Attention）机制，该值直接决定 KV Cache 的大小，显著小于 MHA 的 32 头。

## Corrected Claim

Qwen3-27B 采用 GQA（Grouped Query Attention）机制，其 KV 头数显著小于 MHA 的 32 头（具体数值需查证，通常此类模型 KV 头数为 8 或 16），该值直接决定 KV Cache 的大小。

## Evidence

[质询]具体数值（8个KV头）属于经验事实，且本轮检索无可用来源，无法通过外部证据直接验证该特定参数值是否准确（尽管GQA机制和量级逻辑合理）。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B config.json num_key_value_heads
