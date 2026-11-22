# N80: 平台GMV变动量 Δ平台GMV = (P_new * Q_new * fee_rate) - (P_old * Q_old * fee_rate)，其中 fee

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N18

## Claim

平台GMV变动量 Δ平台GMV = (P_new * Q_new * fee_rate) - (P_old * Q_old * fee_rate)，其中 fee_rate 为平台佣金率，通常设定为 2%-5%

## Corrected Claim

平台GMV变动量 Δ平台GMV = (P_new * Q_new * fee_rate) - (P_old * Q_old * fee_rate)，其中 fee_rate 为平台佣金率，通常设定为 2%-5%

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点存在严重命名冲突与逻辑重叠：两个子节点均标记为'工作点C'，导致正交性破坏；此外，工作点A、B、C本质上是同一公式在不同参数约束下的特例，存在冗余，应合并为参数化描述而非独立节点。）
