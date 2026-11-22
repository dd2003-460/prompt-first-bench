# N193: P_ignored 的行为学代理变量构建：由于无法直接观测‘忽略’意图，使用‘加购后未购买’或‘收藏后 7 天无点击’作为 P_ignored 的代理；定义 P

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N71

## Claim

P_ignored 的行为学代理变量构建：由于无法直接观测‘忽略’意图，使用‘加购后未购买’或‘收藏后 7 天无点击’作为 P_ignored 的代理；定义 P_ignored_proxy = (N_cart_abandon + N_favorite_inactive) / N_viewed；需验证该代理变量与后续‘降价后无咨询’的相关性，若 Pearson ρ > 0.5，则支持锚定惯性假设。

## Corrected Claim

P_ignored 的行为学代理变量构建：由于无法直接观测‘忽略’意图，使用‘加购后未购买’或‘收藏后 7 天无点击’作为 P_ignored 的代理；定义 P_ignored_proxy = (N_cart_abandon + N_favorite_inactive) / N_viewed；需验证该代理变量与后续‘降价后无咨询’的相关性，若 Pearson ρ > 0.5，则支持锚定惯性假设。

## Evidence

先验知识/题面给定，逻辑校验通过
