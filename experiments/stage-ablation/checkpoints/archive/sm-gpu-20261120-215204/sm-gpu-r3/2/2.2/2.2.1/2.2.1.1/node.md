# N203: FP8 (E4M3) 量化 Qwen3-27B 后在 MMLU 基准测试上的准确率下降具体数值为 0.2%，基于 Qwen 官方技术报告及 HuggingFac

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71

## Claim

FP8 (E4M3) 量化 Qwen3-27B 后在 MMLU 基准测试上的准确率下降具体数值为 0.2%，基于 Qwen 官方技术报告及 HuggingFace 社区基准测试数据，该值低于 N71 声称的 0.5% 阈值，表明 FP8 在通用知识任务上几乎无损。

## Corrected Claim

FP8 (E4M3) 量化 Qwen3-27B 后在 MMLU 基准测试上的准确率下降幅度较小（通常低于 0.5%），表明 FP8 在通用知识任务上几乎无损。

## Evidence

[质询]具体数值 0.2% 属于经验事实，且缺乏来源支持；不同量化实现（如 SmoothQuant, GPTQ, 原生 FP8）及评测设置可能导致准确率下降幅度在 0.1%-0.5% 之间波动，断言精确为 0.2% 且低于 0.5% 阈值缺乏直接证据支撑。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值 0.2% 及阈值比较的准确性）

## Search Query

Qwen3-27B FP8 E4M3 MMLU benchmark accuracy drop percentage
