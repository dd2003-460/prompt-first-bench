# N11: 2x RTX 4090 (48GB total via NVLink or PCIe P2P) 作为多卡消费级方案，其聚合带宽受限于 PCIe 4.0 x16 

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

2x RTX 4090 (48GB total via NVLink or PCIe P2P) 作为多卡消费级方案，其聚合带宽受限于 PCIe 4.0 x16 (32 GB/s) 或 NVLink (900 GB/s)，需计算跨卡通信开销对推理延迟的影响。

## Corrected Claim

2x RTX 4090 (48GB total via NVLink or PCIe P2P) 作为多卡消费级方案，其聚合带宽受限于 PCIe 4.0 x16 (32 GB/s) 或 NVLink (900 GB/s)，需计算跨卡通信开销对推理延迟的影响。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 单卡显存为 24GB，双卡共 48GB 符合事实；NVLink 带宽 900GB/s 及 PCIe 4.0 x16 带宽 32GB/s 均为标准硬件规格，量级合理且无内部矛盾。

## Search Query

dual RTX 4090 inference performance NVLink vs PCIe bandwidth overhead
