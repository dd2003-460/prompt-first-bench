# N182: FP8 量化在代码生成任务 (HumanEval) 上的准确率下降机制：代码生成对语法结构和逻辑一致性敏感，FP8 的较低动态范围 (E4M3/E5M2) 可能

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N54

## Claim

FP8 量化在代码生成任务 (HumanEval) 上的准确率下降机制：代码生成对语法结构和逻辑一致性敏感，FP8 的较低动态范围 (E4M3/E5M2) 可能导致 Logits 分布中的微小偏移被放大，造成关键 Token (如分号、括号) 概率排名错误；实测数据显示，对于 7B-70B 模型，FP8 在 HumanEval Pass@1 上的下降通常为 1-3%，高于 MMLU 的 0.5-1%，但若使用 Per-Channel Scaling 可缩小至 <1%。

## Corrected Claim

FP8 量化在代码生成任务 (HumanEval) 上的准确率通常会有所下降，且往往高于通用知识任务 (如 MMLU) 的下降幅度，具体数值取决于模型规模与量化策略。

## Evidence

[质询]具体数值区间（1-3% vs 0.5-1%）及Per-Channel Scaling的效果缺乏通用性，高度依赖具体模型架构、量化实现细节及评测基准版本，属于经验事实而非普适规律。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

FP8 quantization impact on HumanEval code generation accuracy Llama Qwen
