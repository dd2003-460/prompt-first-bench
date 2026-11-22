# N106: 卖家高挂价策略的期望收益函数 E[Payoff] 中的成交概率 P(deal) 需量化为 P(deal | Premium, Signal) = α * exp

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N26

## Claim

卖家高挂价策略的期望收益函数 E[Payoff] 中的成交概率 P(deal) 需量化为 P(deal | Premium, Signal) = α * exp(-β * Premium) * γ * Signal_strength，其中 α 为基准成交率，β 为价格敏感度系数（[待核验]，通常二手市场 β≈0.5-1.0），γ 为信号放大系数（与 k=0.6 相关），Signal_strength 为平台算法赋予的权重。

## Corrected Claim

卖家高挂价策略的期望收益函数中，成交概率可建模为 P(deal | Premium, Signal) = α * exp(-β * Premium) * γ * Signal_strength，其中 α, β, γ 为需根据具体市场数据校准的经验参数。

## Evidence

[质询]该公式为特定模型假设而非通用事实，且参数β（0.5-1.0）和γ（与k=0.6相关）缺乏普适性依据，属于经验性设定而非第一性原理推导。 | 先验知识/题面给定，逻辑校验通过，但具体参数值（β, γ）为经验假设，无外部来源支持，故降级。

## Search Query

second hand market price elasticity demand curve premium effect
