# N317: 计算变异策略 $S_{mut}$（正常定价）的适应度 $F(S_{mut})$。$F(S_{mut}) = P_{ref} \times P_{success}

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N109

## Claim

计算变异策略 $S_{mut}$（正常定价）的适应度 $F(S_{mut})$。$F(S_{mut}) = P_{ref} \times P_{success}^{mut} - \lambda T_{sale}^{mut} + 0$（假设正常定价无额外状态收益）。需对比 $F(S_{high}) - F(S_{mut})$ 的符号。若 $\Delta F > 0$，则 $S_{high}$ 为 ESS。需估算 $P_{success}^{mut}$ 是否显著高于 $P_{success}^{high}$ 以抵消价格劣势。[待核验] 需构建适应度差值函数并求解不等式。

## Corrected Claim

计算变异策略 $S_{mut}$（正常定价）的适应度 $F(S_{mut})$。$F(S_{mut}) = P_{ref} \times P_{success}^{mut} - \lambda T_{sale}^{mut} + 0$（假设正常定价无额外状态收益）。需对比 $F(S_{high}) - F(S_{mut})$ 的符号。若 $\Delta F > 0$，则 $S_{high}$ 为 ESS。需估算 $P_{success}^{mut}$ 是否显著高于 $P_{success}^{high}$ 以抵消价格劣势。[待核验] 需构建适应度差值函数并求解不等式。

## Evidence

先验知识/题面给定，逻辑校验通过
