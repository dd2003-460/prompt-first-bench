# N103: 两现象同源性的统计检验指标：计算条件概率 P(ShortCycle | HighPrice) 和 P(NoInquiry | PriceDrop) 的联合分布，

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

两现象同源性的统计检验指标：计算条件概率 P(ShortCycle | HighPrice) 和 P(NoInquiry | PriceDrop) 的联合分布，若二者由同一机制驱动，则相关系数 ρ = Cov(P(ShortCycle|HighPrice), P(NoInquiry|PriceDrop)) / (σ_1 * σ_2) 应显著为正（ρ > 0.3），置信度提升至 0.75。

## Corrected Claim

两现象同源性的统计检验：若 ShortCycle 与 HighPrice、NoInquiry 与 PriceDrop 由同一潜在机制驱动，则跨样本/跨时间序列中，P(ShortCycle | HighPrice) 的波动与 P(NoInquiry | PriceDrop) 的波动应呈现显著正相关（Pearson r > 0.3），且联合分布的似然比检验支持同源性假设。

## Evidence

[质询]统计指标定义存在逻辑瑕疵：条件概率 P(ShortCycle | HighPrice) 和 P(NoInquiry | PriceDrop) 是标量（固定值），两个标量之间的协方差和标准差在单样本或静态定义下无意义（方差为0，导致分母为0或未定义）。该陈述混淆了‘两个随机变量之间的相关系数’与‘两个条件概率值之间的相关性’。若意指跨时间/跨样本的波动相关性，表述应更严谨；若意指静态关联，则公式不适用。 | 先验知识/题面给定，但逻辑校验发现统计公式应用对象错误（标量间无协方差），且无外部来源支持该特定阈值（0.3, 0.75）的合理性。
