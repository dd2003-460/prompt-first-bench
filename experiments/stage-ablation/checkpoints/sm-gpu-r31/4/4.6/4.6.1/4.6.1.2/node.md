# N228: H100 SXM5 在 LLaMA-70B FP16 下，batch_size=32 时的实测吞吐量约为 400-500 tokens/s，而理论峰值约为 50

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N73

## Claim

H100 SXM5 在 LLaMA-70B FP16 下，batch_size=32 时的实测吞吐量约为 400-500 tokens/s，而理论峰值约为 500-600 tokens/s，差异系数约为 0.8-0.9，表明在大批量下计算利用率显著提升，接近理论上限。

## Corrected Claim

H100 SXM5 在 LLaMA-70B FP16 下，batch_size=32 时的实测吞吐量通常接近理论峰值，计算利用率较高，但具体数值（如400-500 tokens/s）需依据特定硬件配置和软件栈的基准测试确定。

## Evidence

[质询]该陈述包含具体的硬件性能实测数据（H100 SXM5, LLaMA-70B, FP16, batch_size=32, 400-500 tokens/s），属于经验事实。参考来源中未包含任何关于LLaMA-70B在H100上的具体吞吐量基准测试数据，无法验证具体数值量级及差异系数。 | 经验事实，逻辑自洽但缺来源支持（来源[3]仅涉及H100内存带宽微基准，来源[4]涉及LLaMA 3 70B应用但未提供H100 FP16吞吐基准，来源[1][2]无关）。

## Search Query

H100 SXM LLaMA-70B FP16 batch_size 32 throughput benchmark tokens/s

## Retrieval Sources

- {'url': 'https://arxiv.org', 'type': None, 'title': 'direct-browser: arxiv.org'}
- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'http://arxiv.org/abs/2608.15764v1', 'type': 'arxiv', 'title': 'Concurrency Response of Plain Global Loads on the NVIDIA H100'}
- {'url': 'http://arxiv.org/abs/2408.11848v2', 'type': 'arxiv', 'title': 'MGH Radiology Llama: A Llama 3 70B Model for Radiology'}
