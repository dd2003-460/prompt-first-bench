# N182: Qwen3-27B 从 BF16 量化至 FP8 (E4M3) 在 MMLU 基准上的准确率下降幅度 Δ_MMLU 需通过实际量化后模型评测获得；社区初步报告指

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58

## Claim

Qwen3-27B 从 BF16 量化至 FP8 (E4M3) 在 MMLU 基准上的准确率下降幅度 Δ_MMLU 需通过实际量化后模型评测获得；社区初步报告指出对于 27B 规模模型，FP8 量化在 MMLU 上的损失通常 < 0.5%，但具体数值需引用 Qwen 官方技术报告或权威第三方评测 (如 LMSYS Chatbot Arena 子集评测)。

## Corrected Claim

Qwen3-27B 从 BF16 量化至 FP8 (E4M3) 在 MMLU 基准上的准确率下降幅度需通过实际量化后模型评测获得；社区报告指出对于 27B 规模模型，FP8 量化在 MMLU 上的损失通常较小，但具体数值需引用 Qwen 官方技术报告或权威第三方评测。

## Evidence

[质询]该陈述包含具体的经验性数值断言（'损失通常 < 0.5%'），属于硬件/模型性能相关的经验事实，无法从第一性原理推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源，无法验证具体数值阈值）。

## Search Query

Qwen3-27B FP8 quantization MMLU accuracy drop benchmark
