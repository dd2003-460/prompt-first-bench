# N235: GMV_new 的敏感性参数：价格弹性 ε_p 和成交量弹性 ε_q。GMV_new ≈ GMV_old * (1 + ε_p * ΔP%) * (1 + ε_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

GMV_new 的敏感性参数：价格弹性 ε_p 和成交量弹性 ε_q。GMV_new ≈ GMV_old * (1 + ε_p * ΔP%) * (1 + ε_q * ΔQ%)。二手平台典型 ε_p ∈ [-0.5, -1.5]，ε_q ∈ [0.3, 1.0]，需通过A/B测试校准。

## Corrected Claim

GMV_new 的敏感性参数：价格弹性 ε_p 和成交量弹性 ε_q。GMV_new ≈ GMV_old * (1 + ε_p * ΔP%) * (1 + ε_q * ΔQ%)。二手平台典型 ε_p ∈ [-0.5, -1.5]，ε_q ∈ [0.3, 1.0]，需通过A/B测试校准。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price elasticity of demand second-hand goods market
