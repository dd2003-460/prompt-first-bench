# N284: H100 SXM5 在 vLLM/TensorRT-LLM 框架下，Batch=1 时的实际实测吞吐量通常在理论带宽上限的 60%-80% 之间，主要损耗来自 

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N110

## Claim

H100 SXM5 在 vLLM/TensorRT-LLM 框架下，Batch=1 时的实际实测吞吐量通常在理论带宽上限的 60%-80% 之间，主要损耗来自 Attention 计算瓶颈和 Kernel Launch 开销，具体数值需参考 NVIDIA 官方 LLM 推理基准报告。

## Corrected Claim

H100 SXM5 在 vLLM/TensorRT-LLM 框架下，Batch=1 时的实际实测吞吐量通常显著低于理论带宽上限，主要损耗来自 Attention 计算瓶颈和 Kernel Launch 开销，具体数值需参考 NVIDIA 官方 LLM 推理基准报告或相关实测研究。

## Evidence

[质询]该陈述包含具体的经验数值范围（60%-80%）和特定框架下的性能表现，属于经验事实。参考来源[1]仅讨论了H100 SXM5上内存受限内核的带宽并发响应机制（Little's Law, LDG bandwidth），并未提供vLLM/TensorRT-LLM在Batch=1时的实际吞吐量与理论带宽上限比值的实测数据，无法直接支持该具体数值区间。 | 逻辑自洽（Batch=1时Kernel Launch开销和Attention计算确实会导致利用率低于理论峰值），但参考来源[1]仅涉及底层内存带宽机制，未覆盖LLM推理框架层面的具体吞吐率实测数据，属于间接相关且缺乏直接数值支持。

## Search Query

H100 SXM5 Qwen 27B vLLM measured throughput tokens per second batch 1

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/2608.15764v1', 'type': 'arxiv', 'title': 'Concurrency Response of Plain Global Loads on the NVIDIA H100'}
