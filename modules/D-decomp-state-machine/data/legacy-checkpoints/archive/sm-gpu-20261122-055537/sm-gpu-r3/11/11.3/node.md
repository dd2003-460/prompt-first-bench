# N119: 单卡RTX 4090在Qwen3-27B BF16下因显存不足（需54GB+KV Cache > 24GB）无法独立运行，必须依赖CPU Offload或模型分

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N35

## Claim

单卡RTX 4090在Qwen3-27B BF16下因显存不足（需54GB+KV Cache > 24GB）无法独立运行，必须依赖CPU Offload或模型分片；其有效计算带宽受限于PCIe带宽（~32 GB/s）而非显存带宽（~1000 GB/s），导致吞吐量极低（<10 tokens/s）。

## Corrected Claim

单卡RTX 4090在Qwen3-27B BF16下因显存不足（需54GB+KV Cache > 24GB）无法独立运行，必须依赖CPU Offload或模型分片；其有效计算带宽受限于PCIe带宽（~32 GB/s）而非显存带宽（~1000 GB/s），导致吞吐量显著低于纯GPU推理场景。

## Evidence

[质询]吞吐量数值（<10 tokens/s）缺乏具体上下文（如序列长度、Batch Size、是否启用量化或特定推理引擎），且PCIe带宽限制下的实际吞吐受多种因素影响，该具体数值可能因配置不同而有较大波动，存在过度具体化的风险。 | 先验知识/题面给定，逻辑校验通过：Qwen3-27B BF16权重约54GB，超过RTX 4090 24GB显存，必须Offload；Offload模式下瓶颈确为PCIe带宽，导致吞吐显著低于纯GPU推理，定性结论正确，但具体数值<10 tokens/s为经验估计，无来源直接支持。

## Search Query

RTX 4090 offload 27B model inference speed penalty
