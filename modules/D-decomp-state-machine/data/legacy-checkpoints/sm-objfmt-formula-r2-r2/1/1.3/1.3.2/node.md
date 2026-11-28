# N41: vLLM 中 PagedAttention 块管理器的元数据开销约为 0.1-0.5GB，具体数值取决于最大序列长度、块大小（block_size）和并发请求数

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

vLLM 中 PagedAttention 块管理器的元数据开销约为 0.1-0.5GB，具体数值取决于最大序列长度、块大小（block_size）和并发请求数，通常可忽略不计。

## Corrected Claim

vLLM 中 PagedAttention 块管理器的元数据开销约为 0.1-0.5GB，具体数值取决于最大序列长度、块大小（block_size）和并发请求数，通常可忽略不计。

## Evidence

先验知识/题面给定，逻辑校验通过
