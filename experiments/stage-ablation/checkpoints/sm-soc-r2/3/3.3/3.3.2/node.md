# N64: 平台算法激励高挂价的机制：曝光权重 W_exposure = f(T_close, Margin, Price)，其中 Margin = (P_ask - P_

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N17

## Claim

平台算法激励高挂价的机制：曝光权重 W_exposure = f(T_close, Margin, Price)，其中 Margin = (P_ask - P_market)/P_market。实证显示 W_exposure 与 Margin 正相关（ρ ≈ 0.4-0.6），且与 T_close 负相关，导致平台算法隐式奖励高溢价且快速成交的商品，形成正向反馈。

## Corrected Claim

平台算法通常存在激励高挂价或高溢价商品的机制，曝光权重往往与商品利润率或溢价幅度正相关，与成交紧迫度负相关，从而形成正向反馈循环。具体相关系数因平台和数据集而异。

## Evidence

[质询]该陈述包含具体的实证统计数值（ρ ≈ 0.4-0.6）和特定的算法机制描述，属于经验事实。虽然逻辑上自洽（高溢价通常伴随高利润，平台可能通过算法激励此类行为以最大化GMV或佣金），但缺乏具体的平台名称、时间范围及数据来源，且“隐式奖励”这一因果机制在不同平台（如Amazon vs. eBay vs. 国内电商）可能存在显著差异，无法仅凭逻辑推导确认具体的相关系数范围。 | 经验事实，逻辑自洽但缺来源支持。该陈述描述了平台算法的一种常见假设或观察到的现象，但具体的相关系数（ρ值）和机制细节属于特定实证研究结论，非第一性原理可推导，且本轮无可用外部来源验证具体数值。

## Search Query

marketplace algorithm ranking bias high margin fast selling items
