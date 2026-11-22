# N72: 可信性约束条件：高价信号仅在 C_signal > C_mimic 时可信，其中 C_mimic 是低质量卖家模仿高价的成本。由于低质量卖家无法承担长期持有成本

- **status**: pending
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

父节点级核验未通过：不完备（子节点1聚焦于C_mimic的成本构成，子节点2聚焦于均衡边界条件及P_mimic=0的推导前提，两者角度不同且无重复。但父节点中提到的关键结论'k_trust ≈ 1.2的信任提升系数在统计上显著'以及'由于低质量卖家无法承担...成本'的逻辑链条在子节点中未得到充分覆盖，子节点2虽提到P_mimic=0，但未解释为何这导致k_trust显著，存在关键逻辑环节缺失。）

## Search Query

costly signaling theory lemons market mimicry cost
