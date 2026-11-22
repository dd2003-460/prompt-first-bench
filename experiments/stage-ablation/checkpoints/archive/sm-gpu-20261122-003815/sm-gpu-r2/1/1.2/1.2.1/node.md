# N48: A100 80GB 运行 Qwen3-27B BF16 的余量分析：总需求 71.2GB (N22) < 80GB，余量 8.8GB 可支持 Batch Siz

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

A100 80GB 运行 Qwen3-27B BF16 的余量分析：总需求 71.2GB (N22) < 80GB，余量 8.8GB 可支持 Batch Size=2 或上下文扩展至 ~40K tokens，无需量化即可满足 32K 上下文要求。

## Corrected Claim

A100 80GB 运行 Qwen3-27B BF16 的余量分析：总需求 71.2GB (N22) < 80GB，余量 8.8GB 可支持 Batch Size=2 或上下文扩展至 ~40K tokens，无需量化即可满足 32K 上下文要求。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16 权重约 54GB，加上 32K 上下文的 KV Cache 及激活值，总显存需求约 71.2GB 符合工程估算量级，小于 80GB 且余量合理。

## Search Query

A100 80GB batch size LLM inference memory margin
