# N279: Qwen3-27B 在 FP8 (E4M3) 量化下，HumanEval/MBPP 代码生成基准的 Pass@1 准确率下降幅度（绝对值百分点），需对比 BF1

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N98, N99, N100

## Claim

Qwen3-27B 在 FP8 (E4M3) 量化下，HumanEval/MBPP 代码生成基准的 Pass@1 准确率下降幅度（绝对值百分点），需对比 BF16 基线

## Corrected Claim

Qwen3-27B 在 FP8 (E4M3) 量化下，HumanEval/MBPP 代码生成基准的 Pass@1 准确率相较于 BF16 基线存在一定程度的下降，具体幅度需查阅官方技术报告或基准测试数据。

## Evidence

[质询]具体数值缺失且来源不可用，无法验证具体的百分点下降幅度，属于经验事实且缺乏直接证据支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B FP8 quantization HumanEval Pass@1 accuracy drop
