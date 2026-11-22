# N36: 共享随机源投影2（卖家侧）：卖家基于过往成交数据估计的价值分布为 V_seller = V_true + ε_seller，假设 ε_seller 与 ε_bu

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N6

## Claim

共享随机源投影2（卖家侧）：卖家基于过往成交数据估计的价值分布为 V_seller = V_true + ε_seller，假设 ε_seller 与 ε_buyer 独立同分布（i.i.d.）N(0, σ²)，但卖家无法直接观测 ε_buyer，仅能观测成交结果，导致信息滞后。

## Corrected Claim

共享随机源投影2（卖家侧）：卖家基于过往成交数据估计的价值分布为 V_seller = V_true + ε_seller，假设 ε_seller 与 ε_buyer 独立同分布（i.i.d.）N(0, σ²)，但卖家无法直接观测 ε_buyer，仅能观测成交结果，导致信息滞后。

## Evidence

父节点级核验未通过：非正交（子节点1（生成机制）在定义中直接包含了子节点2和子节点3的具体量化公式，导致逻辑层级混乱和概念重叠。子节点1应仅描述结构关系，而不应包含本应由子节点2和3承载的具体参数化细节。）

## Search Query

seller buyer information asymmetry used market independent noise
