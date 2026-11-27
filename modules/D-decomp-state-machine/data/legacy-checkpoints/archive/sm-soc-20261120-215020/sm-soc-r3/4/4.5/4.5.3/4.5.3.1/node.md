# N187: 短期 GMV 损失 $GMV_{Loss\_ShortTerm}$ 的精确计算：$GMV_{Loss\_ShortTerm} = Total\_GMV \tim

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N64

## Claim

短期 GMV 损失 $GMV_{Loss\_ShortTerm}$ 的精确计算：$GMV_{Loss\_ShortTerm} = Total\_GMV \times S_{high} \times (1 - \text{Retain\_Rate}_{high})$，其中 $\text{Retain\_Rate}_{high}$ 为受惩罚高溢价卖家在干预后的留存/成交比例，需量化卖家因曝光下降而退出或降价的比例。

## Corrected Claim

短期 GMV 损失 $GMV_{Loss\_ShortTerm}$ 的精确计算：$GMV_{Loss\_ShortTerm} = Total\_GMV \times S_{high} \times (1 - \text{Retain\_Rate}_{high})$，其中 $\text{Retain\_Rate}_{high}$ 为受惩罚高溢价卖家在干预后的留存/成交比例，需量化卖家因曝光下降而退出或降价的比例。

## Evidence

先验知识/题面给定，逻辑校验通过
