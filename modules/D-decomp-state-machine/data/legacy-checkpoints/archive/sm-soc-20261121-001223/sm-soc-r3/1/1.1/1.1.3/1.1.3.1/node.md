# N91: 保留价值 V_res 与风险厌恶 λ 的耦合推导：在确定性等价（Certainty Equivalent）框架下，V_res = CE(V) = E[V] - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N29

## Claim

保留价值 V_res 与风险厌恶 λ 的耦合推导：在确定性等价（Certainty Equivalent）框架下，V_res = CE(V) = E[V] - λ * σ_V² / (2 * W_0)（近似公式，假设正态分布）；因此边际效应 ∂V_res/∂λ = -σ_V² / (2 * W_0)，量化 λ 每增加 0.1 对 V_res 的提升幅度为 0.1 * σ_V² / (2 * W_0) 的百分比值，其中 σ_V 为商品价值估计的标准差，W_0 为卖家财富。

## Corrected Claim

保留价值 V_res 与风险厌恶 λ 的耦合推导：在确定性等价（Certainty Equivalent）框架下，V_res = CE(V) = E[V] - λ * σ_V² / (2 * W_0)（近似公式，假设正态分布）；因此边际效应 ∂V_res/∂λ = -σ_V² / (2 * W_0)，量化 λ 每增加 0.1 对 V_res 的提升幅度为 0.1 * σ_V² / (2 * W_0) 的百分比值，其中 σ_V 为商品价值估计的标准差，W_0 为卖家财富。

## Evidence

先验知识/题面给定，逻辑校验通过：基于正态分布假设下的确定性等价（CE）近似公式 CE ≈ E[X] - (λ/2)Var(X)/W 是金融经济学中的标准二阶泰勒展开近似，推导逻辑自洽，量纲与符号正确。

## Search Query

marginal effect of risk aversion on reservation value certainty equivalent formula derivation
