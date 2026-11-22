# N126: ΔP_expected 的贝叶斯后验均值计算：在买家已观察 n 个商品后，剩余发现更低价的期望收益 ΔP_expected = E[P_market - min

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N43

## Claim

ΔP_expected 的贝叶斯后验均值计算：在买家已观察 n 个商品后，剩余发现更低价的期望收益 ΔP_expected = E[P_market - min(P_remaining)]，需基于当前已见价格分布的尾部截断进行计算，而非简单的市场均价差。

## Corrected Claim

ΔP_expected 的贝叶斯后验均值计算：在买家已观察 n 个商品后，剩余发现更低价的期望收益 ΔP_expected = E[P_market - min(P_remaining)]，需基于当前已见价格分布的尾部截断进行计算，而非简单的市场均价差。

## Evidence

先验知识/题面给定，逻辑校验通过：基于已见价格分布进行尾部截断以计算剩余最小值的期望，符合贝叶斯推断及极值理论的基本逻辑，量纲与定义自洽。

## Search Query

Bayesian posterior expected gain search stopping rule
