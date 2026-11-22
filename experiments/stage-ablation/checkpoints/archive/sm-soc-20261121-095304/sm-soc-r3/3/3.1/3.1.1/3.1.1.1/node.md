# N131: 回看窗口 T_lookback 的选取对 P_market 稳定性的影响：T_lookback 通常设为 7 天或 30 天；若 T_lookback 过短（如

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N44

## Claim

回看窗口 T_lookback 的选取对 P_market 稳定性的影响：T_lookback 通常设为 7 天或 30 天；若 T_lookback 过短（如 3 天），P_market 对极端高价成交敏感，导致高挂价卖家误判市场均价，T_lookback 的具体取值需根据类目成交频率（如日成交量 < 5 件时延长至 30 天）动态调整。

## Corrected Claim

回看窗口 T_lookback 的选取对 P_market 稳定性有显著影响。通常建议根据类目成交频率动态调整：对于高频成交类目，较短窗口（如7天）可能足够；对于低频成交类目（如日成交量极低），应延长窗口（如30天）以避免因样本过少导致对极端高价成交过于敏感，从而防止卖家误判市场均价。

## Evidence

[质询]来源主题不匹配：参考来源讨论的是时间序列预测模型（LTSF）中的超参数 lookback window，而事实陈述讨论的是二手交易/电商市场中用于计算市场均价（P_market）的业务逻辑回看窗口。两者领域完全不同，来源无法支持该具体业务规则（如7天/30天、日成交量<5件等具体阈值）。 | 逻辑自洽：在低频交易场景下，短窗口确实会导致样本不足从而对极端值敏感，延长窗口以平滑波动符合统计学直觉。但参考来源[1][2]均关于机器学习时间序列预测，与电商市场均价计算无关，属于「无可用外部证据」。根据经验事实排除条款，此类具体业务参数（7天/30天、<5件）无法从第一性原理严格推出，且缺乏直接来源支持，故降级。

## Search Query

market average price lookback window 7 days OR 30 days low liquidity category

## Retrieval Sources

- {'url': 'https://arxiv.org/pdf/2502.09683&rut=3132140338eb282e1a2b27fadc73a91a9cf344a5973ec44b3f8f6cc277c33bb6', 'type': 'ddg', 'title': 'Channel Dependence, Limited Lookback Windows, and the Simplicity of ...'}
- {'url': 'https://arxiv.org/abs/2502.09683&rut=d69d5d5af04568ecf3d52661bb779f2e0275b8c17db70ecadad297c964cf307c', 'type': 'ddg', 'title': '[2502.09683] Channel Dependence, Limited Lookback Windows, and the ...'}
