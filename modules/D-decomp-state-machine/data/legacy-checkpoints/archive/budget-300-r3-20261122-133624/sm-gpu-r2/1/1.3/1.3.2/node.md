# N50: vLLM 的 PagedAttention 块表 (Block Table) 和调度器元数据开销约为 0.1-0.3GB，随最大序列数 (max_num_seq

- **status**: degraded
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

[质询]该陈述包含具体的经验数值范围（0.1-0.3GB）和阈值（<0.5GB），属于经验事实而非第一性原理可推导的数学/物理定律。在缺乏外部来源支持的情况下，无法验证这些具体数值是否准确，且不同硬件配置、vLLM版本及具体参数设置下，元数据开销可能存在显著差异，存在数值量级或具体阈值不准确的风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

vLLM scheduler metadata memory overhead block table size
