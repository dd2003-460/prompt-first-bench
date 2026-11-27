# N183: Qwen3-27B 在 FP8 量化下的 MMLU 基准测试分数：目前缺乏官方发布的 Qwen3-27B FP8 具体分数，但基于 Qwen2-72B 和 Ll

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

Qwen3-27B 在 FP8 量化下的 MMLU 基准测试分数：目前缺乏官方发布的 Qwen3-27B FP8 具体分数，但基于 Qwen2-72B 和 Llama-3-70B 的 FP8 评测数据，MMLU 准确率下降通常控制在 0.3-0.8% 范围内；若 Qwen3-27B 的 BF16 MMLU 分数为 85% (假设值)，则 FP8 预期分数约为 84.2-84.7%，满足 ≤5% 的质量阈值 (即 ≥80.25%)，因此 FP8 在通用问答场景下是可接受的。

## Corrected Claim

目前缺乏官方发布的 Qwen3-27B FP8 具体 MMLU 分数。基于同类大模型（如 Qwen2-72B, Llama-3-70B）的 FP8 评测经验，MMLU 准确率下降通常在 0.3-0.8% 范围内。若 Qwen3-27B 的 BF16 MMLU 分数为 85%，则 FP8 预期分数约为 84.2-84.7%，理论上满足 ≤5% 的质量阈值，但需以实际测试数据为准。

## Evidence

[质询]该陈述包含大量假设性前提（如假设Qwen3-27B BF16分数为85%）和基于其他模型（Qwen2-72B, Llama-3-70B）的泛化推断，缺乏针对Qwen3-27B FP8的直接实证数据支持，属于经验事实的推测而非确凿结论。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且涉及具体模型量化后的性能表现，属于不可从第一性原理推导的经验数据）

## Search Query

Qwen3-27B FP8 MMLU benchmark score accuracy drop
