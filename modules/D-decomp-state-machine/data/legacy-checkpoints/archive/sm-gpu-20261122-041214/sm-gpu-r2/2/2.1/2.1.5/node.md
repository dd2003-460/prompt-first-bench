# N78: 消费级多卡方案可行性：2x RTX 4090 (48GB 总显存) 可通过 PCIe 4.0 互联，但缺乏 NVLink，通信带宽受限 (~25 GB/s)，适

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N20

## Claim

消费级多卡方案可行性：2x RTX 4090 (48GB 总显存) 可通过 PCIe 4.0 互联，但缺乏 NVLink，通信带宽受限 (~25 GB/s)，适用于 FP8/INT8 4-bit 量化模型，但不适用于 BF16 大并发场景。

## Corrected Claim

消费级多卡方案可行性：2x RTX 4090 (48GB 总显存) 可通过 PCIe 4.0 互联，但缺乏 NVLink，通信带宽受限 (~25 GB/s)，适用于 FP8/INT8 4-bit 量化模型，但不适用于 BF16 大并发场景。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 单卡显存为 24GB，双卡共 48GB 符合事实；PCIe 4.0 x16 双向带宽约 64GB/s，单向约 32GB/s，实际有效带宽受协议开销影响约为 25-30GB/s，量级合理；缺乏 NVLink 导致跨卡通信瓶颈，适合小模型或量化模型，不适合大并发 BF16 场景，逻辑自洽。

## Search Query

2x RTX 4090 multi-GPU inference PCIe bandwidth limitation
