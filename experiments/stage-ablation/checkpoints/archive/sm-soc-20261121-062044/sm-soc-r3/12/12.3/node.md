# N277: 低流动性卖家的收入冲击 ΔRevenue_low_liq = (P_avg - P_current) * Q_expected，其中 P_avg 为展示参考价，

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

低流动性卖家的收入冲击 ΔRevenue_low_liq = (P_avg - P_current) * Q_expected，其中 P_avg 为展示参考价，P_current 为原挂价，Q_expected 为预期成交量；若 Q_expected 因透明度降低而减少，需引入价格弹性系数 ε_p 修正：Q_new = Q_old * (P_avg/P_current)^ε_p，ε_p 估计值在 0.6-1.0 之间。

## Corrected Claim

低流动性卖家的收入冲击 ΔRevenue_low_liq = (P_avg - P_current) * Q_expected，其中 P_avg 为展示参考价，P_current 为原挂价，Q_expected 为预期成交量；若 Q_expected 因透明度降低而减少，需引入价格弹性系数 ε_p 修正：Q_new = Q_old * (P_avg/P_current)^ε_p，ε_p 估计值在 0.6-1.0 之间。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price elasticity of demand for second hand goods low liquidity items
