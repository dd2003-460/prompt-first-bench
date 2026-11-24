# N633: 维修成本敏感性分析：单次维修成本 Repair_Cost = Parts_Cost + Labor_Cost，中值 ¥2,250（¥1,500 + ¥750）；

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N217

## Claim

维修成本敏感性分析：单次维修成本 Repair_Cost = Parts_Cost + Labor_Cost，中值 ¥2,250（¥1,500 + ¥750）；若采用高可靠性硬件（MTBF 翻倍）和自动化运维（Labor_Cost=0），Repair_Cost 降至 ¥1,500，但硬件 CapEx 增加 30%；需计算 3 年 TCO 比较：高可靠性方案 TCO = 1.3 × CapEx + (0.5 × Failure_Rate × ¥1,500)，标准方案 TCO = CapEx + (Failure_Rate × ¥2,250)。

## Corrected Claim

维修成本敏感性分析：单次维修成本 Repair_Cost = Parts_Cost + Labor_Cost，中值 ¥2,250（¥1,500 + ¥750）；若采用高可靠性硬件（MTBF 翻倍）和自动化运维（Labor_Cost=0），Repair_Cost 降至 ¥1,500，但硬件 CapEx 增加 30%；需计算 3 年 TCO 比较：高可靠性方案 TCO = 1.3 × CapEx + (0.5 × Failure_Rate × ¥1,500)，标准方案 TCO = CapEx + (Failure_Rate × ¥2,250)。

## Evidence

先验知识/题面给定，逻辑校验通过：成本构成公式及TCO推导逻辑自洽，数值量级合理，无内部矛盾。
