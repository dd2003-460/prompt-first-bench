# N63: 信号破坏后的买家瑕疵概率重估机制：买家对瑕疵概率的后验更新 P(defect|price_drop) = P(defect|prior) * (1 + γ * 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N12

## Claim

信号破坏后的买家瑕疵概率重估机制：买家对瑕疵概率的后验更新 P(defect|price_drop) = P(defect|prior) * (1 + γ * (ΔP/P)^η)，其中γ为价格-质量关联强度，η为非线性指数（通常η>1表示边际效应递减），需确定γ和η的基准值以解释为何仅10%降价导致咨询概率下降60%

## Corrected Claim

信号破坏后的买家瑕疵概率重估机制：买家对瑕疵概率的后验更新 P(defect|price_drop) = P(defect|prior) * (1 + γ * (ΔP/P)^η)，其中γ为价格-质量关联强度，η为非线性指数（通常η>1表示边际效应递减），需确定γ和η的基准值以解释为何仅10%降价导致咨询概率下降60%

## Evidence

先验知识/题面给定，逻辑校验通过
