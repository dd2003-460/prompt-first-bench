# N288: 信号污染的交互效应需通过同时展示降价历史和商品成色信息的 A/B 测试量化，具体为 CTR 和感知质量评分的联合变化。

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N93

## Claim

信号污染的交互效应需通过同时展示降价历史和商品成色信息的 A/B 测试量化，具体为 CTR 和感知质量评分的联合变化。

## Corrected Claim

信号污染的交互效应可通过A/B测试结合因果推断方法（如多实验分析）进行量化，具体指标需根据业务场景确定（如CTR及用户反馈评分）。

## Evidence

[质询]来源仅讨论了A/B测试中通用的干扰效应（如网络溢出、竞争效应）及多实验分析（MEA）方法，并未具体提及“信号污染”、“降价历史”、“商品成色”或“CTR与感知质量评分联合变化”这一特定业务场景下的量化方案，存在将通用方法论强行套用于特定未验证场景的风险。 | 来源[1]和[2]支持通过A/B测试及特定因果推断方法（如MEA）量化交互/干扰效应的逻辑框架，但未直接支持该特定业务指标组合（降价历史+成色 vs CTR+感知质量）的有效性，属于间接支持。

## Search Query

A/B test interaction effect of price history and product condition on CTR and perceived quality

## Retrieval Sources

- {'url': 'https://bbs.csdn.net/weixin_30898555/article/details/100114710&rut=23f5a75758a0b002a5e1148c79b57d708598884aa0206ed9600458317b70b661', 'type': 'ddg', 'title': '多实验分析：破解A/B测试组合效应评估难题的因果推断方法'}
- {'url': 'https://bbs.huaweicloud.com/blogs/469534&rut=3ee653768639c179a0ce5bfc4d22d2078021d0059a67082ee619680b945d8a38', 'type': 'ddg', 'title': '网络a/B测试：处理干扰效应的实验设计-云社区-华为云'}
