# N34: 买家策略‘放弃’的触发概率：P(Abort) = 1 - exp(-(P_ask - P_market)/σ_price)，其中 σ_price 为买家对价格偏

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

买家策略‘放弃’的触发概率：P(Abort) = 1 - exp(-(P_ask - P_market)/σ_price)，其中 σ_price 为买家对价格偏差的容忍度标准差（假设 σ_price ≈ 0.1 * P_market），当 P_ask > P_market * 1.25 时，P(Abort) > 0.9，表明极端高挂价将直接导致买家退出策略空间。

## Corrected Claim

买家策略‘放弃’的触发概率：P(Abort) = 1 - exp(-(P_ask - P_market)/σ_price)，其中 σ_price 为买家对价格偏差的容忍度标准差（假设 σ_price ≈ 0.1 * P_market），当 P_ask > P_market * 1.25 时，P(Abort) > 0.9，表明极端高挂价将直接导致买家退出策略空间。

## Evidence

先验知识/题面给定，逻辑校验通过：代入 σ_price = 0.1 * P_market 及 P_ask = 1.25 * P_market，计算得 P(Abort) = 1 - exp(-2.5) ≈ 0.918 > 0.9，数学推导自洽。
