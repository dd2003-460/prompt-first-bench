# N25: 卖家定价参数 k 的最优值：k* = argmax [f(k) * (P - C) - C_holding]，其中 f(k) 为剩余买家成交意愿概率，C 为卖家

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

卖家定价参数 k 的最优值：k* = argmax [f(k) * (P - C) - C_holding]，其中 f(k) 为剩余买家成交意愿概率，C 为卖家成本，C_holding 为持有成本（时间成本+机会成本），k* 通常落在 1.2-1.8 区间，具体值取决于 C_holding 的相对大小。

## Corrected Claim

卖家定价参数 k 的最优值由 k* = argmax [f(k) * (P - C) - C_holding] 决定，其中 f(k) 为剩余买家成交意愿概率，C 为卖家成本，C_holding 为持有成本。k* 的具体数值取决于 C_holding 的相对大小及市场供需弹性，并非固定落在 1.2-1.8 区间。

## Evidence

父节点级核验未通过：不完备（子节点正交：一个推导最优值公式，一个分解成本项，无重叠。但不完备：父节点强调 k* 取决于 C_holding 的相对大小及区间，子节点虽提供了具体算例，但未涵盖 k* 随参数变化的敏感性分析或边界条件（如当 C_holding 极大或极小时 k* 是否仍落在 1.2-1.8 区间），也未解释为何该区间是“通常”范围（缺乏对 ε 和 C_holding 典型取值范围的约束说明）。）
