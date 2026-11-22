# N383: RTX 5090 采用 GDDR7 显存，其有效带宽利用率（Memory Efficiency）在 vLLM 等框架下通常可达 85%-90%，而 H100 S

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N134

## Claim

RTX 5090 采用 GDDR7 显存，其有效带宽利用率（Memory Efficiency）在 vLLM 等框架下通常可达 85%-90%，而 H100 SXM 采用 HBM3e，受高功耗和散热限制，在长时间满载推理下实际带宽利用率约为 75%-80%，此效率差异需修正理论带宽比，修正后 RTX 5090 的实际吞吐量约为 H100 的 55%-60%。

## Corrected Claim

RTX 5090 采用 GDDR7 显存，H100 SXM 采用 HBM3e。在 vLLM 等框架下，由于架构、功耗及散热差异，两者的实际带宽利用率和推理吞吐量存在差异，但具体效率百分比及吞吐量比值需依据特定负载和基准测试确定，不宜直接断定为固定区间。

## Evidence

[质询]具体数值（85%-90% vs 75%-80% 利用率，55%-60% 吞吐量比）缺乏公开基准测试支持，且将复杂的推理吞吐量差异简单归因于‘带宽利用率’修正，忽略了计算密度、显存容量及架构差异的影响，属于过度简化的经验推测。 | 先验知识/题面给定，逻辑校验通过，但具体效率百分比及吞吐量比值为经验性估计，缺乏直接来源支持，故降级。

## Search Query

GDDR7 vs HBM3e memory bandwidth utilization efficiency LLM inference
