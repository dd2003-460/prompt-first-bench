# N192: Qwen3-27B 在 NVFP4 量化下 MMLU 基准的绝对准确率数值 [待核验: 需查找 NVIDIA TensorRT-LLM 优化后的 Qwen3 量

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N58

## Claim

Qwen3-27B 在 NVFP4 量化下 MMLU 基准的绝对准确率数值 [待核验: 需查找 NVIDIA TensorRT-LLM 优化后的 Qwen3 量化报告]；若缺失，参考 Llama-3-70B NVFP4 数据 (损失约 0.8%)，因 27B 模型参数更密集，预计损失略高，为 1.0%-1.5%

## Corrected Claim

Qwen3-27B 在 NVFP4 量化下的 MMLU 基准绝对准确率数值暂无确切公开数据；参考 Llama-3-70B 的量化损失（约 0.8%），推测 Qwen3-27B 的损失可能在 1.0%-1.5% 区间，但需以实际测试报告为准。

## Evidence

[质询]该陈述包含具体的经验性数值预测（1.0%-1.5%），且明确标注为‘待核验’和‘预计’，缺乏直接来源支持，属于无法从第一性原理严格推导的经验事实。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值为基于类比模型的推测而非确定事实）

## Search Query

Qwen3-27B NVFP4 W4A4 MMLU accuracy benchmark
