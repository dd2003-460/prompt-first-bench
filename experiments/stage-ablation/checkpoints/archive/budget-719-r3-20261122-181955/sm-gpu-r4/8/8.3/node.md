# N119: 量化损失可接受阈值：MMLU 下降 < 2% 且 HumanEval 下降 < 3% 视为可接受；若任一指标下降 > 5%，则需回退到 BF16/FP8 或采用

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N35

## Claim

量化损失可接受阈值：MMLU 下降 < 2% 且 HumanEval 下降 < 3% 视为可接受；若任一指标下降 > 5%，则需回退到 BF16/FP8 或采用混合精度策略；该阈值基于 LLM 应用对任务准确率的典型业务要求（如代码助手、问答系统）设定。

## Corrected Claim

量化损失可接受阈值：MMLU 下降 < 2% 且 HumanEval 下降 < 3% 视为可接受；若任一指标下降 > 5%，则需回退到 BF16/FP8 或采用混合精度策略；该阈值基于 LLM 应用对任务准确率的典型业务要求（如代码助手、问答系统）设定。

## Evidence

先验知识/题面给定，逻辑校验通过
