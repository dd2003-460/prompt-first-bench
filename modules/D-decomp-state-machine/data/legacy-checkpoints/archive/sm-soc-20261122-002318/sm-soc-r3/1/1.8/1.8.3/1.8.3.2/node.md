# N160: 离散定价约束下的均衡跳跃 (Discrete Pricing Jump) 量化：由于卖家通常以整数或特定步长 (如 50 元) 定价，连续最优解 P* 可能落在

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

离散定价约束下的均衡跳跃 (Discrete Pricing Jump) 量化：由于卖家通常以整数或特定步长 (如 50 元) 定价，连续最优解 P* 可能落在两个离散价格点 P_low 和 P_high 之间。若 P* 更接近 P_low 但 P_high 带来的期望收益增量 ΔE > 交易概率下降损失，则均衡跳跃至 P_high。量化条件为：(P_high - P_low) * Prob(Sale|P_low) > P_low * (Prob(Sale|P_low) - Prob(Sale|P_high))。

## Corrected Claim

离散定价约束下的均衡跳跃 (Discrete Pricing Jump) 量化：由于卖家通常以整数或特定步长 (如 50 元) 定价，连续最优解 P* 可能落在两个离散价格点 P_low 和 P_high 之间。若 P* 更接近 P_low 但 P_high 带来的期望收益增量 ΔE > 交易概率下降损失，则均衡跳跃至 P_high。量化条件为：(P_high - P_low) * Prob(Sale|P_low) > P_low * (Prob(Sale|P_low) - Prob(Sale|P_high))。

## Evidence

先验知识/题面给定，逻辑校验通过：该不等式正确描述了离散定价下，选择较高价格 P_high 优于 P_low 的期望收益条件（即价格增量带来的收益大于概率下降导致的损失）。

## Search Query

Discrete pricing equilibrium jump condition second hand market
