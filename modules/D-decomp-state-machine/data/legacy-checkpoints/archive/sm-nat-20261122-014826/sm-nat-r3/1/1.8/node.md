# N13: 更新率对 LRU 命中率的折扣因子：1%/天更新率意味着 1% 对象失效，LRU 有效命中率 H_LRU_eff = H_LRU × (1 - 0.01 × P

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

更新率对 LRU 命中率的折扣因子：1%/天更新率意味着 1% 对象失效，LRU 有效命中率 H_LRU_eff = H_LRU × (1 - 0.01 × P[updated object in LRU set])，其中 P[updated object in LRU set] ≈ 0.3 (因热门对象更新率高)，量化为折扣因子 ≈ 0.997。

## Corrected Claim

更新率对 LRU 命中率的折扣因子：1%/天更新率意味着 1% 对象失效，LRU 有效命中率 H_LRU_eff = H_LRU × (1 - 0.01 × P[updated object in LRU set])，其中 P[updated object in LRU set] ≈ 0.3 (因热门对象更新率高)，量化为折扣因子 ≈ 0.997。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

object update rate impact LRU cache hit rate discount factor 1 percent daily
