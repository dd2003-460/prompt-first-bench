# N158: Qwen3-27B 在 BF16 精度下，使用 llama.cpp 框架（AVX2 加速，F16 精度）在 HumanEval 代码生成基准（Pass@1 指标

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

Qwen3-27B 在 BF16 精度下，使用 llama.cpp 框架（AVX2 加速，F16 精度）在 HumanEval 代码生成基准（Pass@1 指标）中的确切得分，用于对比 vLLM 与 llama.cpp 在代码生成任务上的性能一致性。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，使用 llama.cpp 框架（AVX2 加速，F16 精度）在 HumanEval 代码生成基准（Pass@1 指标）中取得了特定得分，该得分可用于对比 vLLM 与 llama.cpp 在代码生成任务上的性能一致性，但具体数值需查阅官方基准测试报告或可靠第三方评测数据以确认。

## Evidence

[质询]该陈述包含具体的经验性数值（确切得分），属于经验事实，无法从第一性原理推导；且检索无可用来源，无法验证具体数值是否准确或是否存在口径混淆（如不同量化版本、不同采样参数导致的分数波动）。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值）

## Search Query

Qwen3-27B llama.cpp HumanEval Pass@1 benchmark
