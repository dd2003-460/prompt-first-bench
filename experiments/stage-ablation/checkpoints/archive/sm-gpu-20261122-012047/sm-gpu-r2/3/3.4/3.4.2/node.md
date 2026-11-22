# N104: 困惑度（Perplexity）与下游任务准确率（如 MMLU、HumanEval）并非线性相关：困惑度增加 10% 不一定导致任务准确率下降 10%。对于 Qw

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

困惑度（Perplexity）与下游任务准确率（如 MMLU、HumanEval）并非线性相关：困惑度增加 10% 不一定导致任务准确率下降 10%。对于 Qwen3-27B，INT4 量化导致的困惑度增加 ~10% 通常对应 MMLU 准确率下降 1-3 个百分点，HumanEval 通过率下降 2-5 个百分点，需通过具体任务基准验证质量损失是否可接受。

## Corrected Claim

困惑度（Perplexity）与下游任务准确率（如 MMLU、HumanEval）并非线性相关：困惑度增加 10% 不一定导致任务准确率下降 10%。对于 Qwen3-27B，INT4 量化导致的困惑度增加 ~10% 通常对应 MMLU 准确率下降 1-3 个百分点，HumanEval 通过率下降 2-5 个百分点，需通过具体任务基准验证质量损失是否可接受。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

perplexity vs task accuracy correlation LLM quantization
