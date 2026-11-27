# N71: 候选A对成交概率的修正：实施上限后，卖家实际定价 P_actual = min(P_ask, P_max)，导致价格分布左移，成交概率 P(Sale|P_act

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

候选A对成交概率的修正：实施上限后，卖家实际定价 P_actual = min(P_ask, P_max)，导致价格分布左移，成交概率 P(Sale|P_actual) 的积分下限从 P_median*(1.15) 降至 P_median*(1-k)，预期提升成交率 ΔP_sale = ∫_{P_median*(1-k)}^{∞} f(P) dP - ∫_{P_median*1.15}^{∞} f(P) dP。

## Corrected Claim

候选A对成交概率的修正：实施上限后，卖家实际定价 P_actual = min(P_ask, P_max)，导致价格分布左移，成交概率 P(Sale|P_actual) 的积分下限从 P_median*(1.15) 降至 P_median*(1-k)，预期提升成交率 ΔP_sale = ∫_{P_median*(1-k)}^{∞} f(P) dP - ∫_{P_median*1.15}^{∞} f(P) dP。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别处理了分布形态重构（截断效应）、期望值计算（总概率公式）以及决策边界分析（边际收益阈值），逻辑层层递进且互不重叠。子节点1定义了新的概率空间，子节点2基于该空间进行积分计算，子节点3对计算结果进行不等式分析以判断干预的有效性，三者共同完整覆盖了父节点中关于成交概率修正的数学推导过程，无冗余。）
