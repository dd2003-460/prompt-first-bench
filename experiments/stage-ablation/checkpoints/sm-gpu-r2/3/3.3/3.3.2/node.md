# N77: Qwen3-27B 在 INT8 量化下的困惑度增加量为 1.0-2.5%，在代码生成任务 (如 HumanEval Pass@1) 上，准确率下降 1-3 个

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 在 INT8 量化下的困惑度增加量为 1.0-2.5%，在代码生成任务 (如 HumanEval Pass@1) 上，准确率下降 1-3 个百分点 [待核验具体数值需查量化基准测试]。

## Corrected Claim

Qwen3-27B 在 INT8 量化下通常会出现轻微的困惑度增加和代码生成任务准确率下降，具体数值需查阅官方量化基准测试报告。

## Evidence

[质询]具体数值（1.0-2.5%困惑度增加，1-3个百分点准确率下降）属于特定模型在特定量化方案下的经验测量结果，无法从第一性原理推导，且缺乏来源支持具体数值的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

Qwen3-27B INT8 quantization HumanEval accuracy drop
