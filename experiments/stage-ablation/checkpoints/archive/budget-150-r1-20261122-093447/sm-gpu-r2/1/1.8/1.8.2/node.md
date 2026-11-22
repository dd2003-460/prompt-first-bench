# N66: RTX 3090/3090 Ti (24GB, 936-1008GB/s, 350-450W, ~$1500-1800 used) 为 BF16/FP8 双卡方

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N14

## Claim

RTX 3090/3090 Ti (24GB, 936-1008GB/s, 350-450W, ~$1500-1800 used) 为 BF16/FP8 双卡方案的基础单元，其二手价格优势使得 2x3090 (48GB) 的硬件成本 (~$3000-3600) 低于单张 L40S (48GB, ~$8000+)，但需验证 PCIe 互联对 KV Cache 分片的影响

## Corrected Claim

RTX 3090/3090 Ti (24GB, 936-1008GB/s, 350-450W, ~$1500-1800 used) 为 BF16/FP8 双卡方案的基础单元，其二手价格优势使得 2x3090 (48GB) 的硬件成本 (~$3000-3600) 低于单张 L40S (48GB, ~$8000+)，但需验证 PCIe 互联对 KV Cache 分片的影响

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 3090/3090 Ti 的显存容量（24GB）、带宽（~936GB/s）、功耗（350-450W）及二手市场价格区间（~$1500-1800）符合市场常识与硬件规格；2x3090 总显存 48GB 且成本低于单张 L40S（~$8000+）的逻辑推导自洽；PCIe 互联对 KV Cache 分片的影响是分布式推理中的已知技术考量，陈述逻辑完整。

## Search Query

RTX 3090 used price 2024 vs L40S price
