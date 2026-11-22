# N12: LFU 相对 LRU 的最大百分点提升 = HitRate_bytes_LFU - HitRate_bytes_LRU，主要增益来源是 LFU 能更精准地保留高

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N3

## Claim

LFU 相对 LRU 的最大百分点提升 = HitRate_bytes_LFU - HitRate_bytes_LRU，主要增益来源是 LFU 能更精准地保留高频小对象，而 LRU 受时间局部性影响可能驱逐仍高频但最近未被访问的对象；量化增益取决于 ρ 的强度和 β 与 α 的差异。

## Corrected Claim

LFU 相对 LRU 的命中率提升主要源于其能更精准地保留高频小对象，避免 LRU 因时间局部性限制而驱逐仍高频但最近未被访问的对象；具体量化增益取决于访问模式参数（如 ρ, β, α）的差异，需结合具体实验数据确定。

## Evidence

[质询]该陈述包含具体的量化结论（'最大百分点提升'）和特定参数（ρ, β, α）的依赖关系，但提供的参考来源[1]仅涉及Redis中LRU与LFU的通用实现与效果分析，未包含针对特定参数ρ, β, α的量化实验数据或公式推导，无法直接支持该具体量化结论。 | 逻辑上LFU确实比LRU更擅长处理高频但非最近访问的对象，定性原理正确；但source为search，且参考来源[1]未提供关于ρ, β, α参数下的具体量化增益数据，属于经验事实/特定实验结论，缺乏直接来源支持，故降级。

## Search Query

LFU vs LRU cache hit rate improvement Pareto workload correlation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/641841636&rut=96c5bc09c47f8a549e8849194645b4663ac2be524195b61a9f699c4474f03ff2', 'type': 'ddg', 'title': '深入解析Redis的LRU与LFU算法实现 - 知乎'}
