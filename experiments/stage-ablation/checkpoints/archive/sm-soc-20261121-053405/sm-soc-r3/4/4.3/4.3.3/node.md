# N70: ΔR 的完整计算式：$\Delta R = (P_{list} - P_{clear}) \times Q_{base} \times 0.36$。其中 $P_

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

ΔR 的完整计算式：$\Delta R = (P_{list} - P_{clear}) \times Q_{base} \times 0.36$。其中 $P_{list} - P_{clear}$ 为价格溢价幅度（题面给定为 15-25%，取中值 20%），$Q_{base}$ 为未干预下的基准成交量。最终伤害程度量化为 $\Delta R / R_{old} \approx 0.2 \times 0.36 = 7.2\%$ 的收益损失。

## Corrected Claim

ΔR 的完整计算式：$\Delta R = (P_{list} - P_{clear}) \times Q_{base} \times 0.36$。其中 $P_{list} - P_{clear}$ 为价格溢价幅度（题面给定为 15-25%，取中值 20%），$Q_{base}$ 为未干预下的基准成交量。最终伤害程度量化为 $\Delta R / R_{old} \approx 0.2 \times 0.36 = 7.2\%$ 的收益损失。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别对应公式中的三个核心变量：$Q_{base}$（流量基数）、价格溢价区间（价格因子）和 0.36 系数（行为修正因子）。三者分别处理数据估计、敏感性分析和模型非线性修正，维度互斥且无重复，共同构成了父节点公式的完整解释。）
