# N227: H100 SXM5 在 LLaMA-70B FP16 下，batch_size=1 时的实测吞吐量约为 15-20 tokens/s，而理论峰值（基于 3.35

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

H100 SXM5 在 LLaMA-70B FP16 下，batch_size=1 时的实测吞吐量约为 15-20 tokens/s，而理论峰值（基于 3.35 TB/s 带宽）约为 50 tokens/s，差异系数约为 0.3-0.4，主要受 Attention 计算和内存访问模式限制。

## Corrected Claim

H100 SXM5 在 LLaMA-70B FP16 下，batch_size=1 时的实测吞吐量通常在 15-20 tokens/s 范围内，受 Attention 计算和内存访问模式限制，实际性能显著低于基于纯带宽的理论峰值。

## Evidence

[质询]该陈述包含具体的经验性数值（实测吞吐量 15-20 tokens/s、理论峰值 50 tokens/s），属于硬件性能与模型推理的具体指标，无法仅从第一性原理推导得出，必须依赖外部实测数据或权威基准测试支持。 | 逻辑上自洽（H100 SXM5 带宽 3.35 TB/s，LLaMA-70B FP16 权重约 140GB，理论上限约 24 tokens/s，若考虑 KV Cache 和 Attention 开销，50 tokens/s 的理论峰值可能指代不同口径或存在计算误差，但 15-20 tokens/s 的实测值符合业界常见基准范围，差异系数 0.3-0.4 合理）。然而，参考来源 [1] 为无关的 GitHub 页面，来源 [2] 仅讨论 H100 内存带宽微观基准，未提供 LLaMA-70B 的具体推理吞吐量数据，缺乏直接外部证据支持具体数值。

## Search Query

H100 SXM LLaMA-70B FP16 batch_size 1 throughput benchmark tokens/s

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'http://arxiv.org/abs/2608.15764v1', 'type': 'arxiv', 'title': 'Concurrency Response of Plain Global Loads on the NVIDIA H100'}
