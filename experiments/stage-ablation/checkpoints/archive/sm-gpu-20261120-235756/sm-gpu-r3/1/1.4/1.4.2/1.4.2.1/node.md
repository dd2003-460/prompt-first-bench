# N157: FP8 (E4M3) 权重在 MMLU 基准测试中的准确率下降幅度：基于 Llama-3-70B 及 Qwen-2 系列公开量化基准，FP8 相比 BF16 的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

FP8 (E4M3) 权重在 MMLU 基准测试中的准确率下降幅度：基于 Llama-3-70B 及 Qwen-2 系列公开量化基准，FP8 相比 BF16 的 MMLU 准确率损失通常在 0.1% - 0.3% 之间（例如 BF16: 84.2% -> FP8: 83.9%），具体数值需参考 NVIDIA TensorRT-LLM 或 vLLM 官方发布的 Qwen3 量化评测报告。

## Corrected Claim

FP8 (E4M3) 权重在 MMLU 基准测试中相比 BF16 的准确率损失通常极小（一般在 0.1% - 0.5% 范围内，具体取决于模型和实现），具体数值需参考 NVIDIA TensorRT-LLM 或 vLLM 官方发布的量化评测报告。

## Evidence

[质询]该陈述包含具体的经验性数值（0.1%-0.3% 损失幅度及具体基准分数），属于硬件/模型量化性能的经验事实，无法从第一性原理推导。且检索无可用来源，无法验证具体数值是否准确，存在数值偏差或特定模型/配置下损失更大的可能性。 | 经验事实，逻辑自洽（FP8量化通常精度损失极小）但缺来源支持，且无外部证据验证具体数值。

## Search Query

Qwen3-27B FP8 E4M3 MMLU accuracy degradation vs BF16 benchmark
