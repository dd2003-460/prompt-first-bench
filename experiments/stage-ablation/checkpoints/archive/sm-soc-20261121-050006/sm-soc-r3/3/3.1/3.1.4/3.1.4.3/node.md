# N235: 咨询率提升目标达成条件：当 ΔQ ≥ 0.20 时，需满足 α_label * (1 - P(IgnoreLabel)) ≥ 0.20；若 α_label = 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N71

## Claim

咨询率提升目标达成条件：当 ΔQ ≥ 0.20 时，需满足 α_label * (1 - P(IgnoreLabel)) ≥ 0.20；若 α_label = 0.25，则要求 P(IgnoreLabel) ≤ 0.20；若 P(IgnoreLabel) > 0.5，则 ΔQ < 0.125，无法达到 20-30% 的提升目标，此时需重新评估标签设计或增加激励。

## Corrected Claim

咨询率提升目标达成条件：当 ΔQ ≥ 0.20 时，需满足 α_label * (1 - P(IgnoreLabel)) ≥ 0.20；若 α_label = 0.25，则要求 P(IgnoreLabel) ≤ 0.20；若 P(IgnoreLabel) > 0.5，则 ΔQ < 0.125，无法达到 20-30% 的提升目标，此时需重新评估标签设计或增加激励。

## Evidence

先验知识/题面给定，逻辑校验通过：数学推导显示 0.25 * (1 - 0.20) = 0.20 且 0.25 * (1 - 0.5) = 0.125，数值与逻辑关系自洽。

## Search Query

inquiry rate improvement threshold label effectiveness target
