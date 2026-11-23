# N226: 各POP点到源站的P99 RTT RTT_origin_P99(i)：取决于POP与源站的物理距离，典型值为10-50ms（同省）或50-100ms（跨省），需

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N70

## Claim

各POP点到源站的P99 RTT RTT_origin_P99(i)：取决于POP与源站的物理距离，典型值为10-50ms（同省）或50-100ms（跨省），需列出10个POP各自的具体值

## Corrected Claim

各POP点到源站的P99 RTT取决于物理距离及网络路径质量，通常同省延迟低于跨省，具体数值需根据实际网络拓扑和链路状况测量确定，典型量级在几十毫秒范围内。

## Evidence

[质询]该陈述包含具体的经验数值范围（10-50ms/50-100ms）和特定场景假设（同省/跨省），属于经验事实。参考来源仅解释了P99的定义或LLM延迟，未提供POP到源站RTT的具体数值或距离与延迟的对应关系，无法通过第一性原理严格推出具体毫秒数，且缺乏来源直接支持。 | 逻辑上RTT随距离增加而增加是合理的，但具体数值范围（10-50ms等）属于经验事实，参考来源[1][2]均与该具体数值无关，无法提供直接支持，故降级。

## Search Query

China origin server P99 RTT from edge POPs inter-provincial

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1907850060240257948&rut=f8568459f53c969be6c08e9ce6f128269cd34bc1378fc3538a037e0cd1594e62', 'type': 'ddg', 'title': '运维必懂：监控指标中的 P90、P95、P99，到底是个啥？'}
- {'url': 'https://zhuanlan.zhihu.com/p/2043804951944638544&rut=edb2bec3a1ee5e3fcd6cc252dd4a976d234f2700b1df9ad7b6f796880959ffde', 'type': 'ddg', 'title': 'vllm学习笔记 (一):TTFT,TPOT,P99 E2E latency,throughput受什么影响'}
