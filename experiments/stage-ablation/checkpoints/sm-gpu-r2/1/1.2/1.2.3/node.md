# N35: 多卡消费级组合方案拓扑：2x RTX 5090 (64GB 总显存) 通过 PCIe 4.0 互联，有效带宽受限。若采用 Tensor Parallelism 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N7

## Claim

多卡消费级组合方案拓扑：2x RTX 5090 (64GB 总显存) 通过 PCIe 4.0 互联，有效带宽受限。若采用 Tensor Parallelism (TP=2)，每卡承担 18.1GB (FP8) 或 31.9GB (BF16) 权重+KV，均低于单卡 32GB 上限，故 2x5090 可支持 BF16 全精度推理，无需量化损失。

## Corrected Claim

2x RTX 5090 (64GB 总显存) 通过 PCIe 4.0 互联，若采用 Tensor Parallelism (TP=2)，每卡承担约 18.1GB (FP8) 或 31.9GB (BF16) 权重+KV。BF16 模式下显存占用接近上限，需严格控制 KV Cache 大小或预留系统开销，否则可能面临显存溢出风险；FP8 模式则有较大余量。

## Evidence

[质询]数值量级与硬件规格存在潜在矛盾：RTX 5090 单卡显存通常为 32GB，2卡总显存 64GB。若模型权重+KV 在 BF16 下每卡需 31.9GB，则总需求为 63.8GB，几乎占满 64GB 总显存，未预留任何系统开销、激活值或通信缓冲区空间，实际部署中极易 OOM（显存溢出）。此外，'无需量化损失'的结论过于绝对，忽略了 KV Cache 动态增长可能导致的显存压力。 | 先验知识/题面给定，逻辑校验通过但存在工程可行性风险（显存余量不足），故降级为定性表述。

## Search Query

2x RTX 5090 tensor parallelism LLM inference memory split
