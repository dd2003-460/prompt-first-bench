# N308: FAISS IVF-PQ 在 N=10k 规模下，默认 nprobe=10 时的 Top-5 召回率（Recall@5）通常低于 Flat 索引的 99%+，具

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N124

## Claim

FAISS IVF-PQ 在 N=10k 规模下，默认 nprobe=10 时的 Top-5 召回率（Recall@5）通常低于 Flat 索引的 99%+，具体数值约为 85%-92%（取决于 PQ 压缩损失），导致为了达到同等召回率必须将 nprobe 提升至 50-100，从而使检索延迟从 ~1ms 升至 5-15ms，抵消了构建时间的微小优势。

## Corrected Claim

FAISS IVF-PQ 在 N=10k 规模下，默认 nprobe=10 时的 Top-5 召回率通常显著低于 Flat 索引的 99%+（具体数值受 PQ 压缩参数影响，常见范围可能在 80%-95% 之间），为了达到同等召回率通常需要提升 nprobe，这将导致检索延迟增加，从而抵消部分构建时间优势。

## Evidence

[质询]具体数值区间（85%-92%）和延迟范围（5-15ms）高度依赖于具体的维度、PQ子向量数量（m）、数据类型及硬件环境，缺乏统一标准，直接断言固定区间存在以偏概全的风险。 | 先验知识/题面给定，逻辑校验通过：IVF-PQ作为近似最近邻算法，其召回率必然低于精确搜索（Flat），且nprobe增加会线性增加计算量从而提升延迟，符合ANN算法的基本权衡逻辑；但具体数值为经验估计，非绝对真理。

## Search Query

faiss ivf-pq recall vs flat small dataset nprobe tradeoff
