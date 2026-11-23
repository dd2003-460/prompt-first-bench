# N227: H100 SXM5 在 LLaMA-70B FP16 下，batch_size=1 时的实测吞吐量约为 15-20 tokens/s，而理论峰值（基于 3.35

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

H100 SXM5 在 LLaMA-70B FP16 下，batch_size=1 时的实测吞吐量约为 15-20 tokens/s，而理论峰值（基于 3.35 TB/s 带宽）约为 50 tokens/s，差异系数约为 0.3-0.4，主要受 Attention 计算和内存访问模式限制。

## Corrected Claim

H100 SXM5 在 LLaMA-70B FP16 下，batch_size=1 时的实测吞吐量通常显著低于基于 3.35 TB/s 带宽计算的理论峰值（约 50 tokens/s），主要受 Attention 计算和内存访问模式限制。

## Evidence

[质询]参考来源仅涉及H100内存带宽的微基准测试（Microbenchmarks），未包含LLaMA-70B在FP16下的具体推理吞吐量实测数据，无法直接验证15-20 tokens/s这一具体经验数值。 | 经验事实，逻辑自洽（带宽瓶颈下实测低于理论峰值符合直觉），但参考来源[1]仅讨论底层内存带宽特性，未直接覆盖LLaMA-70B的具体吞吐量数值，缺来源直接支持。

## Search Query

H100 SXM LLaMA-70B FP16 batch_size 1 throughput benchmark tokens/s

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2608.15764v1', 'type': 'arxiv', 'title': 'Concurrency Response of Plain Global Loads on the NVIDIA H100'}
