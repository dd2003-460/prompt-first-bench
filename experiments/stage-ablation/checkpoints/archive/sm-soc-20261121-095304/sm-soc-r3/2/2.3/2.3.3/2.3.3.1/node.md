# N123: 在主流二手交易平台（如闲鱼/转转）的公开风控逻辑或逆向工程数据中，标准价格波动监测窗口 T_window 通常设定为 7 天或 14 天，具体数值需依据平台最新

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

在主流二手交易平台（如闲鱼/转转）的公开风控逻辑或逆向工程数据中，标准价格波动监测窗口 T_window 通常设定为 7 天或 14 天，具体数值需依据平台最新卖家协议或 A/B 测试日志确认。

## Corrected Claim

在主流二手交易平台的逆向工程或风控研究中，价格波动监测窗口常被设定为短期周期（如7-14天），但具体数值因平台策略动态调整而异，需依据最新逆向数据确认。

## Evidence

[质询]该陈述声称在公开风控逻辑或逆向数据中，标准价格波动监测窗口“通常”设定为7天或14天，但参考来源仅涉及数据采集、反爬机制及违禁词审核，未提供关于价格监测具体时间窗口（T_window）的实证数据或行业共识，属于缺乏来源支持的特定经验参数断言。 | 逻辑上7-14天作为短期价格波动监测窗口符合电商风控直觉，但参考来源[1][2][3]均未提及具体的时间窗口数值，属于经验事实且缺来源直接支持。

## Search Query

Xianyu seller risk control price fluctuation window 7 days OR 14 days documentation

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_33046983/article/details/164348954&rut=0cfda06c50ef7d08a5cd68b5b5b3e5be2e18f6b3c16b46dc84df6b4cf839e49b', 'type': 'ddg', 'title': '闲鱼智能监控与风控系统：从数据采集到自动化决策的实战拆解-csdn博客'}
- {'url': 'https://blog.csdn.net/weixin_29323273/article/details/162322988&rut=9ff3777a036a3b43ae4204f02280ddd4703504e5db488a1103632866ead3da5a', 'type': 'ddg', 'title': '闲鱼反爬虫实战：逆向js加密与行为风控对抗策略-csdn博客'}
- {'url': 'https://blog.gitcode.com/e71eb985dbbd4be43a4cd9115804559f.html&rut=9a48a914e14cc65dff652cd98fab53283dbf32b1e06e457519e8f1645007a165', 'type': 'ddg', 'title': '二手平台风控是如何拦词的？从awesome-chinese-secondhand-slang词条趋势看闲鱼、转转、小红书违禁词审核逻辑 ...'}
