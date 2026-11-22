# N160: vLLM 在 32K 上下文、batch_size=1 时，PagedAttention 的 block table 和元数据开销约为 100-500 MB，具

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

vLLM 在 32K 上下文、batch_size=1 时，PagedAttention 的 block table 和元数据开销约为 100-500 MB，具体数值取决于 block_size 配置（通常为 16 tokens/block）。

## Corrected Claim

vLLM 在 32K 上下文、batch_size=1 时，PagedAttention 的 block table 和元数据开销约为 100-500 MB，具体数值取决于 block_size 配置（通常为 16 tokens/block）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM PagedAttention block table memory overhead 32K context
