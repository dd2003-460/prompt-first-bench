# N72: 可信性约束条件：高价信号仅在 C_signal > C_mimic 时可信，其中 C_mimic 是低质量卖家模仿高价的成本。由于低质量卖家无法承担长期持有成本

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

可信性约束条件：高价信号仅在 C_signal > C_mimic 时可信，其中 C_mimic 是低质量卖家模仿高价的成本。由于低质量卖家无法承担长期持有成本 C_wait 或拒绝交易的成本 C_rejection，其模仿概率 P_mimic 趋近于 0，从而使得 k_trust ≈ 1.2 的信任提升系数在统计上显著。

## Corrected Claim

可信性约束条件：高价信号仅在 C_signal > C_mimic 时可信，其中 C_mimic 是低质量卖家模仿高价的成本。由于低质量卖家无法承担长期持有成本 C_wait 或拒绝交易的成本 C_rejection，其模仿概率 P_mimic 趋近于 0，从而使得 k_trust ≈ 1.2 的信任提升系数在统计上显著。

## Evidence

先验知识/题面给定，逻辑校验通过：信号博弈中模仿成本高于收益导致模仿概率趋零，从而支撑信任系数显著性，逻辑自洽。

## Search Query

costly signaling theory lemons market mimicry cost
