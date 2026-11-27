# N305: S_avg_LFU / S_avg_LRU 的比值计算：S_avg_LFU = (Σ_{i∈S_LFU} s_i) / |S_LFU|，S_avg_LRU = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N108

## Claim

S_avg_LFU / S_avg_LRU 的比值计算：S_avg_LFU = (Σ_{i∈S_LFU} s_i) / |S_LFU|，S_avg_LRU = (Σ_{i∈S_LRU} s_i) / |S_LRU|，其中 s_i 服从 Pareto(α=1.1) 且与热度负相关（ρ=-0.3）；需量化该比值对 ΔH_max 的影响。

## Corrected Claim

S_avg_LFU / S_avg_LRU 的比值计算：S_avg_LFU = (Σ_{i∈S_LFU} s_i) / |S_LFU|，S_avg_LRU = (Σ_{i∈S_LRU} s_i) / |S_LRU|，其中 s_i 服从 Pareto(α=1.1) 且与热度负相关（ρ=-0.3）；需量化该比值对 ΔH_max 的影响。

## Evidence

先验知识/题面给定，逻辑校验通过
