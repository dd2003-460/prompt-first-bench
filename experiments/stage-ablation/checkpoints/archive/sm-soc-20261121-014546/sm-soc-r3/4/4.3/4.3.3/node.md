# N91: 高挂价卖家（偏离度>20%）在干预措施A实施后，其成交周期延长的具体数值范围：基于 ε_d=0.5-0.8 和 P_ask_old=1.25V, P_ancho

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N21, N22, N23

## Claim

高挂价卖家（偏离度>20%）在干预措施A实施后，其成交周期延长的具体数值范围：基于 ε_d=0.5-0.8 和 P_ask_old=1.25V, P_anchor=V 的假设，ΔT 约为 T_old 的 20%-40%（即若原周期为7天，延长1.4-2.8天）。

## Corrected Claim

在假设 ε_d=0.5-0.8 且价格锚定机制成立的前提下，高挂价卖家的成交周期预计延长 20%-40%，但该结论依赖于特定模型参数，需实证数据验证。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 逻辑矛盾：子节点1和2基于需求弹性推导得出周期缩短（负值），直接反驳了父节点‘延长20-40%’的结论，导致子节点与父节点在事实结论上冲突，而非支撑父节点。2. 冗余严重：子节点1和2本质上是同一公式在不同参数（ε_d=0.5和0.8）下的计算，属于参数化重复，应合并。3. 覆盖偏差：子节点3引入了新的摩擦项模型，但前两个子节点未考虑此因素，导致不同子节点基于不同模型假设，缺乏统一性。）

## Search Query

empirical study price anchoring transaction time extension high premium sellers
