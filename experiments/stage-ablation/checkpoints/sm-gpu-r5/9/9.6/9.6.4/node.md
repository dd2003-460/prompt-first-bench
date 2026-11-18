# N288: Apple M2 Ultra 在 llama.cpp 或 MLX 框架下，Batch=1 时的实际实测吞吐量通常为理论带宽上限的 70%-90%（因为 Appl

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N111

## Claim

Apple M2 Ultra 在 llama.cpp 或 MLX 框架下，Batch=1 时的实际实测吞吐量通常为理论带宽上限的 70%-90%（因为 Apple Silicon 内存子系统效率较高且无 PCIe 瓶颈），预计实际值在 10-13 tokens/s (BF16) 或 20-26 tokens/s (INT8) 范围。

## Corrected Claim

Apple M2 Ultra 在 llama.cpp 或 MLX 框架下，Batch=1 时的实际实测吞吐量通常受限于内存带宽，具体数值取决于模型参数量，一般可达理论带宽上限的较高比例（因无PCIe瓶颈），但具体 tokens/s 数值需结合特定模型规模确定。

## Evidence

[质询]该陈述包含具体的硬件性能数值（10-13 tokens/s, 20-26 tokens/s）和效率百分比（70%-90%），属于经验事实。参考来源[1]是关于LaFeAsO材料磁相互作用的物理学论文，与Apple M2 Ultra芯片性能或LLM推理吞吐量完全无关，无法提供外部支持。此外，具体吞吐量高度依赖于模型参数量（如7B, 13B, 70B等），未指定模型规模使得数值断言缺乏明确基准，存在口径模糊的风险。 | 参考来源[1]与事实主题无关（无可用外部证据）。该事实为经验事实（硬件性能指标），逻辑上量级合理（M2 Ultra带宽约800GB/s，对于中等规模模型，10-26 tokens/s在合理范围内），但缺乏直接来源支持，依据经验事实排除条款降级。

## Search Query

Apple M2 Ultra 192GB LLM inference throughput llama.cpp MLX tokens per second

## Retrieval Sources

- {'url': 'http://arxiv.org/abs/1303.4033v1', 'type': 'arxiv', 'title': 'Two-dimensional magnetic interactions in LaFeAsO'}
