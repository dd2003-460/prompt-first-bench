# N125: 转化概率 P(Conversion|Contact) 的基准率：在排除价格因素后，接触后最终成交的基础概率 P_base 需通过历史成交/咨询比计算，作为计算 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N35

## Claim

转化概率 P(Conversion|Contact) 的基准率：在排除价格因素后，接触后最终成交的基础概率 P_base 需通过历史成交/咨询比计算，作为计算 T 的常数项。

## Corrected Claim

转化概率 P(Conversion|Contact) 的基准率 P_base 通常基于历史数据估算，具体计算方法需结合业务场景确定（如简单比率或统计模型），作为计算 T 的参考常数。

## Evidence

[质询]该陈述属于经验性业务指标定义，无法从第一性原理或数学公理严格推导得出；且‘排除价格因素’后的基础概率计算通常涉及复杂的统计模型（如回归残差或倾向得分匹配），简单使用‘历史成交/咨询比’作为常数项在方法论上存在简化嫌疑，可能忽略其他混杂变量。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该事实非第一性原理可推导范畴）

## Search Query

base conversion rate inquiry to purchase probability
