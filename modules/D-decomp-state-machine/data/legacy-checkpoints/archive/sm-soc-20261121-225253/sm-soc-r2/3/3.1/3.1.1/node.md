# N30: 参数 $\alpha$ 的标定基准：为使高挂价（溢价>20%）商品的搜索排名从Top 10%降至Top 50%，基于典型平台排序公式（如Score = CTR 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N11

## Claim

参数 $\alpha$ 的标定基准：为使高挂价（溢价>20%）商品的搜索排名从Top 10%降至Top 50%，基于典型平台排序公式（如Score = CTR * Price * (1-Penalty)），$\alpha$ 的理论下限约为 2.5（假设CTR与Price正相关且权重相等）。

## Corrected Claim

参数 α 的标定需基于具体平台的数据分布进行实证分析；在假设 Score = CTR * Price * (1-Penalty) 且 CTR 与 Price 正相关的简化模型下，α 的取值需通过模拟或回归确定，以达成特定的排名压制效果（如从 Top 10% 降至 Top 50%），而非存在普适的理论下限 2.5。

## Evidence

[质询]该陈述将具体的经验性数值（α≈2.5）与特定的业务目标（排名从Top 10%降至Top 50%）直接挂钩，并假设了特定的排序公式结构（Score = CTR * Price * (1-Penalty)）及参数关系（CTR与Price正相关且权重相等）。然而，排名分位数的变化取决于整个商品池的分布形态（如价格分布的长尾程度、CTR的方差等），并非仅由公式结构决定。在没有具体数据分布的情况下，断言α的理论下限“约为2.5”缺乏严谨的数学推导支持，属于基于特定假设的经验估算，而非普适的理论下限。 | source=knowledge，逻辑上公式结构自洽，但具体数值2.5依赖于未给出的分布假设，属于经验事实范畴，缺乏来源直接支持或第一性原理严格推导，故降级。

## Search Query

search ranking penalty coefficient calibration price deviation
