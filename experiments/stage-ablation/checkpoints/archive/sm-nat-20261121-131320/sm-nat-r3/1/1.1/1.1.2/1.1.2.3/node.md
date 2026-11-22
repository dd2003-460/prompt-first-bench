# N66: 工作点 C（极端敏感性）：取 S_max = 10GB，此时积分截断误差 < 0.01%，但计算复杂度显著增加，适用于理论极限分析。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

工作点 C（极端敏感性）：取 S_max = 10GB，此时积分截断误差 < 0.01%，但计算复杂度显著增加，适用于理论极限分析。

## Corrected Claim

工作点 C（极端敏感性）：取 S_max = 10GB，此时积分截断误差 < 0.01%，但计算复杂度显著增加，适用于理论极限分析。

## Evidence

先验知识/题面给定，逻辑校验通过：增大积分上限 S_max 确实会减小截断误差并增加计算复杂度，符合数值积分基本原理。
