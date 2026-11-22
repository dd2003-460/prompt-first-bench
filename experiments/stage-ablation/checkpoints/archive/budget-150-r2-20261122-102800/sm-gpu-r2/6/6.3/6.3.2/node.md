# N138: 2× RTX 4090 部署 vLLM 时，由于缺乏 NVLink，张量并行 (TP=2) 的通信开销占比从单卡方案的 ~0% 上升至 ~15-20% (基于 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45, N46, N47

## Claim

2× RTX 4090 部署 vLLM 时，由于缺乏 NVLink，张量并行 (TP=2) 的通信开销占比从单卡方案的 ~0% 上升至 ~15-20% (基于 batch_size=1, seq_len=32K 估算)，导致实际吞吐量 (tokens/s) 相比理论带宽上限下降 15-20%。

## Corrected Claim

2× RTX 4090 部署 vLLM 时，由于缺乏 NVLink，张量并行 (TP=2) 的通信开销相比单卡方案显著上升（在长序列、小 batch 场景下估算约为 10-20%），导致实际吞吐量相比理论带宽上限出现明显下降。

## Evidence

[质询]数值量级与具体场景强相关，缺乏通用性：在 batch_size=1 且 seq_len=32K 的极端长序列场景下，计算密度极高，通信占比通常远低于 15-20%（往往在 5-10% 左右，取决于具体模型架构如 Llama-3 70B 或 405B 的层数和隐藏层维度）；15-20% 的开销更常见于中等 batch size 或较短序列场景，此处将特定估算值表述为普遍规律存在以偏概全风险。 | 先验知识/题面给定，逻辑校验通过：无 NVLink 时 PCIe 带宽瓶颈确实导致 TP 通信开销显著上升，量级在合理范围内，但具体百分比依赖模型参数，故降级为定性表述。
