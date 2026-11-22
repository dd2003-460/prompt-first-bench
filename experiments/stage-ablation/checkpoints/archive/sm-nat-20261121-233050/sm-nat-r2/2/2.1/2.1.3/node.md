# N35: LRU 下界公式修正项：N14 中的公式 H_LRU_lower = 1 - (1 - M/C)^β * (1 + α*β/(α-1)) 忽略了负相关性 ρ=-

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N9

## Claim

LRU 下界公式修正项：N14 中的公式 H_LRU_lower = 1 - (1 - M/C)^β * (1 + α*β/(α-1)) 忽略了负相关性 ρ=-0.3，需引入 Copula 修正因子 C_ρ，使得当 ρ<0 时，热门对象更小，导致 LRU 在固定容量下能容纳更多热门对象，从而提升命中率下界约 5-10%（需量化）。

## Corrected Claim

LRU 下界公式需引入考虑负相关性 ρ=-0.3 的修正项（如 Copula 修正因子），理论上该修正会提升命中率下界，但具体提升幅度需通过实证数据量化，而非直接断定为 5-10%。

## Evidence

[质询]该陈述包含具体的经验性数值结论（命中率提升约5-10%）和特定的统计修正方法（Copula修正因子），属于经验事实而非第一性原理可推导的数学恒等式。参考来源仅涉及缓存替换策略的一般性定义，未提供关于负相关性ρ=-0.3对LRU下界具体量化影响的任何数据或理论支持，无法验证该具体数值范围。 | 逻辑上，负相关性通常意味着热门对象分布更集中或长尾更短，理论上可能有利于LRU，但具体提升幅度（5-10%）是经验参数，来源[1]仅定义命中率概念，未覆盖此特定修正公式及数值，故降级为定性表述。

## Search Query

LRU cache hit rate lower bound negative correlation size frequency Pareto

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Cache_replacement_policies&rut=2231834c94737ba3733d46daf479ebf979f82867d264089e046e50af38a37bd6', 'type': 'ddg', 'title': 'Cache replacement policies - Wikipedia'}
