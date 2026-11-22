# N92: 实际吞吐量修正因子 (Efficiency Factor)：理论值需乘以硬件利用率 (MFU/MBU)。消费级GPU在长上下文推理中MBU通常为40-60% (

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N15

## Claim

实际吞吐量修正因子 (Efficiency Factor)：理论值需乘以硬件利用率 (MFU/MBU)。消费级GPU在长上下文推理中MBU通常为40-60% (受PCIe/显存控制器限制)，数据中心级SXM模组MBU可达60-80% (HBM3低延迟)。因此RTX 4090实际Decode ≈ 16.8 × 0.5 ≈ 8.4 tokens/s，H100实际Decode ≈ 55.8 × 0.7 ≈ 39.1 tokens/s。

## Corrected Claim

实际吞吐量修正因子 (Efficiency Factor)：理论值需乘以硬件利用率 (MFU/MBU)。消费级GPU在长上下文推理中MBU通常较低，数据中心级SXM模组MBU较高。具体数值需根据实际硬件配置和负载情况测定。

## Evidence

[质询]参考来源[1]讨论的是工业工程中的效率因子（工时与允许时间的关系），与GPU硬件利用率（MFU/MBU）完全无关，属于主题不匹配；且具体数值（如4090的50%、H100的70%）属于经验事实，缺乏直接来源支持。 | 逻辑自洽（吞吐量=理论值×利用率），但参考来源[1]与GPU性能无关，无法提供外部证据支持具体数值，依据经验事实排除条款降级。

## Search Query

LLM inference memory bandwidth utilization efficiency RTX 4090 vs H100 32k context

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Efficiency_factor&rut=135966d8768e830b9af3c287342520e2b8a39759a33442e362605d6b48b7e06d', 'type': 'ddg', 'title': 'Efficiency factor - Wikipedia'}
