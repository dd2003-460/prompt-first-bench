# N160: 在 TP=4 下，All-Reduce 通信延迟随序列长度线性增加，当 L>32k 时，通信开销占总推理时间的比例超过 20%，导致实际吞吐量 N_max 的理

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

在 TP=4 下，All-Reduce 通信延迟随序列长度线性增加，当 L>32k 时，通信开销占总推理时间的比例超过 20%，导致实际吞吐量 N_max 的理论值无法达成，需引入通信重叠优化。

## Corrected Claim

在 TP=4 下，All-Reduce 通信延迟随序列长度增加而显著上升，在大序列长度场景下通信开销占比高，导致实际吞吐量受限，需引入通信重叠优化。

## Evidence

[质询]陈述中关于“L>32k”的具体阈值以及“占比超过20%”的具体数值缺乏通用性，属于特定硬件/模型配置下的经验数据，且参考来源仅提供了定性分析（指出通信开销大、需要优化），并未提供该特定阈值和比例的定量支持，存在以偏概全或数据无据的风险。 | 来源[1]定性支持了TP下AllReduce通信开销显著及需引入重叠优化的结论，但未提供L>32k及20%的具体数值支持，属经验事实缺直接来源。

## Search Query

tensor parallelism all-reduce communication overhead long sequence latency

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/1954274548775125348&rut=b7888f0df948cdc05485d3917a9048ef4eacec2036a6024ee4a809891475ee9c', 'type': 'ddg', 'title': '从 0 实现单机多卡 TP Gemm+AllReduce 优化 - 知乎'}
