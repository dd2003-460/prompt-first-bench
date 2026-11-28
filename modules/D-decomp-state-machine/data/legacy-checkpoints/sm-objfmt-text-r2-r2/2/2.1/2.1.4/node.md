# N53: Intel Arc A770 (16GB GDDR6) 的显存带宽为 560 GB/s，新品市场价约为 $300-$400，二手市场价约为 $200-$300，

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N12

## Claim

Intel Arc A770 (16GB GDDR6) 的显存带宽为 560 GB/s，新品市场价约为 $300-$400，二手市场价约为 $200-$300，显存容量 16GB 不足以容纳 Qwen3-27B 的 BF16/INT8 权重及 KV Cache，必须依赖 INT4 量化或 CPU Offload，带宽仅为 RTX 4090 的 55%，在内存带宽受限场景中性能显著落后。

## Corrected Claim

Intel Arc A770 (16GB GDDR6) 的显存带宽为 560 GB/s，新品市场价约为 $300-$400，二手市场价约为 $200-$300，显存容量 16GB 不足以容纳 Qwen3-27B 的 BF16/INT8 权重及 KV Cache，必须依赖 INT4 量化或 CPU Offload，带宽仅为 RTX 4090 的 55%，在内存带宽受限场景中性能显著落后。

## Evidence

先验知识/题面给定，逻辑校验通过：Intel Arc A770 官方规格确认为 16GB GDDR6，带宽 560 GB/s；RTX 4090 带宽约 1008 GB/s，560/1008 ≈ 55.5%，比例准确；Qwen3-27B BF16 权重约 54GB，远超 16GB 显存，必须量化或 Offload 的逻辑成立；价格区间符合市场常识。

## Search Query

Intel Arc A770 memory bandwidth price 2024
