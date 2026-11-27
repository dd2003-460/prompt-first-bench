# N246: 针对‘代码生成’任务，质量损失可接受性的量化阈值为：HumanEval Pass@1 下降 < 1.0% 或 Perplexity 增加 < 2.0%；若 IN

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N71, N72, N74

## Claim

针对‘代码生成’任务，质量损失可接受性的量化阈值为：HumanEval Pass@1 下降 < 1.0% 或 Perplexity 增加 < 2.0%；若 INT4 量化导致 HumanEval 下降 1.5%，则判定为不可接受，需回退至 INT8 或混合精度

## Corrected Claim

针对‘代码生成’任务，质量损失可接受性通常需根据具体业务场景设定量化阈值（例如 HumanEval Pass@1 下降 < 1.0% 或 Perplexity 增加 < 2.0%）；若 INT4 量化导致 HumanEval 下降 1.5% 且超过预设阈值，则判定为不可接受，需回退至 INT8 或混合精度。

## Evidence

[质询]该陈述中的具体量化阈值（HumanEval Pass@1 下降 < 1.0% 或 Perplexity 增加 < 2.0%）属于经验性工程标准，并非由第一性原理或数学公理严格推导出的普适真理，且不同研究或应用场景下对‘可接受性’的定义可能存在差异，缺乏统一的行业标准支持该特定数值组合。 | 先验知识/题面给定，逻辑校验通过（内部逻辑自洽：1.5% > 1.0% 故判定不可接受），但具体阈值数值属于经验事实，无外部来源直接支持，依据经验事实排除条款降级。

## Search Query

LLM quantization code generation HumanEval pass@1 threshold acceptable degradation
