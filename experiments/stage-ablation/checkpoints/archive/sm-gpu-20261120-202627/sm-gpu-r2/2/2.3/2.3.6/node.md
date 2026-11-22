# N60: 在 32K 长上下文场景下，NVFP4/W4 量化 Qwen3-27B 的累积误差导致困惑度增加幅度比短上下文额外增加 0.5% - 1.0% 个百分点，主要源

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N13, N14, N15

## Claim

在 32K 长上下文场景下，NVFP4/W4 量化 Qwen3-27B 的累积误差导致困惑度增加幅度比短上下文额外增加 0.5% - 1.0% 个百分点，主要源于 KV Cache 量化误差在长序列中的累积效应 [待核验：需长文本基准测试数据]

## Corrected Claim

在 32K 长上下文场景下，NVFP4/W4 量化 Qwen3-27B 的累积误差导致困惑度增加，主要源于 KV Cache 量化误差在长序列中的累积效应，具体幅度需长文本基准测试数据验证。

## Evidence

[质询]具体数值（0.5%-1.0%）缺乏来源支持，且来源[2]提到的±0.5精度差距可能指代不同指标（如MMLU分数而非困惑度百分点），存在口径混淆风险。 | 经验事实，逻辑自洽但缺来源支持；来源[2]仅提及精度差距在±0.5内，未明确为长上下文下的困惑度增加幅度。

## Search Query

Qwen3-27B W4 quantization long context 32K perplexity cumulative error

## Retrieval Sources

- {'url': 'https://blog.csdn.net/gitblog_01106/article/details/168111467&rut=066e2ce04f477f0d2129366936f36896bdbfab8a59f38de5acbb6cc067213d32', 'type': 'ddg', 'title': 'Qwen3.8-27B-NVFP4完整指南：4位NVFP4量化如何玩转27B多模态大模型-CSDN博客'}
- {'url': 'https://devpress.csdn.net/v1/article/detail/162604876&rut=ce986b437346723395d5fede77531458e5cfcc2fbcd05d48661b83dc8050cb57', 'type': 'ddg', 'title': 'Qwen3.6-27B-NVFP4 深度评测：英伟达官方量化，27B 长上下文本地部署新选择'}
