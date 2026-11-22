# N326: L40S 运行 Qwen3-27B FP8 时的框架效率系数 k_framework 实测值，需查阅 NVIDIA 官方或第三方（如 HuggingFace B

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N97, N98, N99

## Claim

L40S 运行 Qwen3-27B FP8 时的框架效率系数 k_framework 实测值，需查阅 NVIDIA 官方或第三方（如 HuggingFace Blog, vLLM benchmark）针对 27B 级别模型在 L40S 上的 PagedAttention 效率数据，通常比理论带宽上限低 20-40%，具体数值需区分 Batch Size=1 和 Batch Size>1 的情况。

## Corrected Claim

L40S 运行 Qwen3-27B FP8 时的框架效率系数 k_framework 实测值通常低于理论带宽上限，具体数值受 Batch Size 和推理框架（如 vLLM）影响，需查阅 NVIDIA 官方或第三方基准测试数据获取精确值。

## Evidence

[质询]该陈述包含具体的经验性数值范围（20-40%效率损失）和特定硬件/模型组合（L40S + Qwen3-27B FP8），属于经验事实而非第一性原理可推导结论。由于缺乏直接来源支持，且不同框架（vLLM, TensorRT-LLM等）和Batch Size下的实际效率波动可能超出此范围，该具体数值区间缺乏实证依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体20-40%的效率损失范围及特定模型/硬件组合的实测数据）。

## Search Query

NVIDIA L40S Qwen3-27B FP8 throughput benchmark tokens per second vLLM
