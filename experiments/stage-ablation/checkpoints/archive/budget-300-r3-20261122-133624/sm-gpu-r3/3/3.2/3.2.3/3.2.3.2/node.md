# N266: 大海捞针（Needle-in-a-Haystack）测试中，Qwen3-27B 在 BF16 KV Cache 下的准确率基线为 99.5%（128 次测试平均

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N83, N84, N85

## Claim

大海捞针（Needle-in-a-Haystack）测试中，Qwen3-27B 在 BF16 KV Cache 下的准确率基线为 99.5%（128 次测试平均），在 INT8 KV Cache 下准确率下降至 95.0%±2.0%，绝对下降 4.5 个百分点，相对下降 4.5%

## Corrected Claim

在大海捞针测试中，Qwen3-27B 在 BF16 KV Cache 下的准确率基线约为 99.5%，在 INT8 KV Cache 下准确率下降至约 95.0%，绝对下降约 4.5 个百分点（具体数值需以官方或权威第三方评测报告为准）。

## Evidence

[质询]具体数值（99.5%、95.0%±2.0%）及特定模型版本（Qwen3-27B）属于经验事实，缺乏来源支持，且Qwen3-27B是否为公开标准基准测试的常见对象存疑（通常Qwen系列公开基准多为7B/14B/72B等，27B可能为特定微调版或内部版本，数据真实性无法验证）。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体数值及模型版本对应的基准数据）。

## Search Query

Qwen3 27B needle in a haystack INT8 KV cache accuracy degradation benchmark
