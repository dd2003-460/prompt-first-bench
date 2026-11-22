# N79: 消费级 GPU 能效比对比：RTX 4090 (1008 GB/s / 450W = 2.24 GB/s/W) vs RTX 3090 (936 GB/s / 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

消费级 GPU 能效比对比：RTX 4090 (1008 GB/s / 450W = 2.24 GB/s/W) vs RTX 3090 (936 GB/s / 350W = 2.67 GB/s/W)，3090 在每瓦特显存带宽上优于 4090，适合长时间低负载推理场景。

## Corrected Claim

消费级 GPU 能效比对比：RTX 4090 (1008 GB/s / 450W = 2.24 GB/s/W) vs RTX 3090 (936 GB/s / 350W = 2.67 GB/s/W)，3090 在每瓦特显存带宽上优于 4090，适合长时间低负载推理场景。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 显存带宽 1008 GB/s，TDP 450W，计算得 2.24 GB/s/W；RTX 3090 显存带宽 936 GB/s，TDP 350W，计算得 2.67 GB/s/W。数值量级符合硬件规格常识，逻辑自洽。

## Search Query

RTX 4090 vs RTX 3090 power efficiency memory bandwidth per watt
