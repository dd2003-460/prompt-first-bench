# N31: 对于无硬性延迟约束的本地工作站，'Time-to-First-Token' (TTFT) 的权重应降至 0，而 'Inter-Token Latency' (I

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

对于无硬性延迟约束的本地工作站，'Time-to-First-Token' (TTFT) 的权重应降至 0，而 'Inter-Token Latency' (ITL) 仅作为体验下限指标（例如 ITL < 50ms 为流畅，>200ms 为不可用）。因此，性价比排序应完全由 'Steady-State Throughput' (每秒生成 token 数) 主导，而非首字延迟。

## Corrected Claim

对于无硬性延迟约束的本地工作站，性价比排序主要由 'Steady-State Throughput' 主导，'Time-to-First-Token' (TTFT) 的重要性相对降低，而 'Inter-Token Latency' (ITL) 主要影响阅读体验的流畅度。

## Evidence

[质询]该陈述包含具体的经验阈值（ITL < 50ms 为流畅，> 200ms 为不可用）以及绝对化的权重设定（TTFT 权重降至 0），这些属于经验事实而非第一性原理可推导内容，且参考来源未提供这些具体数值或权重建议的支持。 | 逻辑上，在无硬性延迟约束的本地场景下，吞吐量确实是核心指标，但具体的 ITL 阈值（50ms/200ms）和 TTFT 权重归零属于经验性判断，参考来源 [1][2][3] 仅定义了 TTFT 概念及其重要性，未涉及具体阈值或权重分配策略，故缺乏直接来源支持。

## Retrieval Sources

- {'url': 'https://www.ibm.com/cn-zh/think/topics/time-to-first-token&rut=aa6bbc6a26bc5cd3ef6d794121e61f4285f5a55bd4b456933e18a293d2b5dde5', 'type': 'ddg', 'title': '首令牌时间（Ttft） | Ibm'}
- {'url': 'https://blog.csdn.net/pythonhy/article/details/159425882&rut=510a75242db2e3bf64e319f81f1f73937695b7944c2f31e6858379c805032021', 'type': 'ddg', 'title': '大模型Prompt Prefill慢与首Token延迟优化：原理剖析与工程实践'}
- {'url': 'https://www.ibm.com/think/topics/time-to-first-token&rut=ec8157d9e201ec2b6cb47571d6594ae19edb3d5e42e5974a2397df71321e90df', 'type': 'ddg', 'title': 'Time to First Token (TTFT) | IBM'}
