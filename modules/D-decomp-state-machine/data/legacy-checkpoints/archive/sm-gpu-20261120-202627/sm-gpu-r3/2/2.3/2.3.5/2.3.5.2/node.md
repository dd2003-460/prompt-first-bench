# N232: W4A16 量化下 Qwen3-27B 在短上下文（<4K）的困惑度增加具体数值需检索 vLLM 社区基准测试或 HuggingFace 量化模型卡片中的 MM

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N59

## Claim

W4A16 量化下 Qwen3-27B 在短上下文（<4K）的困惑度增加具体数值需检索 vLLM 社区基准测试或 HuggingFace 量化模型卡片中的 MMLU/GSM8K 准确率下降反推的困惑度增量，以验证其是否显著高于 INT8 且低于 W3

## Corrected Claim

W4A16 量化下 Qwen3-27B 在短上下文（<4K）的困惑度增加具体数值需直接检索 vLLM 社区基准测试或 HuggingFace 量化模型卡片中报告的 Perplexity 指标，以验证其是否显著高于 INT8 且低于 W3；不能通过 MMLU/GSM8K 准确率下降反推困惑度增量。

## Evidence

[质询]该陈述试图通过MMLU/GSM8K准确率下降来反推困惑度（Perplexity）增量，这在方法论上存在严重缺陷。困惑度是语言模型在特定语料上的平均负对数似然，而MMLU/GSM8K是特定领域的问答/推理基准，两者之间没有直接的数学换算关系。准确率下降不能直接‘反推’出困惑度的具体数值增量，这种推导逻辑不成立。 | 逻辑校验失败：MMLU/GSM8K准确率与困惑度（Perplexity）无直接换算关系，无法通过前者反推后者的具体数值增量；且本轮检索无可用来源支持该具体数值或推导方法。

## Search Query

vLLM W4A16 Qwen3-27B perplexity degradation vs INT8 W3 benchmark
