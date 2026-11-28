# N203: GPT-4o API 在 50k context 下的 TTFT 分解为：网络往返时间 RTT (约 100-200ms) + 服务端 Queueing Tim

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

GPT-4o API 在 50k context 下的 TTFT 分解为：网络往返时间 RTT (约 100-200ms) + 服务端 Queueing Time (随负载波动，P99 可达 1-3s) + Prefill Time (GPT-4o 优化后极短，<200ms)；总 TTFT 中 Queueing 占比 >60%，具有高度随机性，而本地推理延迟确定性高。

## Corrected Claim

GPT-4o API 的 TTFT 通常由网络往返时间、服务端排队时间和预填充时间组成。其中排队时间受负载影响显著，波动较大，往往占据总延迟的主要部分；相比之下，本地推理延迟受网络波动影响较小，确定性更高。

## Evidence

[质询]具体数值（如RTT 100-200ms, P99 1-3s, Prefill <200ms, Queueing占比>60%）属于高度依赖实时负载、地理位置及具体部署环境的经验数据，缺乏通用稳定性，且不同测试环境差异巨大，难以作为固定事实陈述。 | 先验知识/题面给定，逻辑校验通过（TTFT分解逻辑自洽，量级符合一般LLM API延迟特征），但具体数值为经验事实且无外部来源支持，故降级。
