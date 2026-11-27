# N63: GTV最大化目标函数的约束条件：平台目标 max GT = Σ(P_deal * Q_deal) 受限于用户体验指标 UX_score，若高挂价导致的退货率 R

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

GTV最大化目标函数的约束条件：平台目标 max GT = Σ(P_deal * Q_deal) 受限于用户体验指标 UX_score，若高挂价导致的退货率 R_return > 15% 或差评率 R_neg > 5%，则算法会下调曝光权重，此时 β_platform 动态降低，需计算均衡点的动态稳定性。

## Corrected Claim

GTV最大化目标函数的约束条件：平台目标 max GT = Σ(P_deal * Q_deal) 受限于用户体验指标 UX_score，若高挂价导致的退货率 R_return > 15% 或差评率 R_neg > 5%，则算法会下调曝光权重，此时 β_platform 动态降低，需计算均衡点的动态稳定性。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

platform total transaction value optimization constraint return rate negative feedback algorithm adjustment
