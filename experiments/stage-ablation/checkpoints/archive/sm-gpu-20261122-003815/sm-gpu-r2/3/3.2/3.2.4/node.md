# N113: Qwen3-27B 在 INT4 (AWQ/GPTQ) 精度下的基准测试分数：MMLU, GSM8K, HumanEval 的具体数值，特别关注代码生成任务 (

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

Qwen3-27B 在 INT4 (AWQ/GPTQ) 精度下的基准测试分数：MMLU, GSM8K, HumanEval 的具体数值，特别关注代码生成任务 (HumanEval) 的分数下降幅度是否显著大于通用任务

## Corrected Claim

Qwen3-27B 在 INT4 (AWQ/GPTQ) 精度下存在量化模型（如GPTQ-Int4），但具体基准测试分数（MMLU, GSM8K, HumanEval）及代码生成任务分数下降幅度需查阅具体评测报告，当前来源未提供。

## Evidence

[质询]参考来源[1]仅提供了量化模型的元数据（如硬件环境、vLLM版本、上下文长度），完全缺失MMLU、GSM8K、HumanEval的具体基准测试分数，无法验证具体数值及代码生成任务分数下降幅度是否显著大于通用任务这一核心事实。 | 来源[1]与主题相关（均为Qwen3-27B INT4量化），但仅间接支持模型存在，未提供具体基准分数，属于经验事实且缺直接来源支持。

## Search Query

Qwen3-27B INT4 AWQ GPTQ benchmark scores MMLU GSM8K HumanEval

## Retrieval Sources

- {'url': 'https://huggingface.co/bernhardbrieger/Qwen3.8-27B-GPTQ-Int4&rut=073e6eb638494d5c6fd5bbe62d0fbf9bc5f2b9be8cb50368e62f0a04c5af08cb', 'type': 'ddg', 'title': 'bernhardbrieger/Qwen3.8-27B-GPTQ-Int4 · Hugging Face'}
