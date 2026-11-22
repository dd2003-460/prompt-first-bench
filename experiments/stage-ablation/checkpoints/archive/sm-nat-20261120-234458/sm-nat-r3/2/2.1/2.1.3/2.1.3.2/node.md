# N111: 在相同容量约束（K=50,000）下，LRU保留最近访问对象，其字节命中率 H_LRU_50 = (Σ_{i∈LRU_Set} q_i * s_i) / (Σ_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N35

## Claim

在相同容量约束（K=50,000）下，LRU保留最近访问对象，其字节命中率 H_LRU_50 = (Σ_{i∈LRU_Set} q_i * s_i) / (Σ_{i=1}^{100000} q_i * s_i)，其中LRU_Set取决于访问序列，在稳态下近似为热度排名随机分布或基于访问间隔的集合，需模拟或解析近似。

## Corrected Claim

在相同容量约束（K=50,000）下，LRU保留最近访问对象，其字节命中率 H_LRU_50 = (Σ_{i∈LRU_Set} q_i * s_i) / (Σ_{i=1}^{100000} q_i * s_i)，其中LRU_Set取决于访问序列，在稳态下近似为热度排名随机分布或基于访问间隔的集合，需模拟或解析近似。

## Evidence

先验知识/题面给定，逻辑校验通过
