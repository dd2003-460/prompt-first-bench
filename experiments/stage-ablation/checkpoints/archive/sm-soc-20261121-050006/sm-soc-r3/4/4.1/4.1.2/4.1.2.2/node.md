# N261: 参数 I_loss_aversion（主观感知强度）的操作化定义与测量公式：I_loss_aversion 量化为卖家持有期间商品市场价值贬损率与实际心理贬损率

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N81

## Claim

参数 I_loss_aversion（主观感知强度）的操作化定义与测量公式：I_loss_aversion 量化为卖家持有期间商品市场价值贬损率与实际心理贬损率之差的标准化值，公式为 I_loss_aversion = (P_ref - P_market_current) / P_ref * (1 + η_sentiment)，其中 η_sentiment 为情感依恋系数（0-1），可通过卖家历史行为日志（如修改价格频率、描述文本情感分析）估算，典型值在 0.3-0.6 之间。

## Corrected Claim

I_loss_aversion 被定义为量化卖家主观感知强度的指标，其计算涉及市场价值贬损与心理贬损的差异，并引入情感依恋系数 η_sentiment 进行修正，但该具体公式及参数典型值缺乏公开权威来源佐证。

## Evidence

[质询]该公式及参数定义（I_loss_aversion, η_sentiment）缺乏公认的学术或行业标准支持，疑似为特定模型或虚构的理论构造，且'典型值0.3-0.6'属于无来源支持的经验性断言。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体公式及参数范围的真实性）

## Search Query

measuring loss aversion intensity seller sentiment analysis second-hand goods price depreciation
