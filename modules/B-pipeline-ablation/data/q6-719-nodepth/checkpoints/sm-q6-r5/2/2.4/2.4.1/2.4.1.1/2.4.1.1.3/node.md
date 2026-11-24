# N569: 工作点C（低成本/高延迟）：偏远地区用户（占比10%）通过卫星/4G混合接入，平均跳数Hops=4，单跳延迟L_hop=2.0ms，总接入延迟L_access=

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N185

## Claim

工作点C（低成本/高延迟）：偏远地区用户（占比10%）通过卫星/4G混合接入，平均跳数Hops=4，单跳延迟L_hop=2.0ms，总接入延迟L_access=8.0ms，利用公有云CDN边缘节点兜底，单用户接入成本¥0（由公有云CDN费用覆盖），适合低ARPU值长尾用户群体。

## Corrected Claim

工作点C（低成本/高延迟）：偏远地区用户（占比10%）通过卫星/4G混合接入，平均跳数Hops=4，单跳延迟L_hop=2.0ms，总接入延迟L_access=8.0ms，利用公有云CDN边缘节点兜底，单用户接入成本¥0（由公有云CDN费用覆盖），适合低ARPU值长尾用户群体。

## Evidence

先验知识/题面给定，逻辑校验通过：4跳×2.0ms=8.0ms计算正确，卫星/4G混合接入偏远地区及CDN兜底符合工程常识，成本由CDN覆盖符合低ARPU长尾用户策略逻辑。
