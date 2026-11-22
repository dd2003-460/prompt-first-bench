# N62: 卖家成本 C 的估算：C = C_production + C_holding + C_transaction，其中 C_production=0, C_hol

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N21

## Claim

卖家成本 C 的估算：C = C_production + C_holding + C_transaction，其中 C_production=0, C_holding=5% of P_base, C_transaction=2% of P_base

## Corrected Claim

卖家成本 C 的估算：C = C_production + C_holding + C_transaction，其中 C_production=0, C_holding=5% of P_base, C_transaction=2% of P_base

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 冗余性：子节点1和子节点2本质上是同一参数（持有成本 C_holding）在不同持有周期下的计算实例，属于参数敏感性分析，而非独立的结构维度，应合并或作为同一节点的参数范围。2. 矛盾性（非正交）：父节点定义 C_transaction 为 2%，但子节点3 将其拆解为 5.2%（平台抽成5%+支付费0.2%），这与父节点定义直接矛盾，且未说明为何在总成本估算中仍使用2%或是否修正了父节点定义。3. 完备性：子节点1和2仅给出了特定场景下的总成本近似值，未明确 C_production=0 的假设条件或验证，且未解释为何在子节点3中交易成本大幅变化后，总成本公式是否随之调整。）

## Search Query

sellers cost structure in second-hand marketplace
