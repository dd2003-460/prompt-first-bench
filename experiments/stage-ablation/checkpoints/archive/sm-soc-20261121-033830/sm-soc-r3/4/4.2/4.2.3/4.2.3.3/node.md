# N228: 候选B的建议价 g() 的梯度约束：为防止建议价剧烈波动导致卖家困惑，g() 需满足 Lipschitz 连续性约束 |g(P_avg, D, S) - g(P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N72

## Claim

候选B的建议价 g() 的梯度约束：为防止建议价剧烈波动导致卖家困惑，g() 需满足 Lipschitz 连续性约束 |g(P_avg, D, S) - g(P_avg', D', S')| ≤ L * ||(P_avg, D, S) - (P_avg', D', S')||，其中 L 为最大调整幅度系数，通常 L ≤ 0.1（即单次建议变化不超过10%）。

## Corrected Claim

候选B的建议价 g() 的梯度约束：为防止建议价剧烈波动导致卖家困惑，g() 需满足 Lipschitz 连续性约束 |g(P_avg, D, S) - g(P_avg', D', S')| ≤ L * ||(P_avg, D, S) - (P_avg', D', S')||，其中 L 为最大调整幅度系数，通常 L ≤ 0.1（即单次建议变化不超过10%）。

## Evidence

先验知识/题面给定，逻辑校验通过
