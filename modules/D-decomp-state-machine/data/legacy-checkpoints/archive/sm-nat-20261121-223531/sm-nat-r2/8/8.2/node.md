# N77: 容量受限假设下的 LRU 命中率公式：若假设有效缓存对象数 N_eff=10,000，LRU 字节命中率 H_LRU = (Σ_{i∈Top10k} s_i *

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

容量受限假设下的 LRU 命中率公式：若假设有效缓存对象数 N_eff=10,000，LRU 字节命中率 H_LRU = (Σ_{i∈Top10k} s_i * r_i) / (Σ_{j=1}^{100k} s_j * r_j)，其中 s_i 为对象大小，r_i 为请求频率，Top10k 按 LRU 堆栈深度（即最近访问顺序）选取。

## Corrected Claim

容量受限假设下的 LRU 命中率公式：若假设有效缓存对象数 N_eff=10,000，LRU 字节命中率 H_LRU = (Σ_{i∈Top10k} s_i * r_i) / (Σ_{j=1}^{100k} s_j * r_j)，其中 s_i 为对象大小，r_i 为请求频率，Top10k 按 LRU 堆栈深度（即最近访问顺序）选取。

## Evidence

先验知识/题面给定，逻辑校验通过
