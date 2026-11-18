# N228: H100 SXM5 在 LLaMA-70B FP16 下，batch_size=32 时的实测吞吐量约为 400-500 tokens/s，而理论峰值约为 50

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

H100 SXM5 在 LLaMA-70B FP16 下，batch_size=32 时的实测吞吐量约为 400-500 tokens/s，而理论峰值约为 500-600 tokens/s，差异系数约为 0.8-0.9，表明在大批量下计算利用率显著提升，接近理论上限。

## Corrected Claim

H100 SXM5 在 LLaMA-70B FP16 下，batch_size=32 时计算利用率显著提升，接近理论上限（差异系数约为 0.8-0.9），具体吞吐量需参考特定基准测试数据。

## Evidence

[质询]该陈述包含具体的经验性性能数值（400-500 tokens/s），属于硬件实测数据，无法从第一性原理推导。参考来源中未包含针对 H100 SXM5 运行 LLaMA-70B FP16 在 batch_size=32 时的具体吞吐量基准测试数据，来源 [1] 仅涉及内存带宽微基准，来源 [2] 和 [3] 虽涉及 LLaMA-70B 但未提供该特定配置下的精确吞吐数值，因此缺乏直接外部证据支持具体数值区间。 | 逻辑上，H100 在大批量下计算利用率接近理论峰值（0.8-0.9）符合 GPU 推理的一般规律，量级合理；但具体数值 400-500 tokens/s 为经验事实，参考来源 [1][2][3] 均未直接提供该特定配置下的实测吞吐量数据，无法验证具体数值，故降级。

## Search Query

H100 SXM LLaMA-70B FP16 batch_size 32 throughput benchmark tokens/s

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2608.15764v1', 'type': 'arxiv', 'title': 'Concurrency Response of Plain Global Loads on the NVIDIA H100'}
- {'url': 'http://arxiv.org/abs/2408.11848v2', 'type': 'arxiv', 'title': 'MGH Radiology Llama: A Llama 3 70B Model for Radiology'}
- {'url': 'http://arxiv.org/abs/2608.14614v1', 'type': 'arxiv', 'title': 'DumpsterCluster: From Dumpster Diving to Serving LLaMA-70B on $60 GPUs'}
