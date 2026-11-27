# N156: Qwen3-27B 在 BF16 精度下，使用 llama.cpp 框架（AVX2 加速，量化精度为 F16，解码参数同上）在 MMLU 5-shot 评测中的

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N44

## Claim

Qwen3-27B 在 BF16 精度下，使用 llama.cpp 框架（AVX2 加速，量化精度为 F16，解码参数同上）在 MMLU 5-shot 评测中的确切得分，用于验证推理框架对基准分数的影响幅度（预期偏差 <0.5%）。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，使用 llama.cpp 框架（AVX2 加速，量化精度为 F16）在 MMLU 5-shot 评测中的得分与标准基准存在微小偏差（预期 <0.5%），具体确切得分需查阅官方基准报告或实测数据。

## Evidence

[质询]该陈述包含具体的经验性数值（MMLU 5-shot 确切得分），属于经验事实，无法从第一性原理推导，且缺乏任何来源支持其具体数值或偏差幅度的断言。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）。

## Search Query

Qwen3-27B llama.cpp MMLU benchmark score F16
