# N341: C4 数据集在 LLM 评测中常用的子集大小（如 1M tokens 或 100K samples）及其与 WikiText-2 在领域分布上的差异对 PPL 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N121

## Claim

C4 数据集在 LLM 评测中常用的子集大小（如 1M tokens 或 100K samples）及其与 WikiText-2 在领域分布上的差异对 PPL 敏感度的量化影响系数。

## Corrected Claim

C4 数据集在 LLM 评测中通常使用大规模子集（如百万级 tokens），其领域分布比 WikiText-2 更广泛，导致 PPL 对数据分布变化的敏感度不同，但具体量化系数需依赖特定实验。

## Evidence

[质询]该陈述包含具体的经验性数值（1M tokens, 100K samples）和未定义的量化指标（PPL敏感度量化影响系数），这些属于经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

C4 dataset subset size perplexity evaluation LLM standard
