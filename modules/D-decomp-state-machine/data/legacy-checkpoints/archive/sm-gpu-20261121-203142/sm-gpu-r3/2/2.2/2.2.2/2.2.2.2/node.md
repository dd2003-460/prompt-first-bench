# N180: RTX 4090 上 W8A16 (权重FP8, 激活BF16) 与 W8A8 (权重FP8, 激活FP8) 的延迟差异主要源于反量化开销和激活值精度转换；在 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N53

## Claim

RTX 4090 上 W8A16 (权重FP8, 激活BF16) 与 W8A8 (权重FP8, 激活FP8) 的延迟差异主要源于反量化开销和激活值精度转换；在 Compute-bound 的 Prefill 阶段，W8A8 比 W8A16 快约 10-20%，但在 Memory-bound 的 Decode 阶段，由于权重读取字节数相同 (8-bit vs 16-bit 激活不影响权重读取)，两者 TPS 差异 <5%，主要差异在于 KV Cache 是否也使用 FP8 存储。

## Corrected Claim

RTX 4090 上 W8A16 (权重FP8, 激活BF16) 与 W8A8 (权重FP8, 激活FP8) 的延迟差异主要源于反量化开销和激活值精度转换；在 Compute-bound 的 Prefill 阶段，W8A8 比 W8A16 快约 10-20%，但在 Memory-bound 的 Decode 阶段，由于权重读取字节数相同 (8-bit vs 16-bit 激活不影响权重读取)，两者 TPS 差异 <5%，主要差异在于 KV Cache 是否也使用 FP8 存储。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill阶段计算密集，W8A8利用FP8 Tensor Core加速矩阵乘法，相比W8A16（需反量化或混合精度计算）有显著速度优势（10-20%合理）；Decode阶段访存密集，权重均为8-bit，带宽瓶颈相同，故TPS差异小，主要取决于KV Cache精度。

## Search Query

W8A8 vs W8A16 inference latency difference RTX 4090 FP8
