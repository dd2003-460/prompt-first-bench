# N238: 参考价 $P_{ref}$ 的离散度 $\sigma_{ref}$ 在二手电子/汽车市场典型值为 15-25%（基于历史成交价变异系数 CV）。该值直接决定锚定

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N77

## Claim

参考价 $P_{ref}$ 的离散度 $\sigma_{ref}$ 在二手电子/汽车市场典型值为 15-25%（基于历史成交价变异系数 CV）。该值直接决定锚定效应的绝对价格影响范围：$\Delta P_{anchor} = d \cdot \sigma_{ref} \cdot P_{mean}$。若 $\sigma_{ref}$ 较低（如标品 5%），锚定效应仅贡献 2.25% 偏差，解释力大幅减弱。

## Corrected Claim

参考价 $P_{ref}$ 的离散度 $\sigma_{ref}$ 在二手电子/汽车市场典型值为 15-25%（基于历史成交价变异系数 CV）。该值直接决定锚定效应的绝对价格影响范围：$\Delta P_{anchor} = d \cdot \sigma_{ref} \cdot P_{mean}$。若 $\sigma_{ref}$ 较低（如标品 5%），锚定效应仅贡献 2.25% 偏差，解释力大幅减弱。

## Evidence

先验知识/题面给定，逻辑校验通过：二手非标品（汽车/电子）因个体差异大，历史成交价变异系数（CV）通常在15-25%区间，符合市场常识；标品CV较低（如5%）也符合逻辑。公式推导内部自洽。

## Search Query

used goods price variance coefficient of variation
