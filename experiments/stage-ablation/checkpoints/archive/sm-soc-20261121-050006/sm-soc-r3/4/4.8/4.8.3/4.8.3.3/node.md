# N299: “降价-补偿-再涨价”循环的迭代成本：每次循环的净收益 ΔR_cycle = V_comp - (P_old - P_new) * Q_expected + C

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N94

## Claim

“降价-补偿-再涨价”循环的迭代成本：每次循环的净收益 ΔR_cycle = V_comp - (P_old - P_new) * Q_expected + C_relist，其中 C_relist 为重新上架的摩擦成本（时间+精力，估算 5-10 元）；当 ΔR_cycle < 0 时，策略性循环停止，需通过追踪卖家价格变动频率实证验证该阈值。

## Corrected Claim

“降价-补偿-再涨价”循环的迭代成本模型：在简化假设下，每次循环的净收益可近似表示为 ΔR_cycle ≈ V_comp - (P_old - P_new) * Q_expected + C_relist，其中 C_relist 为重新上架的摩擦成本（具体数值需根据平台规则及卖家时间成本实证估算）；当 ΔR_cycle < 0 时，策略性循环停止。该阈值需通过追踪特定卖家价格变动频率及实际成本进行实证验证。

## Evidence

[质询]该公式将复杂的动态博弈简化为静态线性模型，忽略了价格弹性、库存损耗及市场反应滞后等关键变量，且C_relist的5-10元估算缺乏普遍适用的实证基础，属于过度简化的经验假设。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该模型为特定场景下的简化假设，非第一性原理可推导的普适真理）

## Search Query

price cycling behavior sellers platform incentives empirical evidence
