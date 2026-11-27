# N45: Pareto(β=0.9) 热度分布下，前 k% 对象占总请求量的比例 R_k = 1 - k^{1-β}，用于确定 LRU 缓存能覆盖的热度区间，进而映射到工

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N11

## Claim

Pareto(β=0.9) 热度分布下，前 k% 对象占总请求量的比例 R_k = 1 - k^{1-β}，用于确定 LRU 缓存能覆盖的热度区间，进而映射到工作集大小

## Corrected Claim

Pareto(β=0.9) 热度分布下，前 k% 对象占总请求量的比例 R_k = 1 - k^{1-β}，用于确定 LRU 缓存能覆盖的热度区间，进而映射到工作集大小

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布（Zipf-like）的累积分布函数推导正确，R_k = 1 - k^{1-β} 符合数学定义，且用于LRU工作集估算符合缓存理论常识。
