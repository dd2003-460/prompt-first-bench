# N115: 全自建 10 个 POP 点的月度基础设施固定成本 $C_{fixed}^{self}$ (¥/月)，由硬件折旧 $C_{hw}$ 和机房电力租赁 $C_{co

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N28

## Claim

全自建 10 个 POP 点的月度基础设施固定成本 $C_{fixed}^{self}$ (¥/月)，由硬件折旧 $C_{hw}$ 和机房电力租赁 $C_{colo}$ 构成：$C_{fixed}^{self} = 10 \times (N_{srv} \times C_{srv}/36 + N_{rack} \times (R_{rack} + E_{pow} \times P_{kWh}))$，需代入具体服务器/机柜参数计算。

## Corrected Claim

全自建 10 个 POP 点的月度基础设施固定成本 $C_{fixed}^{self}$ (¥/月)，由硬件折旧 $C_{hw}$ 和机房电力租赁 $C_{colo}$ 构成：$C_{fixed}^{self} = 10 \times (N_{srv} \times C_{srv}/36 + N_{rack} \times (R_{rack} + E_{pow} \times P_{kWh}))$，需代入具体服务器/机柜参数计算。

## Evidence

先验知识/题面给定，逻辑校验通过：公式结构符合基础设施成本构成逻辑（硬件折旧+电力租赁），量纲与数值关系自洽。

## Search Query

data center colocation cost per rack China server depreciation
