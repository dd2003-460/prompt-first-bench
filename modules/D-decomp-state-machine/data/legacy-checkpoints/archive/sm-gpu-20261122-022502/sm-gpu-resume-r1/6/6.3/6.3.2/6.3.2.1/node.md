# N305: 2x RTX 4090 在 128K 上下文下的实际 Decode 吞吐：理论上限 74.6 tokens/s (单卡 INT4)，考虑 PCIe 互联延迟 (

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N109

## Claim

2x RTX 4090 在 128K 上下文下的实际 Decode 吞吐：理论上限 74.6 tokens/s (单卡 INT4)，考虑 PCIe 互联延迟 (10-20% 损失) 和 KV Cache 跨卡分片开销，实际吞吐预计为 55-65 tokens/s；若使用 vLLM PagedAttention 优化，可部分缓解碎片问题，但通信开销仍为主要瓶颈。

## Corrected Claim

2x RTX 4090 在 128K 上下文下的 Decode 吞吐受限于 PCIe 互联带宽与 KV Cache 跨卡通信开销，实际性能通常显著低于单卡理论上限，具体数值（如 55-65 tokens/s）需结合具体模型规模、Batch Size 及软件栈优化程度实测确定。

## Evidence

[质询]数值量级与具体参数缺乏实证支持：74.6 tokens/s 的理论上限及 55-65 tokens/s 的实际吞吐范围属于特定硬件配置下的经验性能数据，无法仅从第一性原理严格推导，且不同模型架构、Batch Size 及具体 PCIe 拓扑下波动较大，单一数值区间可能过于绝对。 | 先验知识/题面给定，逻辑校验通过（量纲合理，PCIe 瓶颈分析符合直觉），但作为经验事实缺乏外部来源直接支持，故降级。

## Search Query

2x RTX 4090 vLLM PagedAttention 128K context actual throughput
