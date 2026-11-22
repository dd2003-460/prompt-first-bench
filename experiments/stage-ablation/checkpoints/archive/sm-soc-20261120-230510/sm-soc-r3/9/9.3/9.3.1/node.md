# N295: L3置信度判定中'相对误差>30%'的基准定义：相对误差 = |Model_Prediction - Observed_Value| / |Observed_V

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N104

## Claim

L3置信度判定中'相对误差>30%'的基准定义：相对误差 = |Model_Prediction - Observed_Value| / |Observed_Value|，需明确分母是单次观测值还是样本均值，以及观测值的时间窗口（如7天滚动平均）以消除短期波动噪声。

## Corrected Claim

L3置信度判定中'相对误差>30%'的基准定义：相对误差 = |Model_Prediction - Observed_Value| / |Observed_Value|，需明确分母是单次观测值还是样本均值，以及观测值的时间窗口（如7天滚动平均）以消除短期波动噪声。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

relative error definition model validation time window rolling average
