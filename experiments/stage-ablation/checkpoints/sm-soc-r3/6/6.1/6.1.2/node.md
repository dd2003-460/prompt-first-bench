# N298: β 的校准方法：通过 A/B 测试中不同溢价梯度下的瑕疵点击率数据，回归 ΔT_defect = α_scarcity * (P_ask/P_median - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N101

## Claim

β 的校准方法：通过 A/B 测试中不同溢价梯度下的瑕疵点击率数据，回归 ΔT_defect = α_scarcity * (P_ask/P_median - 1)^β，其中 β 为非线性指数，需通过非线性最小二乘法估计，假设 β=1.2，该参数决定容忍度提升的边际效应递减/递增特征。

## Corrected Claim

β 的校准方法：通过 A/B 测试中不同溢价梯度下的瑕疵点击率数据，回归 ΔT_defect = α_scarcity * (P_ask/P_median - 1)^β，其中 β 为非线性指数，需通过非线性最小二乘法估计，假设 β=1.2，该参数决定容忍度提升的边际效应递减/递增特征。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

nonlinear exponent calibration defect tolerance premium gradient e-commerce
