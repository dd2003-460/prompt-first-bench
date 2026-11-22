# N226: 价格公平性指数 Price_Fairness_Index 的构造：定义为 1 - |P_listed - P_median| / P_median，取值范围[0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

价格公平性指数 Price_Fairness_Index 的构造：定义为 1 - |P_listed - P_median| / P_median，取值范围[0,1]，值越高表示价格越接近市场公允价。

## Corrected Claim

价格公平性指数 Price_Fairness_Index 的构造：定义为 1 - |P_listed - P_median| / P_median，取值范围[0,1]，值越高表示价格越接近市场公允价。

## Evidence

先验知识/题面给定，逻辑校验通过：该指数定义为 1 - 相对偏差，当价格等于中位数时值为1，偏差越大值越小，符合[0,1]区间及越高越接近公允价的逻辑。
