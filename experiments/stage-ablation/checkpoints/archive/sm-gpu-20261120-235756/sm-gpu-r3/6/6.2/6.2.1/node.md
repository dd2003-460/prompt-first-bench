# N114: 二手 RTX 4090 故障率与停机成本：基于社区数据，二手 4090 在 6 个月内的故障率约为 3-5%（主要源于显存颗粒老化或供电模块电容失效）；平均修复

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N30

## Claim

二手 RTX 4090 故障率与停机成本：基于社区数据，二手 4090 在 6 个月内的故障率约为 3-5%（主要源于显存颗粒老化或供电模块电容失效）；平均修复时间 (MTTR) 为 3-7 天（含 RMA 流程），若机会成本为 $100/天，则期望停机成本约为 $150-$350/卡 [待核验]。

## Corrected Claim

二手 RTX 4090 存在较高的故障风险（主要源于显存老化或供电模块失效），且维修周期较长（通常涉及 RMA 流程，耗时数天至一周以上），导致显著的停机机会成本。

## Evidence

[质询]具体数值（3-5%故障率、3-7天MTTR）缺乏权威统计来源支持，属于基于社区经验的估算值，且不同来源对二手卡风险的具体量化数据不一致或缺失。 | 来源[1][2][3]均定性讨论了二手RTX 4090的故障风险、老化问题及持有成本，但未提供具体的故障率百分比或MTTR天数，属于间接支持；经验事实无直接来源支持，降级为定性表述。

## Search Query

Used RTX 4090 failure rate MTTR downtime cost estimate

## Retrieval Sources

- {'url': 'https://world.taobao.com/lang/zh-tw/shopping-guide/2046130802663620608.htm&rut=62487eac1c6b2c54387b11833e06fe02b1a78fce465a1e21377be56ce64f490f', 'type': 'ddg', 'title': '二手rtx 4090避坑指南：估值邏輯、礦卡風險識別與實戰檢測攻略'}
- {'url': 'https://blog.csdn.net/weixin_42311427/article/details/152071260&rut=dd176e51a63c95f9f82644180c2feef25fbb3261778faf949cce1ff21aac8e06', 'type': 'ddg', 'title': '买二手rtx4090显卡靠谱吗？ - Csdn博客'}
- {'url': 'https://world.taobao.com/lang/zh-tw/shopping-guide/2014511599716401152.htm&rut=305041b0faf726476de6aa91b28443f09594293bd8ec5db5a308f8c056080cd7', 'type': 'ddg', 'title': 'Rtx 4090 魔改卡真的省錢？揭秘二手殘值黑洞與總體持有成本真相'}
