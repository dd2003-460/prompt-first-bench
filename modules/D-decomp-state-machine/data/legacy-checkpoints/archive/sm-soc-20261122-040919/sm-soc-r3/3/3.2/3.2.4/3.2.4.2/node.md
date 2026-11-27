# N266: 动态降价策略的触发阈值 T_threshold：卖家在成交周期超过 T_threshold 时自动降价。T_threshold 的分布取决于卖家的风险偏好和资金

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N72

## Claim

动态降价策略的触发阈值 T_threshold：卖家在成交周期超过 T_threshold 时自动降价。T_threshold 的分布取决于卖家的风险偏好和资金压力，通常服从对数正态分布，均值约为初始预期成交周期的 1.5 倍。

## Corrected Claim

动态降价策略的触发阈值 T_threshold 通常服从对数正态分布，其均值与初始预期成交周期的比值取决于卖家的风险偏好和资金压力，具体倍数需根据市场实证数据确定。

## Evidence

[质询]「均值约为初始预期成交周期的 1.5 倍」这一具体数值缺乏普适性，属于高度依赖特定市场环境和卖家群体的经验参数，无法从第一性原理严格推导，且不同风险偏好下的分布形态差异巨大，固定倍数缺乏理论支撑。 | source=knowledge，逻辑自洽（对数正态分布常用于描述正偏态的时间/价格数据），但具体倍数 1.5 为经验估计，无来源直接支持，依据经验事实排除条款降级。

## Search Query

dynamic pricing strategy threshold second hand market
