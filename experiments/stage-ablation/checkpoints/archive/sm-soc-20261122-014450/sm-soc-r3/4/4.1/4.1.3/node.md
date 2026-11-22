# N72: 最小干预成本 C_intervention 中的 ΔP, ΔT, ΔQ 需通过反事实推断（Counterfactual Inference）估计：即假设实施干预

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N16

## Claim

最小干预成本 C_intervention 中的 ΔP, ΔT, ΔQ 需通过反事实推断（Counterfactual Inference）估计：即假设实施干预后，市场参数相对于无干预基线的变化量，需量化基线波动率以排除噪声干扰。

## Corrected Claim

最小干预成本 C_intervention 中的 ΔP, ΔT, ΔQ 需通过反事实推断（Counterfactual Inference）估计：即假设实施干预后，市场参数相对于无干预基线的变化量，需量化基线波动率以排除噪声干扰。

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应保守、基准、激进三种不同的反事实推断策略（不同方法论与置信水平），彼此在方法论、参数取值和应用场景上互斥且互补，无逻辑矛盾或内容重叠。它们共同覆盖了父节点中关于‘估计方法’、‘基线波动率设定’及‘不确定性量化’的关键方面，且每个节点代表一个独立的决策工作点，而非同一参数的简单变体，因此不视为冗余。）
