# N217: RTX 4090 (24GB) 在 W4 精度下的理论吞吐量上限计算：吞吐量 = 1008 GB/s / (13.5GB 权重 + 5.2GB KV + 2.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N100

## Claim

RTX 4090 (24GB) 在 W4 精度下的理论吞吐量上限计算：吞吐量 = 1008 GB/s / (13.5GB 权重 + 5.2GB KV + 2.5GB 激活) ≈ 47.5 tokens/s，此值假设计算单元不成为瓶颈且显存带宽利用率达 100%。

## Corrected Claim

RTX 4090 (24GB) 在 W4 精度下的理论吞吐量上限计算：吞吐量 = 1008 GB/s / (13.5GB 权重 + 5.2GB KV + 2.5GB 激活) ≈ 47.5 tokens/s，此值假设计算单元不成为瓶颈且显存带宽利用率达 100%。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽约 1008 GB/s，总数据量 21.2 GB，计算 1008/21.2 ≈ 47.55，数值与逻辑自洽。
