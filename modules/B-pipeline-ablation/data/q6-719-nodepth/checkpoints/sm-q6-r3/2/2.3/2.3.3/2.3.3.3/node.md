# N184: 交换机处理延迟 L_switching 的 P99 值约为 10-20ms（受队列排队和CPU抖动影响），因此在计算 P99 总延迟时，RTT_p99 = 2 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N58

## Claim

交换机处理延迟 L_switching 的 P99 值约为 10-20ms（受队列排队和CPU抖动影响），因此在计算 P99 总延迟时，RTT_p99 = 2 * L_prop + L_switching_p99，其中 L_switching_p99 贡献了总延迟的 70%-80%，远超传播延迟本身。

## Corrected Claim

交换机处理延迟 L_switching 的 P99 值受队列排队和CPU抖动影响，在特定高负载或复杂网络环境下可能达到 10-20ms 量级，此时在计算 P99 总延迟时，L_switching_p99 可能成为主要延迟成分，但具体数值和占比需根据实际网络环境测量确定。

## Evidence

[质询]数值量级与具体比例缺乏依据：交换机P99延迟10-20ms及占比70%-80%属于特定网络环境下的经验数据，非通用物理定律或第一性原理可推导，且不同网络拓扑、设备性能下差异巨大，无法从通用原理推出固定比例。 | 经验事实，逻辑自洽但缺来源支持（来源[1]仅解释P99定义，未提供交换机延迟具体数值或占比数据）

## Search Query

network switch processing latency P99 queueing delay ms

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1907850060240257948&rut=f8568459f53c969be6c08e9ce6f128269cd34bc1378fc3538a037e0cd1594e62', 'type': 'ddg', 'title': '运维必懂：监控指标中的 P90、P95、P99，到底是个啥？'}
