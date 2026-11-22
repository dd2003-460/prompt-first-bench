# N261: 高价值商品（单价 > 5000 元）的尾部风险实证检验：统计成交溢价超过 15% 的订单中，高价值商品占比 OVR_high_value 与低价值商品占比 OV

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N93

## Claim

高价值商品（单价 > 5000 元）的尾部风险实证检验：统计成交溢价超过 15% 的订单中，高价值商品占比 OVR_high_value 与低价值商品占比 OVR_low_value 的差异。若 OVR_high_value 显著高于正态分布预测值，则证实右尾更厚（Heavy-tail），需采用 Pareto 或 Log-normal 分布替代正态分布进行 VOI 计算。

## Corrected Claim

高价值商品（单价 > 5000 元）的尾部风险实证检验：统计成交溢价超过 15% 的订单中，高价值商品占比 OVR_high_value 与低价值商品占比 OVR_low_value 的差异。若实证数据显示 OVR_high_value 显著高于正态分布预测值，则表明右尾更厚（Heavy-tail），建议采用 Pareto 或 Log-normal 分布替代正态分布进行 VOI 计算。

## Evidence

[质询]该陈述包含具体的实证数据结论（如'显著高于正态分布预测值'、'证实右尾更厚'），属于经验事实。在缺乏具体数据集、样本量及统计检验结果（如p值、置信区间）的情况下，无法验证该特定实证结论的真实性，且不同市场或时间段的数据可能得出不同结论。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体实证结论）

## Search Query

heavy tail distribution high value used goods price premium excess kurtosis
