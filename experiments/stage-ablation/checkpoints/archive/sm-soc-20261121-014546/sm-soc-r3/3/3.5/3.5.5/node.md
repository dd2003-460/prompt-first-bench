# N79: 卖家成交概率提升率 Δp：成交概率 p 随价格接近真实价值 V 而增加，假设 p = p_0 * exp(-γ_price * (P_ask - V))。当 P

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

卖家成交概率提升率 Δp：成交概率 p 随价格接近真实价值 V 而增加，假设 p = p_0 * exp(-γ_price * (P_ask - V))。当 P_ask 下移 10% V，Δp/p = 1 - exp(-γ_price * 0.1)。若 γ_price = 2.5，则 Δp ≈ 22%，接近预期的 25%。

## Corrected Claim

卖家成交概率提升率 Δp：成交概率 p 随价格接近真实价值 V 而增加，假设 p = p_0 * exp(-γ_price * (P_ask - V))。当 P_ask 下移 10% V，Δp/p = 1 - exp(-γ_price * 0.1)。若 γ_price = 2.5，则 Δp ≈ 22%，接近预期的 25%。

## Evidence

父节点级核验未通过：不完备（子节点之间存在逻辑包含关系（非严格正交）且覆盖不全。子节点1（γ_price估计）和子节点2（σ_buyer量化）在数学上高度耦合，因为σ_buyer实际上定义了γ_price的有效作用域或截断点，二者并非独立参数；此外，父节点明确给出了具体的数值推导（P_ask下移10%，Δp≈22%），但子节点仅提供了公式和定性描述，缺失了该具体数值场景的计算验证或推导步骤，导致关键方面覆盖不完整。）
