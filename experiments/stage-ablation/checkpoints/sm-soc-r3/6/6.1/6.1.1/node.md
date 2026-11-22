# N297: α_scarcity 的校准方法：通过 A/B 测试中不同溢价梯度（10%, 15%, 20%, 25%）下的瑕疵点击率数据，回归 ΔT_defect = α_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N101

## Claim

α_scarcity 的校准方法：通过 A/B 测试中不同溢价梯度（10%, 15%, 20%, 25%）下的瑕疵点击率数据，回归 ΔT_defect = α_scarcity * (P_ask/P_median - 1)^β，其中 α_scarcity 为稀缺性敏感度系数，需通过最小二乘法估计，假设 α_scarcity=0.5，该参数直接决定瑕疵容忍度提升的边际效应强度。

## Corrected Claim

α_scarcity 的校准方法：通过 A/B 测试中不同溢价梯度（10%, 15%, 20%, 25%）下的瑕疵点击率数据，回归 ΔT_defect = α_scarcity * (P_ask/P_median - 1)^β，其中 α_scarcity 为稀缺性敏感度系数，需通过最小二乘法估计，假设 α_scarcity=0.5，该参数直接决定瑕疵容忍度提升的边际效应强度。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

scarcity sensitivity coefficient calibration A/B test defect tolerance e-commerce
