# N158: Pareto(β=0.9) 热度分布下，前 K 个对象的总热度占比 H_head(K) = (1 - K^{1-β}) / (1 - N^{1-β})，由于 β

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N57

## Claim

Pareto(β=0.9) 热度分布下，前 K 个对象的总热度占比 H_head(K) = (1 - K^{1-β}) / (1 - N^{1-β})，由于 β=0.9<1，分母项 N^{0.1} 约为 6.3，分子项随 K 变化。

## Corrected Claim

Pareto(β=0.9) 热度分布下，前 K 个对象的总热度占比 H_head(K) = (1 - K^{1-β}) / (1 - N^{1-β})，由于 β=0.9<1，分母项 N^{0.1} 约为 6.3，分子项随 K 变化。

## Evidence

先验知识/题面给定，逻辑校验通过：Pareto分布累积和公式推导正确，且N=1000时N^0.1≈6.31，数值量级合理。
