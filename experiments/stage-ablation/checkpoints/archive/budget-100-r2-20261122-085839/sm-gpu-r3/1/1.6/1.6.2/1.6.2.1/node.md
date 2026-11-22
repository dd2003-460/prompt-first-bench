# N157: Qwen3-27B 在 BF16 精度下，使用 vLLM 框架（默认解码参数）在 HumanEval 代码生成基准（Pass@1 指标）中的确切得分，需检索 Q

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N45

## Claim

Qwen3-27B 在 BF16 精度下，使用 vLLM 框架（默认解码参数）在 HumanEval 代码生成基准（Pass@1 指标）中的确切得分，需检索 Qwen3 官方技术报告或第三方评测平台（如 OpenCompass）数据。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，使用 vLLM 框架在 HumanEval 代码生成基准（Pass@1 指标）中的得分需参考 Qwen3 官方技术报告或第三方评测平台（如 OpenCompass）的具体数据，不同解码参数设置可能导致结果差异。

## Evidence

[质询]该陈述要求提供‘确切得分’，但缺乏具体来源支持，且不同评测环境（如温度、top_p等默认参数差异）可能导致数值波动，无法从第一性原理推出具体经验数值。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

Qwen3-27B HumanEval Pass@1 score BF16 technical report
