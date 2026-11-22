# N122: 在 MMLU-Pro 基准测试中，Qwen3-27B FP8 量化模型的准确率绝对下降值通常为 0.2% - 0.5% (例如从 75.2% 降至 74.8%)

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N36

## Claim

在 MMLU-Pro 基准测试中，Qwen3-27B FP8 量化模型的准确率绝对下降值通常为 0.2% - 0.5% (例如从 75.2% 降至 74.8%)，而在 IFEval 指令遵循基准中下降幅度 <0.3%，证实了其在知识检索和指令遵循任务上的稳定性。

## Corrected Claim

在 MMLU-Pro 和 IFEval 等基准测试中，Qwen3-27B FP8 量化模型通常表现出较高的稳定性，准确率下降幅度较小（通常在 0.5% 以内），但具体数值取决于量化方法和实现细节。

## Evidence

[质询]具体数值（75.2%降至74.8%）及特定基准（MMLU-Pro, IFEval）的量化下降幅度属于经验事实，缺乏来源支持，且不同量化实现（如SmoothQuant, GPTQ等）可能导致结果差异，无法仅凭逻辑推导确认具体数值。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B FP8 quantization MMLU-Pro IFEval accuracy drop percentage benchmark
