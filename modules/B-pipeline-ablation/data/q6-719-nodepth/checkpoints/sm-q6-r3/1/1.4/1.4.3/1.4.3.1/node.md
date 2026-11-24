# N181: 工作点A（高命中率/高容量成本）：假设单POP缓存容量 S_pop=10TB，日活500万，人均请求10次，日均请求量 R=50M；基于Zipf α=0.8，若

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N52

## Claim

工作点A（高命中率/高容量成本）：假设单POP缓存容量 S_pop=10TB，日活500万，人均请求10次，日均请求量 R=50M；基于Zipf α=0.8，若热门对象覆盖60%流量，则 U（唯一未命中对象数）≈ 0.4 × 50M / (1 - 1/K^0.8) 的逆运算，需解出 K 使得 Hit_Rate ≥ 90%，此时 U/R ≈ 0.1，Hit_Rate = 0.9。

## Corrected Claim

工作点A（高命中率/高容量成本）：在假设单POP缓存容量 S_pop=10TB、日活500万、人均请求10次、日均请求量 R=50M，且流量分布符合Zipf(α=0.8)并设定热门对象覆盖60%流量的前提下，估算得出唯一未命中对象数占比 U/R ≈ 0.1，对应命中率 Hit_Rate ≈ 0.9。

## Evidence

[质询]该陈述包含具体的经验参数（如Zipf指数α=0.8、热门对象覆盖60%流量、Hit_Rate=0.9等），这些并非第一性原理可推导的数学恒等式，而是基于特定假设的工程估算。参考来源均未提供这些具体数值或验证该特定场景下的命中率计算结果，属于缺乏外部证据支持的经验事实。 | 逻辑上自洽（命中率与未命中率的互补关系成立），但参考来源[1]和[2]仅涉及通用公式或计算机组成原理Cache，未覆盖CDN/POP缓存的具体Zipf分布参数及命中率估算，属于经验事实且缺来源直接支持。

## Search Query

CDN cache hit rate calculation Zipf distribution 90% hit rate object count

## Retrieval Sources

- {'url': 'https://peterguy326.github.io/soft-exam-topic-exam-calculations/index.html&rut=13dab8b179b930b49901650de000686b6e1b0cbddca6fd09da58cfd5b7544d02', 'type': 'ddg', 'title': '软考专题 · 计算题专项（计算机系统 + 网络 + 项目管理 + 软件度量｜公式速查 + 例题） | Peter の 技术小屋'}
- {'url': 'https://blog.csdn.net/weixin_29611239/article/details/162776267&rut=e1bdf12c70f33b24991e8bd602589ac18b12fe0e8478807b63a3cfc73e360d97', 'type': 'ddg', 'title': '计算机组成原理 Cache 命中率计算：3步实战解析与访存时间优化-CSDN博客'}
