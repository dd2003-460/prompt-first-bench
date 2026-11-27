# N135: I_asym 的阈值敏感性分析：当 I_asym 从 0.5 变化到 0.2 时，买家价格敏感度 E_price 的变化幅度 ΔE = E(0.5) - E(0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N33

## Claim

I_asym 的阈值敏感性分析：当 I_asym 从 0.5 变化到 0.2 时，买家价格敏感度 E_price 的变化幅度 ΔE = E(0.5) - E(0.2)，假设 E(0.5) = 2.0, E(0.2) = 1.2，则 ΔE = 0.8，表明信息不对称度每降低 0.1，价格敏感度降低 0.267。

## Corrected Claim

I_asym 的阈值敏感性分析：当 I_asym 从 0.5 变化到 0.2 时，买家价格敏感度 E_price 的变化幅度 ΔE = E(0.5) - E(0.2)，假设 E(0.5) = 2.0, E(0.2) = 1.2，则 ΔE = 0.8，表明信息不对称度每降低 0.1，价格敏感度降低 0.267。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算正确（2.0-1.2=0.8，0.8/3≈0.267），线性假设在局部敏感性分析中合理。

## Search Query

information asymmetry threshold price elasticity sensitivity analysis
