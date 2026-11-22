# N111: 卖家初始挂价 P_ask 的决策函数：P_ask = P_min + (λ - 1) * (P_ref - P_min) * (1 - β_liquidity)

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N30

## Claim

卖家初始挂价 P_ask 的决策函数：P_ask = P_min + (λ - 1) * (P_ref - P_min) * (1 - β_liquidity)，其中 β_liquidity 为流动性风险折价系数，反映卖家对‘卖不出去’风险的感知，需通过平台数据回归估计 β_liquidity 的具体数值以解释为何溢价仅为 15-25% 而非更高。

## Corrected Claim

卖家初始挂价 P_ask 的决策函数：P_ask = P_min + (λ - 1) * (P_ref - P_min) * (1 - β_liquidity)，其中 β_liquidity 为流动性风险折价系数，反映卖家对‘卖不出去’风险的感知，需通过平台数据回归估计 β_liquidity 的具体数值以解释为何溢价仅为 15-25% 而非更高。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

seller listing price decision model liquidity discount coefficient
