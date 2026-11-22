# N169: llama.cpp 在 Qwen3-27B Q4_K_M 量化下，HumanEval Pass@1 准确率相比 BF16 下降约 5-8% [待核验]，MMLU

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N51

## Claim

llama.cpp 在 Qwen3-27B Q4_K_M 量化下，HumanEval Pass@1 准确率相比 BF16 下降约 5-8% [待核验]，MMLU 准确率下降约 3-5%；Q8_0 量化下，HumanEval Pass@1 下降约 1-2%，MMLU 下降约 0.5-1%；因此 Q4_K_M 在精度敏感任务中不被推荐，Q8_0 更适合本地工作站推理

## Corrected Claim

llama.cpp 在 Qwen3-27B 模型上，Q4_K_M 量化相比 BF16 会导致 HumanEval 和 MMLU 准确率出现一定程度的下降，而 Q8_0 量化带来的精度损失显著小于 Q4_K_M，因此对于精度敏感任务，Q8_0 是更推荐的本地推理量化方案。

## Evidence

[质询]具体数值范围（如5-8%、3-5%）属于经验事实，缺乏特定模型（Qwen3-27B）在特定量化格式下的公开基准测试数据支持，且不同评测集版本可能导致结果波动，无法从第一性原理推导。 | 经验事实，逻辑自洽（量化精度降低通常导致性能下降，Q8_0优于Q4_K_M符合常识）但缺来源支持，且检索无可用来源。

## Search Query

llama.cpp Qwen3-27B Q4_K_M Q8_0 HumanEval MMLU accuracy drop quantization
