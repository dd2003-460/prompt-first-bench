# N220: 阿里云CDN P99延迟观测值 P99_observed_ali：在相同负载条件下，P99延迟通常比P50高30-100ms，具体数值需从监控仪表盘获取，用于计

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N68

## Claim

阿里云CDN P99延迟观测值 P99_observed_ali：在相同负载条件下，P99延迟通常比P50高30-100ms，具体数值需从监控仪表盘获取，用于计算分子差值

## Corrected Claim

在相同负载条件下，P99延迟通常高于P50延迟，具体差值（如30-100ms）需依据阿里云CDN监控仪表盘的实际观测数据确定，用于计算分子差值。

## Evidence

[质询]该陈述包含具体的经验数值范围（P99比P50高30-100ms），这属于特定系统（阿里云CDN）在特定负载下的经验观测值，无法从第一性原理或通用数学定义中严格推导得出，且不同业务场景下该差值波动极大，缺乏普适性。 | 来源[1]仅解释了P99等百分位数的定义，未提供阿里云CDN的具体延迟差值数据；该事实为经验观测值，逻辑上自洽（P99通常高于P50）但缺乏直接来源支持具体数值范围，依据经验事实排除条款降级。

## Search Query

Alibaba Cloud CDN P99 latency observed value high concurrency

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1907850060240257948&rut=f8568459f53c969be6c08e9ce6f128269cd34bc1378fc3538a037e0cd1594e62', 'type': 'ddg', 'title': '运维必懂：监控指标中的 P90、P95、P99，到底是个啥？'}
