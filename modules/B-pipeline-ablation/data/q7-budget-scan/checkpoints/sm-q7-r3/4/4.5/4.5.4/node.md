# N89: 紧急人力成本 Emergency_Labor_Cost 等于 参与应急的工程师数量 (N_engineers) 乘以 人均时薪 (Hourly_Wage) 乘以

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N25

## Claim

紧急人力成本 Emergency_Labor_Cost 等于 参与应急的工程师数量 (N_engineers) 乘以 人均时薪 (Hourly_Wage) 乘以 实际工作时长 (T_downtime)，假设 N_engineers=2, Hourly_Wage=¥500/h，则 C_emergency = 2 * 500 * T_downtime。

## Corrected Claim

紧急人力成本 Emergency_Labor_Cost 等于 参与应急的工程师数量 (N_engineers) 乘以 人均时薪 (Hourly_Wage) 乘以 实际工作时长 (T_downtime)，假设 N_engineers=2, Hourly_Wage=¥500/h，则 C_emergency = 2 * 500 * T_downtime。

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（子节点1和子节点2存在严重的逻辑包含与冗余关系。子节点1定义了 T_effective 的计算规则（效率衰减），而子节点2不仅复述了该结果（引用 T_effective=9.6h），还引入了新变量 Overtime_Multiplier 并给出了最终公式。这两个子节点并非平行独立的维度，而是“中间变量定义”与“最终公式整合”的关系，且子节点2的内容完全涵盖了子节点1的逻辑意图。此外，父节点仅关注基础成本，子节点引入了“加班倍率”这一父节点未提及的新约束，导致分解层级不一致。）
