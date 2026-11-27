# N45: 主动降价卖家的基线咨询率 $CTR_{drop} = \frac{Clicks_{drop}}{Impressions_{drop}}$，需在降价事件发生后48

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

主动降价卖家的基线咨询率 $CTR_{drop} = \frac{Clicks_{drop}}{Impressions_{drop}}$，需在降价事件发生后48小时窗口内，基于特定平台日志数据计算得出。

## Corrected Claim

主动降价卖家的基线咨询率 $CTR_{drop}$ 定义为降价事件后特定时间窗口内的点击率，具体窗口长度（如48小时）需依据平台具体规范或实验设计确定。

## Evidence

[质询]该陈述包含具体的工程实现细节（48小时窗口、特定平台日志），属于经验事实或特定系统定义，无法从第一性原理推导，且参考来源未提供此具体参数支持。 | 逻辑自洽（CTR定义及时间窗口在业务场景中合理），但参考来源[1]仅讨论亚马逊价格机制，未涉及CTR计算的具体时间窗口或日志定义，属于经验事实且缺来源直接支持。

## Search Query

second-hand platform seller price drop CTR 48 hours baseline click-through rate data

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2037125292804855584&rut=1d44db1d627bffe2800d6d809aeee784814da67f1945a607f50988934abd9af2', 'type': 'ddg', 'title': '促销折扣一直报错？亚马逊2026年价格新政全解析（附6大实操解法）'}
