# N227: 分类型输出的 X_ref 来源约束：若 X_ref 来自人工标注，标注一致性（inter-annotator agreement）的 Kappa 系数需 >0.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N65

## Claim

分类型输出的 X_ref 来源约束：若 X_ref 来自人工标注，标注一致性（inter-annotator agreement）的 Kappa 系数需 >0.8 才能作为可靠基准；若 Kappa <0.6，标注噪声本身会引入 >1% 的错误率，使 E_cat <0.1% 的阈值失去意义，此时需改用多数投票（n≥5 标注者）或 LLM-as-judge 方案

## Corrected Claim

分类型输出的 X_ref 来源约束：若 X_ref 来自人工标注，通常要求较高的标注一致性（如 Kappa 系数 >0.8）以确保基准可靠性；若一致性较低（如 Kappa <0.6），标注噪声可能显著影响评估精度，此时建议采用多数投票（n≥5 标注者）或 LLM-as-judge 等更鲁棒的方案。

## Evidence

[质询]Kappa系数与错误率之间的线性映射关系（Kappa<0.6导致>1%错误率）缺乏普适的理论基础，具体数值阈值高度依赖于类别分布和任务难度，属于经验性断言而非严格推导。 | 先验知识/题面给定，逻辑校验通过；但具体数值阈值（0.8, 0.6, 1%）为经验参数，虽符合一般统计学直觉，但缺乏绝对严谨的推导支撑，故降级为定性建议。
