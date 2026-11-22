# N29: 驱动方判定的敏感性分析：若平台算法权重中‘成交速度’对曝光量的影响系数 w_speed 高于‘价格竞争力’系数 w_price (即 w_speed/w_pri

- **status**: degraded
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N5

## Claim

驱动方判定的敏感性分析：若平台算法权重中‘成交速度’对曝光量的影响系数 w_speed 高于‘价格竞争力’系数 w_price (即 w_speed/w_price > 2)，则平台是主要驱动方。该比值可通过 A/B 测试中曝光量变化对价格变动和成交时间变动的弹性比来量化，当前估计比值为 2.5 [待核验]。

## Corrected Claim

驱动方判定的敏感性分析：若平台算法权重中‘成交速度’对曝光量的影响系数 w_speed 高于‘价格竞争力’系数 w_price (即 w_speed/w_price > 2)，则平台是主要驱动方。该比值可通过 A/B 测试中曝光量变化对价格变动和成交时间变动的弹性比来量化，当前估计比值约为 2.5（需进一步实证验证）。

## Evidence

[质询]该陈述包含具体的经验性数值估计（比值为2.5）和特定的因果机制假设（成交速度对曝光量的影响系数高于价格竞争力），这属于平台算法内部参数，无法从第一性原理或数学公理中严格推导出来，且缺乏外部来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

algorithmic exposure weight on transaction speed vs price competitiveness
