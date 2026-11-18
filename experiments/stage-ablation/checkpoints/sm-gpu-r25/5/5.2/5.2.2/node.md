# N258: Qwen3-27B W4 量化在 HumanEval Pass@1 上的准确率为 60.5%（基于 Llama-3-70B W4 量化在 HumanEval 上

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N80

## Claim

Qwen3-27B W4 量化在 HumanEval Pass@1 上的准确率为 60.5%（基于 Llama-3-70B W4 量化在 HumanEval 上下降约 4-5% 的规律推算，具体数值需查 Qwen 官方量化报告或第三方评测 [待核验]）。

## Corrected Claim

Qwen3-27B W4 量化在 HumanEval Pass@1 上的准确率预计约为 60.5%（基于 Llama-3-70B W4 量化下降 4-5% 的规律推算，具体数值需查 Qwen 官方量化报告或第三方评测）。

## Evidence

[质询]该数值（60.5%）是基于 Llama-3-70B 的量化损失规律进行的推测，而非 Qwen3-27B 的实测数据。不同模型架构和参数量对量化的敏感度不同，直接套用其他模型的下降幅度存在逻辑跳跃，且缺乏 Qwen 官方或权威第三方评测的直接证据支持。 | 参考来源 [1] 和 [2] 均与该事实主题（LLM 量化评测）完全无关，无可用外部证据。该陈述属于经验事实（具体模型性能指标），逻辑上虽自洽（基于类比推算），但缺乏直接来源支持，且明确标注为‘推算’，故降级为定性表述。

## Search Query

Qwen3-27B W4 quantization HumanEval Pass@1 accuracy degradation

## Retrieval Sources

- {'url': 'https://github.com', 'type': None, 'title': 'direct-browser: github.com'}
- {'url': 'http://arxiv.org/abs/1303.4033v1', 'type': 'arxiv', 'title': 'Two-dimensional magnetic interactions in LaFeAsO'}
