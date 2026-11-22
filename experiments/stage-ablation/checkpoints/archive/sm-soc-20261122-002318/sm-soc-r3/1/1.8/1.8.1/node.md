# N53: 卖家单方降价的边际收益增量 ΔE[Revenue] 由价格下降带来的成交概率提升决定：ΔE[Revenue] ≈ -ΔP * Prob(Sale) + P_ne

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

卖家单方降价的边际收益增量 ΔE[Revenue] 由价格下降带来的成交概率提升决定：ΔE[Revenue] ≈ -ΔP * Prob(Sale) + P_new * ΔProb(Sale)，其中 ΔProb(Sale) 是价格弹性系数 ε * (ΔP / P_old) * Prob(Sale)。

## Corrected Claim

卖家单方降价的边际收益增量 ΔE[Revenue] 由价格下降带来的成交概率提升决定：ΔE[Revenue] ≈ -ΔP * Prob(Sale) + P_new * ΔProb(Sale)，其中 ΔProb(Sale) 是价格弹性系数 ε * (ΔP / P_old) * Prob(Sale)。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了参数基准设定（子节点1）、核心公式的数值验证与逻辑推导（子节点2）、以及边界条件与外部变量（时间成本/信号效应）的修正（子节点3）。三者逻辑层层递进，分别对应‘参数’、‘计算’、‘修正/边界’，互不重叠且共同构成了对父节点公式的完整解释。虽然子节点2和3都涉及具体数值计算，但子节点2旨在验证基准情况下的理性，子节点3旨在探讨低弹性下的失效边界及引入新变量（C_wait），二者目的不同，不构成冗余。）
