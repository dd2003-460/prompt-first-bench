# N12: 负相关 ρ≈-0.3 对 LRU 命中率的影响修正项：热门对象较小意味着 LRU 驱逐大对象时字节损失较低，命中率修正因子 f(ρ) = 1 + c*ρ，其中 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

负相关 ρ≈-0.3 对 LRU 命中率的影响修正项：热门对象较小意味着 LRU 驱逐大对象时字节损失较低，命中率修正因子 f(ρ) = 1 + c*ρ，其中 c 为耦合系数，需通过协方差 Cov(Size, Popularity) = ρ*σ_S*σ_P 量化

## Corrected Claim

负相关 ρ≈-0.3 对 LRU 命中率的影响修正项：热门对象较小意味着 LRU 驱逐大对象时字节损失较低，命中率修正因子 f(ρ) = 1 + c*ρ，其中 c 为耦合系数，需通过协方差 Cov(Size, Popularity) = ρ*σ_S*σ_P 量化

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

negative correlation size popularity LRU cache hit rate correction factor
