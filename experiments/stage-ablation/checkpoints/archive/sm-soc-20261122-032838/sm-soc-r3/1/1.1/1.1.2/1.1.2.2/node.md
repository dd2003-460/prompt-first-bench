# N114: 基于历史成交价方差的异质性指数 $H_{price} = \sqrt{\text{Var}(P_{hist})} / P_{ref}$ 的阈值判断：若 $H_{

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N34

## Claim

基于历史成交价方差的异质性指数 $H_{price} = \sqrt{\text{Var}(P_{hist})} / P_{ref}$ 的阈值判断：若 $H_{price} > 0.2$，表明市场定价离散度高，买家难以形成稳定价格预期，需引入更高质量信号（如认证）才能降低 $C_{info}$。

## Corrected Claim

基于历史成交价方差的异质性指数 $H_{price} = \sqrt{\text{Var}(P_{hist})} / P_{ref}$ 的阈值判断：若 $H_{price} > 0.2$，表明市场定价离散度高，买家难以形成稳定价格预期，需引入更高质量信号（如认证）才能降低 $C_{info}$。

## Evidence

先验知识/题面给定，逻辑校验通过：该陈述定义了基于价格方差的异质性指数，并基于信息经济学原理（高价格离散度导致预期不稳定，需高质量信号降低信息成本）建立了合理的因果逻辑，量纲与量级在理论模型中自洽。

## Search Query

price dispersion index used goods market heterogeneity threshold 0.2
