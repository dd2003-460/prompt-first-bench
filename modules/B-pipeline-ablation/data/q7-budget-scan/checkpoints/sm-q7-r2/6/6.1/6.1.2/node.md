# N79: 年增长率 g 的敏感性区间：基于数据湖典型增长模式，假设 g 在 5% 到 20% 之间。当 g=5% 时，3年后数据量为 579TB；当 g=20% 时，3年

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

年增长率 g 的敏感性区间：基于数据湖典型增长模式，假设 g 在 5% 到 20% 之间。当 g=5% 时，3年后数据量为 579TB；当 g=20% 时，3年后数据量为 864TB。需计算不同 g 值下三种方案的总成本变化斜率。

## Corrected Claim

年增长率 g 的敏感性区间：基于数据湖典型增长模式，假设 g 在 5% 到 20% 之间。当 g=5% 时，3年后数据量为 579TB；当 g=20% 时，3年后数据量为 864TB。需计算不同 g 值下三种方案的总成本变化斜率。

## Evidence

先验知识/题面给定，逻辑校验通过：假设初始数据量为500TB，则500*(1.05)^3≈578.9TB≈579TB，500*(1.20)^3=864TB，数值计算准确且符合复利增长逻辑。

## Search Query

data lake growth rate benchmark 5% 20%
