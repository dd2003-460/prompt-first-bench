# N91: INT8 工作点下 A6000 的实际推理吞吐修正值：理论带宽上限 26.3 tokens/s，A6000 的 INT8 Tensor Core 利用率较低，实

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

INT8 工作点下 A6000 的实际推理吞吐修正值：理论带宽上限 26.3 tokens/s，A6000 的 INT8 Tensor Core 利用率较低，实测吞吐通常为理论值的 60-70%，即 15.8-18.4 tokens/s；A6000 的 48GB 显存允许单卡部署 BF16，但在 INT8 下显存冗余大，适合需要更高精度或更长上下文的场景。

## Corrected Claim

A6000 在 INT8 工作点下的实际推理吞吐受模型规模、Batch Size 及序列长度影响显著，通常低于理论带宽上限；其 48GB 显存允许单卡部署 BF16 大模型，INT8 下显存冗余较大，适合高精度或长上下文场景。

## Evidence

[质询]具体数值（26.3 tokens/s 理论上限及 60-70% 利用率）缺乏来源直接支持，且不同模型规模下吞吐差异巨大，该数值可能仅针对特定小模型或特定配置，不具备普适性；此外，A6000 的 INT8 Tensor Core 利用率受 batch size 和序列长度影响极大，笼统断言 60-70% 缺乏严谨性。 | 来源 [1] 和 [2] 仅确认了 A6000 支持混合精度推理及 vLLM 优化，未提供具体的 INT8 理论带宽上限或实测吞吐数值，属于经验事实且缺来源直接支持。

## Search Query

A6000 48GB Qwen 27B INT8 inference throughput tokens per second measured

## Retrieval Sources

- {'url': 'https://github.com/321176aaaaaA/qwen38-27b-dspark-hybrid-inference-a6000/tree/main&rut=bd5538318b339754921e23b5eca59405b533c1f719ad8e48aef0baff70e1d163', 'type': 'ddg', 'title': 'Qwen3.8-27B DSpark — Hybrid-Precision Inference on A6000'}
- {'url': 'https://github.com/321176aaaaaA/qwen38-27b-dspark-hybrid-inference-a6000/blob/main/README.md&rut=9e48dab9fec13379029fb8b4f2e16f843b7eb2aadd749c112f7d4ebc3f8b928f', 'type': 'ddg', 'title': 'qwen38-27b-dspark-hybrid-inference-a6000/README.md at main ... - GitHub'}
