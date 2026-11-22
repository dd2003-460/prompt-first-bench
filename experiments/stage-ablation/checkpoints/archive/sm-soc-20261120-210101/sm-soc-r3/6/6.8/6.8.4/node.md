# N377: μ_signal 的操作化定义：μ_signal = E[Credit_Score | ΔP ∈ [15%, 25%] & T_deal < T_median]

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N110, N114, N115

## Claim

μ_signal 的操作化定义：μ_signal = E[Credit_Score | ΔP ∈ [15%, 25%] & T_deal < T_median]，即高溢价且快速成交商品的卖家信用分均值。该值需通过数据库查询近90天数据计算，作为SNR分子中的信号均值。

## Corrected Claim

μ_signal 的操作化定义通常涉及高溢价且快速成交商品的卖家信用分均值，具体阈值（如溢价区间、时间窗口）需依据特定业务规则或数据库配置确定，而非固定为[15%, 25%]和90天。

## Evidence

[质询]该陈述包含具体的业务逻辑参数（如溢价区间[15%, 25%]、时间窗口90天、中位数成交时间阈值），这些属于经验性业务规则或特定系统配置，无法从第一性原理或数学公理中严格推导出来。若缺乏具体文档或代码支持，这些具体数值和条件组合可能不准确或过时。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且具体业务参数无法从第一性原理推出）

## Search Query

seller credit score distribution high price premium fast transaction used goods platform
