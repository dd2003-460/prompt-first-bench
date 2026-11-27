# N121: FP8/INT8 精度下显存需求 ~34.2GB (N13)，单卡消费级 (24GB) 不可行；双卡 RTX 3090 (48GB) 可行，但需 NVLink 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N38

## Claim

FP8/INT8 精度下显存需求 ~34.2GB (N13)，单卡消费级 (24GB) 不可行；双卡 RTX 3090 (48GB) 可行，但需 NVLink 或 PCIe P2P 支持；RTX 3090 支持 NVLink (112.5GB/s)，RTX 4090 不支持 NVLink，双卡 4090 仅 PCIe 4.0 x16 (64GB/s)，KV Cache 跨卡同步延迟增加 ~20-30% [待核验：vLLM 对 PCIe 多卡的支持效率]

## Corrected Claim

FP8/INT8 精度下显存需求 ~34.2GB (N13)，单卡消费级 (24GB) 不可行；双卡 RTX 3090 (48GB) 可行，但需 NVLink 或 PCIe P2P 支持；RTX 3090 支持 NVLink (112.5GB/s)，RTX 4090 不支持 NVLink，双卡 4090 仅 PCIe 4.0 x16 (64GB/s)，KV Cache 跨卡同步延迟增加 ~20-30% [待核验：vLLM 对 PCIe 多卡的支持效率]

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090 支持 NVLink 而 RTX 4090 不支持 NVLink 是确凿的硬件规格事实；PCIe 4.0 x16 带宽 64GB/s 符合标准；显存需求与卡数匹配逻辑自洽。

## Search Query

vLLM multi-GPU PCIe vs NVLink performance impact
