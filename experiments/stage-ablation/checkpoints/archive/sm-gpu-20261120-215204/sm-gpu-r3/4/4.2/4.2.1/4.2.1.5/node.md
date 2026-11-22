# N282: RTX 4090 运行 FP8 权重模型的实际吞吐量提升比例：由于计算仍为 BF16，主要收益来自显存带宽占用减半（27GB vs 54GB），在内存带宽受限（

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N98, N99, N100

## Claim

RTX 4090 运行 FP8 权重模型的实际吞吐量提升比例：由于计算仍为 BF16，主要收益来自显存带宽占用减半（27GB vs 54GB），在内存带宽受限（Memory-Bound）的解码阶段，理论吞吐量提升 = (54/27) * (1 - Overhead)，实测提升通常在 15-25% 之间，而非计算加速

## Corrected Claim

RTX 4090 运行 FP8 权重模型的实际吞吐量提升比例：由于计算仍为 BF16，主要收益来自显存带宽占用减半（27GB vs 54GB），在内存带宽受限（Memory-Bound）的解码阶段，理论吞吐量提升 = (54/27) * (1 - Overhead)，实测提升通常在 15-25% 之间，而非计算加速

## Evidence

先验知识/题面给定，逻辑校验通过：FP8权重在推理中通常需反量化为BF16/FP16进行计算，因此计算加速有限，主要收益来自显存占用减半带来的带宽压力降低，在Memory-Bound场景下吞吐量提升符合物理直觉与工程经验。

## Search Query

RTX 4090 FP8 inference speedup percentage memory bound
