# N50: vLLM 的 PagedAttention 块表 (Block Table) 和调度器元数据开销约为 0.1-0.3GB，随最大序列数 (max_num_seq

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N8

## Claim

vLLM 的 PagedAttention 块表 (Block Table) 和调度器元数据开销约为 0.1-0.3GB，随最大序列数 (max_num_seqs) 和最大上下文长度线性增长，但在 32K 上下文中通常小于 0.5GB。

## Corrected Claim

vLLM 的 PagedAttention 块表 (Block Table) 和调度器元数据开销通常较小，随最大序列数 (max_num_seqs) 和最大上下文长度增长，但在常规配置下通常远小于模型权重和KV缓存的开销。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 8 column 5 (char 811)

## Search Query

vLLM scheduler metadata memory overhead block table size
