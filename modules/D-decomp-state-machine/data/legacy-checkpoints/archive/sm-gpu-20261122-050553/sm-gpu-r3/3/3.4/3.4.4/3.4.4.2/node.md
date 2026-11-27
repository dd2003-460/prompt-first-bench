# N232: Qwen3-27B W4 量化（AWQ）在 HumanEval 基准上的 Pass@1 实测值 (Pass@1_W4) 为 [待核验]，需查找针对 Qwen3 

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N74

## Claim

Qwen3-27B W4 量化（AWQ）在 HumanEval 基准上的 Pass@1 实测值 (Pass@1_W4) 为 [待核验]，需查找针对 Qwen3 系列 W4 量化的代码生成能力评测数据；若官方未提供，需基于 Qwen2.5-32B 或类似规模模型的 W4 量化退化比例（通常 3-5% 绝对值下降）进行保守估计。

## Corrected Claim

Qwen3-27B W4 量化（AWQ）在 HumanEval 基准上的 Pass@1 实测值暂无公开权威数据；参考同规模模型（如 Qwen2.5-32B）W4 量化通常带来的 3-5% 绝对值性能退化，可保守估计其 Pass@1 较 FP16 版本下降约 3-5 个百分点。

## Evidence

[质询]该陈述包含具体的经验性数值（Qwen3-27B W4 AWQ 在 HumanEval 上的 Pass@1 实测值或基于 Qwen2.5-32B 的退化估计），属于硬件/模型性能经验事实，无法从第一性原理推导，且检索无可用来源支持具体数值。 | 经验事实，逻辑自洽但缺来源支持（检索失败，无外部证据）

## Search Query

Qwen3-27B W4 quantization HumanEval Pass@1 score
