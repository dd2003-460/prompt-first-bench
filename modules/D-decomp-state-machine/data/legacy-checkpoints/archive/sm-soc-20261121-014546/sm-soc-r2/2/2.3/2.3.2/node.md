# N61: 一阶条件投影 FOC_seller：卖家效用函数对挂价的一阶偏导数 ∂U_seller/∂P_ask = 0 的具体解析式，展开为 p'(P_ask)·(P_a

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N13

## Claim

一阶条件投影 FOC_seller：卖家效用函数对挂价的一阶偏导数 ∂U_seller/∂P_ask = 0 的具体解析式，展开为 p'(P_ask)·(P_ask - C) + p(P_ask)·(1 - γ)·(P_ask - C)^(-γ) = 0，其中 p'(P_ask) 为成交概率对价格的敏感度系数，通常取 -0.05/单位价格变动。

## Corrected Claim

卖家效用函数对挂价的一阶偏导数 ∂U_seller/∂P_ask = 0 的具体解析式依赖于特定的效用函数和成交概率模型假设，通常形式为 p'(P_ask)·(P_ask - C) + p(P_ask)·(其他项) = 0，其中 p'(P_ask) 为成交概率对价格的敏感度系数，具体数值需根据市场数据校准。

## Evidence

[质询]该陈述包含具体的经验参数（如敏感度系数 -0.05）和特定的函数形式（含 (P_ask - C)^(-γ) 项），这些并非第一性原理可推导的通用数学恒等式，而是依赖于特定市场模型假设的经验设定。在缺乏来源支持的情况下，无法确认该具体解析式及参数值的普适性或准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

seller utility maximization first order condition price elasticity probability of sale
