# N209: LRU 驱逐边界对应的频率阈值 λ_threshold 的解析近似：λ_threshold ≈ f_{N_cap}，其中 f_{N_cap} 是第 N_cap 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N79

## Claim

LRU 驱逐边界对应的频率阈值 λ_threshold 的解析近似：λ_threshold ≈ f_{N_cap}，其中 f_{N_cap} 是第 N_cap 个最热门对象的访问频率，需结合 N_cap 与 Pareto(β=0.9) 的逆 CDF 计算

## Corrected Claim

LRU 驱逐边界对应的频率阈值 λ_threshold 的解析近似：λ_threshold ≈ f_{N_cap}，其中 f_{N_cap} 是第 N_cap 个最热门对象的访问频率，需结合 N_cap 与 Pareto(β=0.9) 的逆 CDF 计算

## Evidence

先验知识/题面给定，逻辑校验通过：LRU 缓存中，当缓存容量为 N_cap 时，被驱逐的对象通常是访问频率低于第 N_cap 个最热门对象频率的对象，因此频率阈值 λ_threshold 近似等于第 N_cap 个最热门对象的频率 f_{N_cap}，该关系符合 LRU 的基本工作原理和 Pareto 分布的性质。
