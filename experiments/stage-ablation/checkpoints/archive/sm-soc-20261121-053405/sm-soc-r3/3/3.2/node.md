# N15: 买家伤害量化：干预后买家剩余消费者剩余变化 $\Delta CS_{buyer} = \int_{P_{new}}^{WTP} (WTP - P) dQ - \

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N3

## Claim

买家伤害量化：干预后买家剩余消费者剩余变化 $\Delta CS_{buyer} = \int_{P_{new}}^{WTP} (WTP - P) dQ - \int_{P_{old}}^{WTP} (WTP - P) dQ$。若干预导致成交均价上升，$\Delta CS_{buyer} < 0$，伤害程度为 $|\Delta CS_{buyer}| / CS_{old}$。

## Corrected Claim

买家伤害量化：干预后买家剩余消费者剩余变化 $\Delta CS_{buyer} = \int_{P_{new}}^{WTP} (WTP - P) dQ - \int_{P_{old}}^{WTP} (WTP - P) dQ$。若干预导致成交均价上升，$\Delta CS_{buyer} < 0$，伤害程度为 $|\Delta CS_{buyer}| / CS_{old}$。

## Evidence

先验知识/题面给定，逻辑校验通过：消费者剩余定义为需求曲线下方、价格线上方的面积，公式表达符合微积分定义；若价格上升（P_new > P_old），积分区间缩小且被积函数在相同Q下值减小，故ΔCS < 0，逻辑自洽。
