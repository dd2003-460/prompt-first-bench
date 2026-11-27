# N390: 最小有效干预的约束条件验证：需验证 ΔP_comp ≥ 5% 是否成立。ΔP_comp = P_pre_display - P_post_display。若 P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N117

## Claim

最小有效干预的约束条件验证：需验证 ΔP_comp ≥ 5% 是否成立。ΔP_comp = P_pre_display - P_post_display。若 P_pre_display 为品类平均挂价 $100，则需 P_post_display ≤ $95。通过模拟 η_display 从 0 到 1 的变化，找到满足 ΔP_comp ≥ 5% 的最小 η_display 值。

## Corrected Claim

最小有效干预的约束条件验证：需验证 ΔP_comp ≥ 5% 是否成立。ΔP_comp = P_pre_display - P_post_display。若 P_pre_display 为品类平均挂价 $100，则需 P_post_display ≤ $95。通过模拟 η_display 从 0 到 1 的变化，找到满足 ΔP_comp ≥ 5% 的最小 η_display 值。

## Evidence

先验知识/题面给定，逻辑校验通过：ΔP_comp = P_pre - P_post，若 P_pre=100 且 ΔP_comp≥5，则 P_post≤95，数学推导自洽。

## Search Query

price compression effect of price transparency label simulation
