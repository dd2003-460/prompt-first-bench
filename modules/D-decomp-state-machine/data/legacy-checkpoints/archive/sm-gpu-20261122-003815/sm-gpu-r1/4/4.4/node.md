# N25: 推理吞吐量瓶颈分析：对于 Decode 阶段，吞吐主要受限于显存带宽 (Memory Bandwidth)。所需最小带宽 = (weights_size + K

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

推理吞吐量瓶颈分析：对于 Decode 阶段，吞吐主要受限于显存带宽 (Memory Bandwidth)。所需最小带宽 = (weights_size + KV_cache_size) / latency_target。若要求 100ms/token 延迟，BF16 下需带宽 ≈ (54GB + 17.2GB) / 0.1s = 712 GB/s。

## Corrected Claim

推理吞吐量瓶颈分析：对于 Decode 阶段，吞吐主要受限于显存带宽 (Memory Bandwidth)。所需最小带宽 = (weights_size + KV_cache_size) / latency_target。若要求 100ms/token 延迟，BF16 下需带宽 ≈ (54GB + 17.2GB) / 0.1s = 712 GB/s。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 (54+17.2)/0.1 = 712 正确，且符合 Decode 阶段受显存带宽限制的基本原理。
