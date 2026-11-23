# N119: 回源延迟 T_origin_P99 的具体数值：基于边缘节点到源站的距离 D_origin（通常<500km），RTT_origin ≈ 10-20ms，T_o

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N32

## Claim

回源延迟 T_origin_P99 的具体数值：基于边缘节点到源站的距离 D_origin（通常<500km），RTT_origin ≈ 10-20ms，T_origin_processing ≈ 5-15ms，T_origin_queue ≈ 5-10ms，则 T_origin_P99 ≈ 20-45ms [待核验]

## Corrected Claim

回源延迟 T_origin_P99 通常由 RTT、处理时间和排队时间组成，在典型边缘节点到源站距离<500km的场景下，其数值量级通常在几十毫秒范围内（具体数值依源站性能而定）。

## Evidence

[质询]该陈述包含具体的经验性参数（如处理时间5-15ms、排队时间5-10ms），这些数值高度依赖于源站的具体硬件配置、软件栈复杂度及负载情况，并非物理定律或通用标准，属于经验事实。参考来源仅解释了P99的定义，未提供CDN回源延迟的具体数值支持，因此无法验证其具体数值的准确性。 | 逻辑上各分量相加得到总和（10-20 + 5-15 + 5-10 = 20-45ms）自洽，量级符合一般网络延迟直觉；但参考来源[1]仅定义P99概念，与具体延迟数值无关，属于经验事实且缺乏直接来源支持。

## Search Query

origin server P99 latency CDN back-to-origin 2024

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1907850060240257948&rut=f8568459f53c969be6c08e9ce6f128269cd34bc1378fc3538a037e0cd1594e62', 'type': 'ddg', 'title': '运维必懂：监控指标中的 P90、P95、P99，到底是个啥？'}
