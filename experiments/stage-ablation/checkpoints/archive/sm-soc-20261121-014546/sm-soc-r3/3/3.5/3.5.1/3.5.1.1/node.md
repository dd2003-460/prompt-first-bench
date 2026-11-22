# N252: 历史成交价分布 F(P_hist) 的样本窗口 W 的具体取值（如 7 天/30 天/90 天），不同 W 导致的中位数 M_50 差异 ΔM_W = |M_5

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: stochastic
- **rework_count**: 1
- **parent_ids**: N75

## Claim

历史成交价分布 F(P_hist) 的样本窗口 W 的具体取值（如 7 天/30 天/90 天），不同 W 导致的中位数 M_50 差异 ΔM_W = |M_50(W1) - M_50(W2)|，需通过回测数据确定对成交周期 T 预测误差的影响幅度。

## Corrected Claim

历史成交价分布 F(P_hist) 的样本窗口 W 的具体取值及其对中位数 M_50 和成交周期 T 预测误差的影响，属于需通过特定市场数据的实证回测才能确定的经验参数，无法从通用逻辑或现有无关来源中推导得出。

## Evidence

[质询]该陈述描述的是一个需要特定领域数据（如金融交易数据）进行实证回测才能确定的经验性结论，而非通用事实。参考来源完全无关，无法提供数值支持或验证其逻辑推导的可行性。 | 参考来源[1]和[2]分别涉及机器学习数据集列表和历史政治实体，与金融交易价格分布及回测策略完全无关，属于「无可用外部证据」。该陈述在逻辑上自洽（即确实需要通过回测来确定参数影响），但作为经验事实，缺乏来源支持，故降级。

## Search Query

historical price window selection impact on median price estimation second-hand market

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research', 'type': 'wikipedia', 'title': 'List of datasets for machine-learning research'}
- {'url': 'https://en.wikipedia.org/wiki/Polish%E2%80%93Lithuanian_Commonwealth', 'type': 'wikipedia', 'title': 'Polish–Lithuanian Commonwealth'}
