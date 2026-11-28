# N54: NVIDIA A100 (80GB HBM2e) 的显存带宽为 2039 GB/s，单卡购买成本约为 $15,000-$20,000，租赁成本约为 $3.5-$

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

NVIDIA A100 (80GB HBM2e) 的显存带宽为 2039 GB/s，单卡购买成本约为 $15,000-$20,000，租赁成本约为 $3.5-$4.5/hour，显存容量 80GB 足以容纳 Qwen3-27B 的 BF16 权重 (55.6GB) 和 KV Cache (13.7GB) 的组合，无需量化即可完整加载，带宽为 RTX 4090 的 2 倍。

## Corrected Claim

NVIDIA A100 (80GB HBM2e) 的显存带宽为 2039 GB/s，单卡购买成本约为 $15,000-$20,000，租赁成本约为 $3.5-$4.5/hour，显存容量 80GB 足以容纳 Qwen3-27B 的 BF16 权重 (55.6GB) 和 KV Cache (13.7GB) 的组合，无需量化即可完整加载，带宽为 RTX 4090 的 2 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：A100 80GB HBM2e 带宽确为 ~2039 GB/s，RTX 4090 带宽约 1008 GB/s，前者约为后者 2 倍；80GB 显存足以容纳 55.6GB 权重 + 13.7GB KV Cache（共 69.3GB），无需量化；价格区间符合市场常识。

## Search Query

NVIDIA A100 80GB HBM2e memory bandwidth price 2024
