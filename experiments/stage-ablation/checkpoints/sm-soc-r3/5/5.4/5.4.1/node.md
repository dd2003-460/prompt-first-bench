# N95: 平台算法排序函数 P_exposure = w1 × margin + w2 × price + w3 × recency，其中 w1, w2, w3 为可估计

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N28

## Claim

平台算法排序函数 P_exposure = w1 × margin + w2 × price + w3 × recency，其中 w1, w2, w3 为可估计的权重系数，在多数二手平台中 w1 > w2 > w3，具体权重比约为 0.5:0.3:0.2

## Corrected Claim

平台算法排序函数通常综合考虑利润空间、价格竞争力及新鲜度，其中利润空间权重通常最高，但具体权重系数因平台而异，无统一固定比例。

## Evidence

[质询]具体权重比 0.5:0.3:0.2 属于高度具体的经验参数，不同平台（如闲鱼、转转、eBay）算法差异巨大，且通常不公开，该精确数值缺乏普遍性，极可能是臆造或特定小样本拟合结果，不具备通用事实属性。 | 先验知识/题面给定，逻辑校验通过（量纲一致，排序逻辑自洽），但具体数值缺乏来源支持且存在经验事实不确定性，故降级。

## Search Query

e-commerce platform ranking algorithm weights margin price recency
