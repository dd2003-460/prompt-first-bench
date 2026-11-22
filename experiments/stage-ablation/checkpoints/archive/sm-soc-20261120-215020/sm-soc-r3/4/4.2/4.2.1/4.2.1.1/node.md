# N154: 浏览时间 $T_{browse}$ 的基准值量化：在二手交易平台，用户从进入搜索页到点击首个商品的平均浏览时间。假设 $T_{browse} = 30$ 秒，占

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N53

## Claim

浏览时间 $T_{browse}$ 的基准值量化：在二手交易平台，用户从进入搜索页到点击首个商品的平均浏览时间。假设 $T_{browse} = 30$ 秒，占总决策时间 $T_0$ 的 10-15%。该值受搜索界面设计和商品图片加载速度影响，需通过日志统计确定中位数。

## Corrected Claim

浏览时间 $T_{browse}$ 的基准值需通过日志统计确定中位数，通常受搜索界面设计和商品图片加载速度影响；具体数值（如30秒或占比10-15%）需依据实际业务数据校准，不可直接作为通用常量。

## Evidence

[质询]该陈述包含具体的经验数值（30秒、10-15%），属于特定业务场景下的统计结果，无法从第一性原理推导，且参考来源仅讨论指标体系搭建方法，未提供该具体数值的支持。 | 逻辑自洽（30秒占3-5分钟总决策时间的10-15%在量级上合理），但参考来源[1]仅涉及搜索指标体系方法论，未提供具体浏览时间数值，属于经验事实且缺乏直接来源支持。

## Search Query

average browsing time before click e-commerce platform log data

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/606079964&rut=26b98344f5398266460901cf28299aaaa31990ec26897d4a1bd22abe964703b6', 'type': 'ddg', 'title': '浅谈搜索业务常见数据指标 - 知乎'}
