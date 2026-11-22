# N193: RTX 4090 在 LLM Decode 阶段的实际有效内存带宽利用率修正系数 (Efficiency_Factor) 的量化范围：在 vLLM 或 Tens

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N56

## Claim

RTX 4090 在 LLM Decode 阶段的实际有效内存带宽利用率修正系数 (Efficiency_Factor) 的量化范围：在 vLLM 或 TensorRT-LLM 优化下，针对 24GB 显存卡，实测有效带宽通常为理论峰值 (1008 GB/s) 的 75%-85%。取中值 80% 计算，有效带宽 = 806.4 GB/s。

## Corrected Claim

在 vLLM 或 TensorRT-LLM 优化下，RTX 4090 (24GB) 在 LLM Decode 阶段的有效内存带宽利用率通常在理论峰值 (1008 GB/s) 的 70%-90% 之间波动，具体数值取决于模型架构、Batch Size 及 Kernel 实现细节，建议根据实际基准测试确定，而非固定取 80%。

## Evidence

[质询]该陈述包含具体的经验性参数（75%-85%利用率范围及80%中值），属于特定硬件在特定软件栈下的实测性能数据，无法从第一性原理推导。此外，RTX 4090显存为24GB，但LLM Decode阶段的带宽利用率受模型大小、Batch Size、Kernel优化程度等多重因素影响，固定为75%-85%缺乏普适性，且不同来源（如vLLM vs TensorRT-LLM）可能存在差异。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值为具体工程实测参数，非第一性原理可推导）。

## Search Query

RTX 4090 LLM decode memory bandwidth efficiency vllm
