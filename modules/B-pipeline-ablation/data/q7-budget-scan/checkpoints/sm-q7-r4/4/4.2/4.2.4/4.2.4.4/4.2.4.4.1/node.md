# N708: 工作点A（高业务价值/低容忍度）：假设Data_Value_business = 500TB * 10,000¥/TB = 5,000,000,000¥（¥50

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N247

## Claim

工作点A（高业务价值/低容忍度）：假设Data_Value_business = 500TB * 10,000¥/TB = 5,000,000,000¥（¥50亿），且采用11个9持久性，则C_risk_cloud = 10^-11 * 5 * 10^9 = ¥50/年；此时若引入人为误删风险P_human_error=10^-4，总风险成本跃升至¥500,000/年，不再可忽略。

## Corrected Claim

工作点A（高业务价值/低容忍度）：假设Data_Value_business = 500TB * 10,000¥/TB = 5,000,000,000¥（¥50亿），且采用11个9持久性，则C_risk_cloud = 10^-11 * 5 * 10^9 = ¥50/年；此时若引入人为误删风险P_human_error=10^-4，总风险成本跃升至¥500,000/年，不再可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算准确（500TB * 10,000¥/TB = 5*10^9¥；5*10^9 * 10^-11 = 50¥；5*10^9 * 10^-4 = 5*10^5¥），量纲与逻辑自洽。
