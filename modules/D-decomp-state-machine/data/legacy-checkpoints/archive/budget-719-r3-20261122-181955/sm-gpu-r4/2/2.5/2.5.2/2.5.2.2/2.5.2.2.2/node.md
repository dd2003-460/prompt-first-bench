# N757: Qwen3-27B FP8 (E4M3) 量化版本在 HumanEval (Pass@1) 评测中的准确率为 64.3%（来源：第三方代码评测平台如 CodeB

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N269

## Claim

Qwen3-27B FP8 (E4M3) 量化版本在 HumanEval (Pass@1) 评测中的准确率为 64.3%（来源：第三方代码评测平台如 CodeBench 或 HuggingFace 社区提交数据，代码生成对量化敏感，通常损失略高于通用知识基准 [待核验]）。

## Corrected Claim

Qwen3-27B FP8 (E4M3) 量化版本在 HumanEval (Pass@1) 评测中的准确率约为 64% 左右（具体数值因量化方法和评测环境而异，通常较 BF16 版本有轻微损失）。

## Evidence

[质询]具体数值 64.3% 缺乏权威来源支持，且不同量化实现（如 SmoothQuant, GPTQ, AWQ）及评测环境（vLLM, TGI）可能导致结果波动，该精确数值可能来自特定社区提交而非官方基准，存在以偏概全或数据陈旧的风险。 | 经验事实，逻辑自洽（FP8量化通常导致代码生成能力轻微下降，64.3%在合理范围内），但本轮检索无可用来源，无法提供直接支持，依据经验事实排除条款降级。

## Search Query

Qwen3-27B FP8 HumanEval Pass@1
