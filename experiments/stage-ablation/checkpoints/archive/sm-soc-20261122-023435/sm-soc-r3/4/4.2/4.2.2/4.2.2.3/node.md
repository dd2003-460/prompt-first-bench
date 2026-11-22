# N167: 预期边际收益 E[Margin|t] 的时间衰减函数：E[Margin|t] = Margin_0 * exp(-γ * t)，其中 γ 为收益衰减率，与 ε_

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

预期边际收益 E[Margin|t] 的时间衰减函数：E[Margin|t] = Margin_0 * exp(-γ * t)，其中 γ 为收益衰减率，与 ε_b 正相关，γ ≈ ε_b * k_decay，k_decay 为品类特定的衰减系数（通常 0.1-0.3/天）。

## Corrected Claim

预期边际收益 E[Margin|t] 的时间衰减函数：E[Margin|t] = Margin_0 * exp(-γ * t)，其中 γ 为收益衰减率，与 ε_b 正相关，γ ≈ ε_b * k_decay，k_decay 为品类特定的衰减系数（通常 0.1-0.3/天）。

## Evidence

先验知识/题面给定，逻辑校验通过
