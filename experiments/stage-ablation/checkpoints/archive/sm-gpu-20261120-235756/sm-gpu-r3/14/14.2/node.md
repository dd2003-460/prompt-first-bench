# N365: 分母项'TCO_3yr'中'购置成本'的构成：Purchase_Cost = MSRP + Import_Taxes + Shipping_Fee，对于二手卡需

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N138

## Claim

分母项'TCO_3yr'中'购置成本'的构成：Purchase_Cost = MSRP + Import_Taxes + Shipping_Fee，对于二手卡需替换为 Market_Price_Second_Hand，并需区分现货价与期货价（RTX 5090 首发期期货价通常高于现货 10-20% [待核验]）。

## Corrected Claim

分母项'TCO_3yr'中'购置成本'的构成：Purchase_Cost = MSRP + Import_Taxes + Shipping_Fee，对于二手卡需替换为 Market_Price_Second_Hand，并需区分现货价与期货价（RTX 5090 首发期期货价通常高于现货，具体溢价幅度视市场供需而定）。

## Evidence

[质询]RTX 5090 首发期期货价高于现货 10-20% 的具体数值区间缺乏普遍性，受市场波动、具体渠道及时间窗口影响极大，属于高度依赖具体市场数据的经验事实，且该卡尚未广泛上市或数据未稳定，存在将短期局部现象泛化为通用规则的风险。 | source=knowledge，逻辑自洽（TCO构成及二手/期货区分符合经济直觉），但‘10-20%’为具体经验数值，无外部来源支持，且属于易变的市场经验事实，依据规则降级。
