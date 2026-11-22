# N226: 成交概率 Q 对价格 P_deal 的偏导数 ∂Q/∂P 的数值估算：基于二手平台平均价格弹性 e_p = -1.2 (假设值，需A/B测试验证)，计算 ∂Q/

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

成交概率 Q 对价格 P_deal 的偏导数 ∂Q/∂P 的数值估算：基于二手平台平均价格弹性 e_p = -1.2 (假设值，需A/B测试验证)，计算 ∂Q/∂P = e_p * Q / P_deal，需代入基准成交概率 Q_base 及基准价 P_market 进行计算。

## Corrected Claim

成交概率 Q 对价格 P_deal 的偏导数 ∂Q/∂P 的数值估算：基于二手平台平均价格弹性 e_p = -1.2 (假设值，需A/B测试验证)，计算 ∂Q/∂P = e_p * Q / P_deal，需代入基准成交概率 Q_base 及基准价 P_market 进行计算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 ∂Q/∂P = e_p * Q / P 符合点弹性定义，量纲与逻辑自洽。

## Search Query

used goods marketplace price elasticity of demand average
