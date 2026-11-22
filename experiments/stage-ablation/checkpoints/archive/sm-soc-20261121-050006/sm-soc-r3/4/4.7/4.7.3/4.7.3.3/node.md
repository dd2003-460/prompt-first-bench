# N289: 干预效果减半时间的边界条件：当市场流动性指数 L_market < 0.5（定义为日均成交量/库存量）时，λ_decay 会降低 30-50%，导致 T_eff

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N91

## Claim

干预效果减半时间的边界条件：当市场流动性指数 L_market < 0.5（定义为日均成交量/库存量）时，λ_decay 会降低 30-50%，导致 T_effective 延长至 21-28 天；此边界条件需通过分位数回归模型验证。

## Corrected Claim

当市场流动性指数 L_market < 0.5 时，λ_decay 通常会降低，导致 T_effective 延长；具体降低幅度（如30-50%）和延长天数（如21-28天）需通过分位数回归模型在特定数据集中验证，而非固定理论值。

## Evidence

[质询]该陈述包含具体的经验性参数（λ_decay降低30-50%，T_effective延长至21-28天），这些数值并非从第一性原理或数学公理严格推导出的必然结果，而是依赖于特定市场微观结构模型的假设。虽然逻辑上流动性低导致衰减慢是合理的，但具体的百分比和天数范围缺乏普适的理论推导基础，属于经验事实范畴。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

market liquidity impact on intervention decay rate
