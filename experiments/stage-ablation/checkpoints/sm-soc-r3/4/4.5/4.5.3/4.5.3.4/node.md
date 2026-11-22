# N242: P_wtp 分布的尾部风险量化：P_wtp ~ N(μ_wtp, σ_wtp²)，临界条件 P_ask_new < P_wtp 的满足概率为 Φ((μ_wtp 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

P_wtp 分布的尾部风险量化：P_wtp ~ N(μ_wtp, σ_wtp²)，临界条件 P_ask_new < P_wtp 的满足概率为 Φ((μ_wtp - P_ask_new)/σ_wtp)；当 P_ask_new 接近 μ_wtp + 1.5σ_wtp 时，满足概率骤降至约 6.7%，意味着高溢价工作点下帕累托改进仅对少数高支付意愿买家成立，不具备市场普遍性。

## Corrected Claim

P_wtp 分布的尾部风险量化：P_wtp ~ N(μ_wtp, σ_wtp²)，临界条件 P_ask_new < P_wtp 的满足概率为 Φ((μ_wtp - P_ask_new)/σ_wtp)；当 P_ask_new 接近 μ_wtp + 1.5σ_wtp 时，满足概率骤降至约 6.7%，意味着高溢价工作点下帕累托改进仅对少数高支付意愿买家成立，不具备市场普遍性。

## Evidence

先验知识/题面给定，逻辑校验通过：正态分布性质推导正确，Φ(-1.5)≈0.0668，与6.7%一致
