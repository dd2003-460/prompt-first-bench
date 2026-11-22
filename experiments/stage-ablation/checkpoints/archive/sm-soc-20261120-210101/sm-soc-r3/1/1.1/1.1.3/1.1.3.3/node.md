# N130: 下游投影2：标签增强锚定系数 α_anchor_tag 的量化，当商品带有‘近期成交’或‘高信用’标签时，α_anchor_tag = α_anchor_bas

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N32

## Claim

下游投影2：标签增强锚定系数 α_anchor_tag 的量化，当商品带有‘近期成交’或‘高信用’标签时，α_anchor_tag = α_anchor_base * (1 + β_tag * I_density)，其中 β_tag 为标签信任系数（假设 β_tag=0.5），I_density 来自 N120。

## Corrected Claim

下游投影2：标签增强锚定系数 α_anchor_tag 的量化，当商品带有‘近期成交’或‘高信用’标签时，α_anchor_tag = α_anchor_base * (1 + β_tag * I_density)，其中 β_tag 为标签信任系数（假设 β_tag=0.5），I_density 来自 N120。

## Evidence

先验知识/题面给定，逻辑校验通过
