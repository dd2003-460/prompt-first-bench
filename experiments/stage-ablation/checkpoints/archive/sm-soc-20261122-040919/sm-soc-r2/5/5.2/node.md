# N107: Red Queen Effect（利润侵蚀）的量化阈值：当市场内采用低价策略的卖家比例 ρ_low 超过临界值 ρ* 时，高定价策略的期望收益 E[Payoff

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

Red Queen Effect（利润侵蚀）的量化阈值：当市场内采用低价策略的卖家比例 ρ_low 超过临界值 ρ* 时，高定价策略的期望收益 E[Payoff_high] 低于低价策略 E[Payoff_low]。ρ* 的计算公式为 ρ* = (C_search_high - C_search_low) / (Margin_high - Margin_low)，其中 Margin 为单位毛利。[待核验]：需具体市场密度数据。

## Corrected Claim

在特定的静态博弈模型假设下（如搜索成本为单位成本且线性），当低价卖家比例 ρ_low 超过临界值 ρ* = (C_search_high - C_search_low) / (Margin_high - Margin_low) 时，高定价策略的期望收益低于低价策略。该阈值依赖于具体的市场结构和成本假设，并非通用常数。

## Evidence

[质询]公式推导隐含了强假设（如搜索成本线性、无策略互动动态、市场完全竞争等），且未定义 C_search 的具体量纲（是总成本还是单位成本？），若 C_search 为固定成本而非单位成本，则量纲不匹配；此外，该公式更像是一个简化的博弈论均衡条件而非通用的“量化阈值”，直接作为通用公式缺乏普适性证明。 | source=knowledge，逻辑上该公式在特定简化模型（如静态博弈、线性成本结构）下可推导成立，量纲若 C_search 为单位搜索成本则自洽；但作为通用量化阈值缺乏普适性，且无外部来源支持其作为标准公式，故降级为定性/特定模型下的结论。

## Search Query

evolutionary game theory red queen effect pricing strategy threshold
