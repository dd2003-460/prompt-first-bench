# N231: 硬件价格季度失效阈值量化：定义价格波动率 σ_price 为近4个季度MSRP或市场均价的标准差/均值。若 σ_price > 10%，则触发TCO重算；若 σ

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N92

## Claim

硬件价格季度失效阈值量化：定义价格波动率 σ_price 为近4个季度MSRP或市场均价的标准差/均值。若 σ_price > 10%，则触发TCO重算；若 σ_price ≤ 5%，则维持原TCO不变。当前RTX 4090市场均价波动率约为 [待核验：需查询近4季度eBay/京东价格数据]，若超过10%则N86中的±15%失效阈值需下调。

## Corrected Claim

硬件价格季度失效阈值量化：定义价格波动率 σ_price 为近4个季度MSRP或市场均价的标准差/均值。若 σ_price > 10%，则触发TCO重算；若 σ_price ≤ 5%，则维持原TCO不变。当前RTX 4090市场均价波动率需查询近4季度eBay/京东价格数据以确定是否超过10%阈值，若超过则N86中的±15%失效阈值需下调。

## Evidence

[质询]该陈述包含具体的经验事实断言（RTX 4090近4季度市场均价波动率），但原文标记为[待核验]，且参考来源仅涉及金融波动率定义，未提供GPU硬件价格数据，无法验证具体数值或阈值触发的实际状态。 | 逻辑自洽（波动率定义及阈值逻辑合理），但属于经验事实（硬件价格），参考来源[1]仅解释金融波动率概念，与GPU价格无关，缺乏直接支持，依据经验事实排除条款降级。

## Search Query

RTX 4090 market price volatility last 4 quarters standard deviation

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1945152227128877088&rut=f6c18e113e444800adaa2e1e45d2dc3c8a6bc037e86305442aad0531cf59656c', 'type': 'ddg', 'title': '量化交易基础(七)----波动率 - 知乎'}
