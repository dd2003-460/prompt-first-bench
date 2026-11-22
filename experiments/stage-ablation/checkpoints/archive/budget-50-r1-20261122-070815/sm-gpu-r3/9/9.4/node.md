# N144: Qwen3-27B 在 AWQ INT4 量化下 GSM8K 基准测试的具体得分及相对于 BF16 的相对下降百分比（验证 N33 中 2-5% 的说法，并区分

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N33

## Claim

Qwen3-27B 在 AWQ INT4 量化下 GSM8K 基准测试的具体得分及相对于 BF16 的相对下降百分比（验证 N33 中 2-5% 的说法，并区分 Pass@1 与 Pass@k 口径）

## Corrected Claim

Qwen3-27B 在 AWQ INT4 量化下的 GSM8K 基准测试得分及相对于 BF16 的相对下降百分比需参考具体评测报告，现有来源仅确认了使用 lm-evaluation-harness 及 Recovery % 的计算口径，未提供具体数值以验证 2-5% 的说法。

## Evidence

[质询]参考来源仅提供了计算相对下降百分比的方法论（Recovery % = quantized / BF16-base）和测试工具（lm-evaluation-harness），但摘要中未包含具体的 GSM8K 得分数值或具体的相对下降百分比数值，无法直接验证 N33 中 '2-5%' 的具体说法。 | 来源 [1] 间接支持了测试方法论和指标定义（Recovery % 计算方式），但未提供具体数值，属于间接支持；经验事实（具体得分和百分比）缺乏直接来源支持，故降级。

## Search Query

Qwen3-27B AWQ INT4 GSM8K score degradation percentage

## Retrieval Sources

- {'url': 'https://huggingface.co/amd/Qwen3.8-27B-Quark-AWQ-INT4-W4A16/blob/main/README.md&rut=9d23e5b4cb0584ff08060806bf7514fd8f5ea9951ced47570aa679754f7e9e08', 'type': 'ddg', 'title': 'README.md · amd/Qwen3.8-27B-Quark-AWQ-INT4-W4A16 at main - Hugging Face'}
