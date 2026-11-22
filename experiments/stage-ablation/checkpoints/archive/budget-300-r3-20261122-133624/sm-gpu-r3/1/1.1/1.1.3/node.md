# N45: 在 vLLM 中，BF16 模型的 KV Cache 块大小配置 (block_size) 通常为 16 或 64 tokens，导致实际分配的 KV Cach

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

在 vLLM 中，BF16 模型的 KV Cache 块大小配置 (block_size) 通常为 16 或 64 tokens，导致实际分配的 KV Cache 显存需向上取整至块边界，相比理论值 (N7) 可能增加 0.1-0.5GB 的碎片开销。

## Corrected Claim

在 vLLM 中，BF16 模型的 KV Cache 块大小配置 (block_size) 通常为 16 或 64 tokens，导致实际分配的 KV Cache 显存需向上取整至块边界，相比理论值可能产生一定的碎片开销（具体数值取决于模型规模和序列长度）。

## Evidence

[质询]该陈述包含具体的经验参数（block_size 默认值 16/64）和具体的量化开销范围（0.1-0.5GB），这些属于经验事实而非第一性原理可推导内容。由于检索失败无外部来源支持，且不同模型规模、序列长度下碎片开销差异巨大，固定范围 0.1-0.5GB 缺乏普适性依据，存在数值量级不准确的风险。 | 经验事实，逻辑自洽但缺来源支持。vLLM 确实采用 PagedAttention 机制，block_size 通常为 16 或 64，向上取整会导致显存碎片，但具体开销 0.1-0.5GB 依赖于具体模型和负载，无来源佐证该特定数值范围。

## Search Query

vLLM paged attention block size overhead bf16 memory allocation fragmentation
