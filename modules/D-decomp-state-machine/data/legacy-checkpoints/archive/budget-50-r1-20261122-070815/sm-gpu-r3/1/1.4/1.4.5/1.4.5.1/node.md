# N188: RTX 4090 在 INT4 权重 (13.5GB) + BF16 KV Cache (2.0GB) 配置下的实际 Decode 吞吐量实测中位数为 45-5

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N47

## Claim

RTX 4090 在 INT4 权重 (13.5GB) + BF16 KV Cache (2.0GB) 配置下的实际 Decode 吞吐量实测中位数为 45-55 tokens/s，理论带宽峰值 65 tokens/s，实际/理论效率比 (Efficiency Ratio) 约为 0.7-0.85，主要损失源于 Kernel Launch Overhead 和 Attention 计算瓶颈

## Corrected Claim

RTX 4090 在 INT4 权重 (13.5GB) + BF16 KV Cache (2.0GB) 配置下，Decode 吞吐量通常受限于显存带宽，理论峰值约 60-70 tokens/s，实际吞吐量因实现和模型架构不同而异，效率比通常在 0.7-0.85 之间，主要损失源于 Kernel Launch Overhead 和 Attention 计算瓶颈。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（吞吐量、效率比），属于经验事实。由于检索失败，无法验证具体数值（45-55 tokens/s, 0.7-0.85）的准确性，且不同模型架构（如Llama vs Mistral）和具体实现（如vLLM vs TGI）会导致显著差异，单一数值区间可能具有误导性。 | 经验事实，逻辑自洽但缺来源支持。RTX 4090显存带宽约1TB/s，INT4权重13.5GB，理论带宽限制下的最大吞吐量约为 1000GB/s / 13.5GB ≈ 74 tokens/s（假设纯带宽受限且无其他开销）。考虑到Attention计算、Kernel Launch Overhead及KV Cache读取，实际效率比0.7-0.85导致吞吐量降至45-55 tokens/s在物理和经济直觉上是合理的，但具体数值缺乏外部来源直接证实。

## Search Query

RTX 4090 Qwen3-27B INT4 vLLM benchmark tokens per second decode latency
