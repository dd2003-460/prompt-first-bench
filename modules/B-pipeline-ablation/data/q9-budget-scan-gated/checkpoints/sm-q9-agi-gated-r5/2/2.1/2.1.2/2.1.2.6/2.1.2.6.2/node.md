# N135: 解释 15-20s 延迟来源：若单序列独占延迟为 3.12s (基于 N75 α=0.5 修正值)，要达到 15-20s，必须存在额外的阻塞因素，如：1) 长上

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N63

## Claim

解释 15-20s 延迟来源：若单序列独占延迟为 3.12s (基于 N75 α=0.5 修正值)，要达到 15-20s，必须存在额外的阻塞因素，如：1) 长上下文 Prefill 的排队等待；2) KV Cache 溢出导致的 CPU Swap 开销（参考 N34，Swap 延迟可达 10x）；3) 批处理中其他长序列的干扰。在纯 Decode 且无 Swap 的理想情况下，8 并发不应导致 5 倍以上的延迟增加。

## Corrected Claim

解释 15-20s 延迟来源：若单序列独占延迟为 3.12s (基于 N75 α=0.5 修正值)，要达到 15-20s，必须存在额外的阻塞因素，如：1) 长上下文 Prefill 的排队等待；2) KV Cache 溢出导致的 CPU Swap 开销（参考 N34，Swap 延迟可达 10x）；3) 批处理中其他长序列的干扰。在纯 Decode 且无 Swap 的理想情况下，8 并发不应导致 5 倍以上的延迟增加。

## Evidence

先验知识/题面给定，逻辑校验通过：单序列3.12s与目标15-20s存在数量级差距，归因于Prefill排队、KV Swap（高延迟开销）及批处理干扰符合LLM推理系统的基本性能瓶颈原理，且排除了纯Decode理想情况下的线性扩展假设，逻辑自洽。

## Search Query

sources of high latency in concurrent LLM inference swap overhead
