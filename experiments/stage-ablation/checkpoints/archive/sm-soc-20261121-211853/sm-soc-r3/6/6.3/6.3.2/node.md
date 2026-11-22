# N147: ‘高价仅被解读为卖家非理性’的量化检验：当 $H > 0.7$ 且 $C > 1.15$ 时，买家对高价的归因概率分布发生翻转。定义归因概率 $P_{irrat

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

‘高价仅被解读为卖家非理性’的量化检验：当 $H > 0.7$ 且 $C > 1.15$ 时，买家对高价的归因概率分布发生翻转。定义归因概率 $P_{irrational} = P(Price \uparrow \mid Quality \approx Constant)$。在标准化商品中，若 $C > 1.15$，买家认为‘质量提升’的先验概率 $P(Q \uparrow)$ 降至 0.2 以下，而‘卖家非理性/信息不对称’的后验概率 $P(Irrational)$ 升至 0.8 以上。此时决策时间延长 15% 的机制是：买家花费额外时间验证卖家信誉（如查看历史成交记录），该验证成本 $C_{verify}$ 约为 2-3 分钟，导致总决策时间 $T_{decision} = T_{base} + C_{verify} \times P(Irrational)$。

## Corrected Claim

在标准化商品市场中，当价格显著高于基准（如 C > 1.15）时，买家倾向于将高价归因于卖家非理性或信息不对称而非质量提升，从而增加验证卖家信誉的时间成本，导致总决策时间延长。

## Evidence

[质询]该陈述包含大量具体的经验性数值（如阈值 H>0.7, C>1.15, 概率 0.2/0.8, 时间成本 2-3 分钟），这些并非第一性原理可推导的数学或物理定律，而是行为经济学或市场微观结构中的经验参数。缺乏实证数据支持这些具体数值在‘标准化商品’这一宽泛场景下的普适性，且‘归因概率分布发生翻转’的机制描述过于简化，忽略了买家异质性和市场结构的影响。 | source=knowledge，逻辑自洽（决策时间公式符合线性叠加直觉，概率归一化合理），但具体数值阈值和概率分布属于经验事实，缺乏来源直接支持，依据经验事实排除条款降级。

## Search Query

buyer attribution of high price irrational seller standardized products decision delay
