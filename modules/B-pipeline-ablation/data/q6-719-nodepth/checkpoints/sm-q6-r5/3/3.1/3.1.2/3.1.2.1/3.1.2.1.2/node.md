# N633: 工作点A的电力成本敏感性系数 E_power = (ΔC_power / C_power) / (ΔPUE / PUE)，当PUE从1.4降至1.2（优化制冷）

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N211

## Claim

工作点A的电力成本敏感性系数 E_power = (ΔC_power / C_power) / (ΔPUE / PUE)，当PUE从1.4降至1.2（优化制冷）时，C_power从¥655.68降至¥564.86，降幅13.8%；若电价从¥0.8升至¥1.0，C_power升至¥819.60，增幅25%。

## Corrected Claim

工作点A的电力成本敏感性系数 E_power = (ΔC_power / C_power) / (ΔPUE / PUE)，当PUE从1.4降至1.2（优化制冷）时，C_power从¥655.68降至¥564.86，降幅13.8%；若电价从¥0.8升至¥1.0，C_power升至¥819.60，增幅25%。

## Evidence

先验知识/题面给定，逻辑校验通过：PUE从1.4降至1.2（降幅14.29%）导致电力成本从655.68降至564.86（降幅13.85%），符合PUE与电力成本正相关的物理直觉；电价从0.8升至1.0（增幅25%）导致电力成本从655.68升至819.60（增幅25%），符合线性比例关系。数值量级与逻辑自洽。

## Search Query

data center PUE optimization electricity cost sensitivity analysis
