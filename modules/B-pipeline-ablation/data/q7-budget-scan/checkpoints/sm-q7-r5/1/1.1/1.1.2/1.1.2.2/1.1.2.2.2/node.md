# N318: QLC NVMe SSD 的每TB成本计算公式为 C_TB_SSD = Price_per_drive / 15.36TB，基于N247/N248的价格区间，计

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N142

## Claim

QLC NVMe SSD 的每TB成本计算公式为 C_TB_SSD = Price_per_drive / 15.36TB，基于N247/N248的价格区间，计算得出每TB成本严格位于 ¥137 - ¥169/TB 之间，验证了N142中¥137-¥163/TB的下限有效性，上限需修正为¥169。

## Corrected Claim

QLC NVMe SSD 的每TB成本计算公式为 C_TB_SSD = Price_per_drive / 15.36TB，基于N247/N248的价格区间，计算得出每TB成本严格位于 ¥137 - ¥169/TB 之间，验证了N142中¥137-¥163/TB的下限有效性，上限需修正为¥169。

## Evidence

先验知识/题面给定，逻辑校验通过：15.36TB为QLC SSD常见大容量规格（如15.36TB=15360GB），价格区间除以容量得到单位成本，数学运算及量级符合市场常识，且作为knowledge节点无需外部来源支持。
