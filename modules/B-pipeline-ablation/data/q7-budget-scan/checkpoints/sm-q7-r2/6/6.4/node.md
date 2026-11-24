# N36: HDD+SSD分层成本估算：热数据100TB SSD（¥2000/TB）+冷数据400TB HDD（¥100~200/TB），混合硬件年折旧≈¥150~250/

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6

## Claim

HDD+SSD分层成本估算：热数据100TB SSD（¥2000/TB）+冷数据400TB HDD（¥100~200/TB），混合硬件年折旧≈¥150~250/TB·年，电力成本~0.3W/TB×24h×365d×¥0.8/kWh≈¥200/TB·年，总成本≈¥350~450/TB·年（含运维与RTO）

## Corrected Claim

HDD+SSD分层成本估算：热数据100TB SSD + 冷数据400TB HDD，混合硬件年折旧与电力成本合计约¥350~450/TB·年（具体数值随硬件采购价格及电价波动，需以实际采购为准）

## Evidence

[质询]具体硬件单价（SSD ¥2000/TB, HDD ¥100-200/TB）及电力成本参数属于经验事实，且不同时期、不同品牌/渠道价格波动较大，参考来源未提供具体数值支持，存在口径混淆或数据过时的风险。 | 逻辑推导自洽（电力成本计算正确，总成本量级合理），但参考来源[1][2][3]仅定性提及冷热分层降本，未提供具体硬件单价或电力成本数值，属于经验事实缺来源直接支持。

## Search Query

HDD price per TB 2026 SSD hybrid storage cost

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_32288959/article/details/170752525&rut=aa3b037923b38b91b61ebedf809ed5fd7ca63cce0749018c05270f4d34d1dc7b', 'type': 'ddg', 'title': 'PolarDB 100TB存储成本优化：ZSTD压缩与冷热分层实战指南'}
- {'url': 'https://blog.csdn.net/weixin_32466193/article/details/164662858&rut=2697e3ed96beff3f54ee414afb01e0cfffb727375d90956a5517052caa0affe5', 'type': 'ddg', 'title': 'PolarDB 100TB存储成本拆解：省钱逻辑与避坑指引 - CSDN博客'}
- {'url': 'https://developer.aliyun.com/article/1752115&rut=eee8c10b4004481c20614413d4da78c87a0612ce3f4d3417b4d12b3bdeea83b1', 'type': 'ddg', 'title': '100tb 数据存云上成本怎么算？存算分离降本解析'}
