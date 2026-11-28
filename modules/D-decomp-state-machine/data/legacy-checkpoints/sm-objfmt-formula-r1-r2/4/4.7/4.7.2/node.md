# N99: Qwen3-27B 在 NVFP4 量化后，MMLU 基准测试相对于 BF16 基线的具体得分下降值（Delta_MMLU），需查阅 NVIDIA Tensor

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N22

## Claim

Qwen3-27B 在 NVFP4 量化后，MMLU 基准测试相对于 BF16 基线的具体得分下降值（Delta_MMLU），需查阅 NVIDIA TensorRT-LLM 或 vLLM 针对 Qwen3-27B 的官方量化报告或第三方评测数据（预期范围 0.5%-2%，但需实证）

## Corrected Claim

Qwen3-27B 在 NVFP4 量化后，MMLU 基准测试相对于 BF16 基线通常会有轻微的性能下降，具体数值需查阅 NVIDIA TensorRT-LLM 或 vLLM 针对 Qwen3-27B 的官方量化报告或第三方评测数据以获取实证。

## Evidence

[质询]该陈述包含具体的经验性数值范围（0.5%-2%），属于特定模型在特定量化格式下的性能表现，无法从第一性原理推导，且缺乏官方或第三方实证数据支持，存在数值偏差风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体Delta值）

## Search Query

Qwen3-27B NVFP4 quantization MMLU benchmark score drop BF16 comparison
