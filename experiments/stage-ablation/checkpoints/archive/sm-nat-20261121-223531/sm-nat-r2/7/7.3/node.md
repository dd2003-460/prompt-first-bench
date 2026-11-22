# N75: Pareto(β=0.9)分布的无均值特性验证：均值 $E[H] = \frac{\beta-1}{\beta-2} h_{min}$，当 $\beta=0.9

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N23

## Claim

Pareto(β=0.9)分布的无均值特性验证：均值 $E[H] = \frac{\beta-1}{\beta-2} h_{min}$，当 $\beta=0.9$ 时，分母为负，分子为正，均值发散，表明热度分布极度长尾，前1%对象的热度权重远高于其余99%，导致LFU策略在理论上能显著提升命中率，但实际增益受限于频率估计误差。

## Corrected Claim

Pareto(β=0.9)分布的无均值特性验证：均值 $E[H] = \frac{\beta-1}{\beta-2} h_{min}$，当 $\beta=0.9$ 时，分母为负，分子为正，均值发散，表明热度分布极度长尾，前1%对象的热度权重远高于其余99%，导致LFU策略在理论上能显著提升命中率，但实际增益受限于频率估计误差。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布均值公式在β<2时发散，β=0.9符合该条件，长尾特性与LFU理论优势推导逻辑自洽。
