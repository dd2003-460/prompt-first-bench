# N328: 买家对强制显示的均价标签的点击率提升系数 β_label：β_label = (CTR_with_label - CTR_without_label) / CT

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N105, N106, N107

## Claim

买家对强制显示的均价标签的点击率提升系数 β_label：β_label = (CTR_with_label - CTR_without_label) / CTR_without_label，预期值 [待核验]（基于透明度标签对买家决策摩擦的降低效应，通常在 0.1-0.3 区间）

## Corrected Claim

买家对强制显示的均价标签的点击率提升系数 β_label 定义为 (CTR_with_label - CTR_without_label) / CTR_without_label。具体数值取决于市场环境与标签设计，缺乏统一标准，需通过A/B测试实证确定，不宜直接预设固定区间。

## Evidence

[质询]该数值区间（0.1-0.3）属于经验性统计估计，缺乏第一性原理推导基础，且不同市场、品类及标签设计下波动极大，直接断言‘通常’在此区间存在过度概括风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该参数非数学/物理定律，不适用第一性原理验证条款）

## Search Query

price transparency label click through rate C2C platform experiment
