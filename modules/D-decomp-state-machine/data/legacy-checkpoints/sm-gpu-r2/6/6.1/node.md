# N85: NVFP4 量化在 Qwen3-27B 上的 MMLU 准确率下降具体值为 0.8% ± 0.3%，基于 NVIDIA TensorRT-LLM v0.9 官方

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

NVFP4 量化在 Qwen3-27B 上的 MMLU 准确率下降具体值为 0.8% ± 0.3%，基于 NVIDIA TensorRT-LLM v0.9 官方基准测试数据

## Corrected Claim

NVFP4 量化在 Qwen3-27B 上的 MMLU 准确率存在轻微下降（具体数值需参考 NVIDIA TensorRT-LLM 官方基准测试数据）

## Evidence

[质询]具体数值（0.8% ± 0.3%）及特定版本（TensorRT-LLM v0.9）属于经验事实，缺乏来源支持，且不同量化实现或模型微调版本可能导致结果波动，无法仅凭逻辑推导确认该精确数值。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

Qwen3-27B NVFP4 MMLU accuracy drop TensorRT-LLM benchmark
