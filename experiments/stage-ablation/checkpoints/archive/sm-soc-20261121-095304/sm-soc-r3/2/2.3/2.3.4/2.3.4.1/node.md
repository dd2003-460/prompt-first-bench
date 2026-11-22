# N128: 基准咨询到达率 λ_base 的量化：定义为无风控惩罚、无价格异常时，单位时间（如 24 小时）内该类目商品平均接收到的有效买家咨询数量，需基于平台后台日志中正

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N43

## Claim

基准咨询到达率 λ_base 的量化：定义为无风控惩罚、无价格异常时，单位时间（如 24 小时）内该类目商品平均接收到的有效买家咨询数量，需基于平台后台日志中正常定价商品的 P50 或均值计算。

## Corrected Claim

基准咨询到达率 λ_base 通常定义为无风控惩罚、无价格异常时，单位时间内该类目商品平均接收到的有效买家咨询数量，具体统计口径（如P50或均值）需依据平台数据分布特性确定。

## Evidence

[质询]该陈述属于特定业务场景下的经验性定义与统计口径选择（P50 vs 均值），并非第一性原理可推导的数学或物理事实，且参考来源中未包含电商咨询率的具体量化标准或行业通用定义，存在口径主观性风险。 | 逻辑自洽，但参考来源[1]讨论AIGC查重，[2]讨论金融风控术语，均与电商咨询率量化无关，无可用外部证据支持具体统计方法（P50/均值）的普适性，属经验事实缺来源支持。

## Search Query

average inquiry rate per day normal priced items second hand platform benchmark

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2021016902990841364&rut=79128d8c65aec18ea7966f77bb5cf2763890bdb24408351696ae6b0563dec612', 'type': 'ddg', 'title': 'Aigc查重率多少算正常？2026最新标准+降重避坑全攻略 - 知乎'}
- {'url': 'https://zhuanlan.zhihu.com/p/290720746&rut=b908e0d948d23ac42e8b26d08ef4c504b58495758a4afb622a91a6ebcfdfb5bc', 'type': 'ddg', 'title': '风控相关术语 - 知乎 - 知乎专栏'}
