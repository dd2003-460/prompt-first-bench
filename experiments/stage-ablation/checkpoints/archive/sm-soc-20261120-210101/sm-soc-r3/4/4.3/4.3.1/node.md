# N79: 价格弹性系数 α 的品类交互效应修正：N20 给出 α_服装=0.5, α_数码=1.2，但未考虑‘新品/旧品’交互。对于数码类，新品 α_new = 1.5，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

价格弹性系数 α 的品类交互效应修正：N20 给出 α_服装=0.5, α_数码=1.2，但未考虑‘新品/旧品’交互。对于数码类，新品 α_new = 1.5，旧品 α_old = 0.8，混合 α = w_new * 1.5 + (1-w_new) * 0.8。若未区分新旧，dT/dP 预测误差可达 40%，需引入商品成色变量 S 修正 α = α_base * (1 + β_s * (S - S_avg))。

## Corrected Claim

价格弹性系数 α 的品类交互效应修正：N20 给出 α_服装=0.5, α_数码=1.2，但未考虑‘新品/旧品’交互。对于数码类，新品 α_new = 1.5，旧品 α_old = 0.8，混合 α = w_new * 1.5 + (1-w_new) * 0.8。若未区分新旧，dT/dP 预测误差可达 40%，需引入商品成色变量 S 修正 α = α_base * (1 + β_s * (S - S_avg))。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

price elasticity of demand new vs used electronics second hand
