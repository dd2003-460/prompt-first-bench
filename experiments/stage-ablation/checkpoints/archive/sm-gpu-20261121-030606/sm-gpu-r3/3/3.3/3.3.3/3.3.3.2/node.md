# N270: HumanEval基准测试的代码生成质量评估需区分：Pass@1（单次生成通过）与Pass@10（多次生成至少一次通过）；INT8量化对Pass@1的影响通常大

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N116

## Claim

HumanEval基准测试的代码生成质量评估需区分：Pass@1（单次生成通过）与Pass@10（多次生成至少一次通过）；INT8量化对Pass@1的影响通常大于Pass@10，需确认N116中-2.4%对应的具体指标

## Corrected Claim

HumanEval基准测试的代码生成质量评估需区分：Pass@1（单次生成通过）与Pass@10（多次生成至少一次通过）；INT8量化对Pass@1的影响通常大于Pass@10，需确认N116中-2.4%对应的具体指标

## Evidence

先验知识/题面给定，逻辑校验通过：Pass@1衡量单次生成能力，对量化误差更敏感；Pass@10通过多次采样增加容错率，因此量化对Pass@1的负面影响通常大于Pass@10，符合代码生成评估的基本逻辑。

## Search Query

HumanEval Pass@1 vs Pass@10 LLM code generation quantization impact
