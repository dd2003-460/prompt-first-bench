# N118: 质量损失阈值 ΔQ 的量化定义：对于通用对话任务，Perplexity 增加 ΔPPL < 0.5 或 MMLU 得分下降 ΔMMLU < 2 个百分点视为可接

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27

## Claim

质量损失阈值 ΔQ 的量化定义：对于通用对话任务，Perplexity 增加 ΔPPL < 0.5 或 MMLU 得分下降 ΔMMLU < 2 个百分点视为可接受；对于代码生成任务，HumanEval Pass@1 下降 ΔHE < 5 个百分点视为可接受。

## Corrected Claim

在缺乏统一行业标准的情况下，质量损失阈值 ΔQ 通常需根据具体业务场景设定；在通用对话任务中，Perplexity 增加 < 0.5 或 MMLU 下降 < 2 个百分点常被用作参考基准；在代码生成任务中，HumanEval Pass@1 下降 < 5 个百分点常被视为可接受范围，但具体阈值应结合下游任务敏感度调整。

## Evidence

[质询]这些具体的数值阈值（ΔPPL < 0.5, ΔMMLU < 2, ΔHE < 5）属于经验性工程参数，缺乏统一的行业标准或第一性原理推导基础，不同研究或应用场景下的容忍度可能差异巨大，存在将特定实验结果泛化为通用标准的风险。 | 经验事实，逻辑自洽但缺来源支持
