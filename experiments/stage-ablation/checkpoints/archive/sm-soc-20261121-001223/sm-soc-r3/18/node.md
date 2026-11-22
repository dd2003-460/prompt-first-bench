# N237: 降价后无咨询的‘锚定断裂’量化：当卖家主动降价幅度 ΔP_drop > 10% 时，会触发买家的‘质量怀疑’启发式（Quality Suspicion Heur

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

降价后无咨询的‘锚定断裂’量化：当卖家主动降价幅度 ΔP_drop > 10% 时，会触发买家的‘质量怀疑’启发式（Quality Suspicion Heuristic），导致咨询概率 P_consult 从基准值下降至 0.4 * P_consult_base；这种‘反常低价’效应解释了为何 60% 的降价卖家在 48 小时内未获新咨询。

## Corrected Claim

降价可能触发买家的质量怀疑心理，从而降低咨询意愿，但具体量化指标（如10%阈值、0.4倍系数、60%比例）缺乏可靠来源支持，需进一步实证研究验证。

## Evidence

[质询]该陈述包含大量未经证实的具体数值（如ΔP_drop > 10%、0.4倍系数、60%卖家、48小时窗口）和特定心理学术语（Quality Suspicion Heuristic），属于经验事实。参考来源[1]和[2]讨论的是亚马逊平台流量机制和广告效应，并未提及‘咨询概率’或‘质量怀疑启发式’的具体量化模型；来源[3]讨论量化交易模型失效，与电商卖家咨询行为无关。所有来源均不支持该具体量化结论，且该结论缺乏第一性原理推导基础，属于无来源支持的臆造数据。 | 参考来源[1][2]涉及亚马逊流量与价格机制，但未提供‘咨询概率下降至0.4倍’或‘60%卖家48小时无咨询’等具体量化数据；来源[3]主题无关。该事实为经验事实，缺乏来源直接支持或多源一致，且具体数值无逻辑推导依据，判定为failed。

## Retrieval Sources

- {'url': 'https://ask.cocoloop.cn/news/amazon-z-deal-ad-drop-2026&rut=501f5542f97ddcce35b7c116e88106ce8b426d75c8a93e1b1db5cd4f9c9f4879', 'type': 'ddg', 'title': '亚马逊Z划算后广告位消失自然位暴跌？2026卖家排查指南 | CocoLoop'}
- {'url': 'https://ask.cocoloop.cn/news/amazon-competitor-sales-surge-no-ads-2026&rut=acc294331487c86196ca2009e068d28ccc25d57021e1dc77f876d9d0915ca38c', 'type': 'ddg', 'title': '竞品没开广告降价后销量涨8倍？2026亚马逊自然流量机制深度拆解 | CocoLoop'}
- {'url': 'https://www.csdn.net/detail/webblog_11703081/101530&rut=49eb9977b09f2b5094483e52bf8687cefa2b8c1ea700a47922c5b76639adc5ff', 'type': 'ddg', 'title': '量化交易模型失效：政策冲击、结构断裂与残差监控 - Csdn'}
