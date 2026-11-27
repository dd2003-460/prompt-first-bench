# N442: NVFP4 量化在 Qwen3-27B 上的 MMLU 准确率下降 ΔMMLU_NVFP4 需参考 NVIDIA TensorRT-LLM 或 HuggingF

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N143

## Claim

NVFP4 量化在 Qwen3-27B 上的 MMLU 准确率下降 ΔMMLU_NVFP4 需参考 NVIDIA TensorRT-LLM 或 HuggingFace 官方发布的 FP4 量化模型基准测试数据，预期范围在 1%-3% 之间（介于 FP8 和 W4 之间），具体数值需查证 [待核验]

## Corrected Claim

NVFP4 量化在 Qwen3-27B 上的 MMLU 准确率下降具体数值需参考 NVIDIA TensorRT-LLM 或 HuggingFace 官方发布的 FP4 量化模型基准测试数据，通常预期介于 FP8 和 W4 量化之间，但具体范围（如 1%-3%）未经证实。

## Evidence

[质询]该陈述包含具体的经验性数值范围（1%-3%）和特定模型/量化组合的性能预期，属于硬件/模型基准测试数据，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B NVFP4 quantization MMLU accuracy benchmark
