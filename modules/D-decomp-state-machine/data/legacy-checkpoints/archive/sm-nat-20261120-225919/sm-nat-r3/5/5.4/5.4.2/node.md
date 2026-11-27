# N81: N23 中 0.61 的有效命中率下界未区分请求与字节命中率：在字节命中率口径下，ρ=-0.3 的负相关意味着热门对象更小，字节命中率可能高于请求命中率，K 因

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

N23 中 0.61 的有效命中率下界未区分请求与字节命中率：在字节命中率口径下，ρ=-0.3 的负相关意味着热门对象更小，字节命中率可能高于请求命中率，K 因子需重新推导为 K_byte = 1 + ρ * (β/α) * (E[S_hot]/E[S_cold])，其中 E[S_hot] 和 E[S_cold] 分别为热门和冷门对象的平均大小。

## Corrected Claim

N23 中 0.61 的有效命中率下界未区分请求与字节命中率：在字节命中率口径下，ρ=-0.3 的负相关意味着热门对象更小，字节命中率可能高于请求命中率，K 因子需重新推导为 K_byte = 1 + ρ * (β/α) * (E[S_hot]/E[S_cold])，其中 E[S_hot] 和 E[S_cold] 分别为热门和冷门对象的平均大小。

## Evidence

先验知识/题面给定，逻辑校验通过：字节命中率与请求命中率在对象大小分布不均时确实存在差异，且负相关（热门对象更小）会导致字节命中率高于请求命中率，公式推导符合加权平均逻辑。

## Search Query

byte hit ratio correlation size distribution
