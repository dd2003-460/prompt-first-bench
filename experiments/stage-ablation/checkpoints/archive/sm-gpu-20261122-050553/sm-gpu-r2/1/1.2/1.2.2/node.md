# N41: RTX 4060 Ti 多卡扩展瓶颈：2×4060 Ti (32GB) 虽容量勉强满足 W4+KV Cache (~30GB)，但聚合显存带宽仅 544 GB/

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N8

## Claim

RTX 4060 Ti 多卡扩展瓶颈：2×4060 Ti (32GB) 虽容量勉强满足 W4+KV Cache (~30GB)，但聚合显存带宽仅 544 GB/s (2*272)，且 PCIe 4.0 x16 跨卡通信带宽 32 GB/s 远低于 NVLink，导致张量并行 (Tensor Parallelism) 的通信开销占比极高，预计吞吐比单卡 4090 低 50% 以上，性价比极低。

## Corrected Claim

RTX 4060 Ti 多卡扩展瓶颈：2×4060 Ti (32GB) 虽容量勉强满足 W4+KV Cache (~30GB)，但聚合显存带宽仅 544 GB/s (2*272)，且 PCIe 4.0 x16 跨卡通信带宽 32 GB/s 远低于 NVLink，导致张量并行 (Tensor Parallelism) 的通信开销占比极高，预计吞吐比单卡 4090 低 50% 以上，性价比极低。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4060 Ti 显存带宽 272GB/s，双卡聚合 544GB/s 计算正确；PCIe 4.0 x16 带宽约 32GB/s 符合规格；相比单卡 4090 (1008GB/s) 带宽劣势及跨卡通信瓶颈导致吞吐大幅下降符合硬件架构逻辑。

## Search Query

RTX 4060 Ti dual card LLM inference PCIe bottleneck tensor parallelism overhead
