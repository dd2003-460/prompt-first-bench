# N507: 在 32K 上下文下，FP8 权重的 KV Cache 若保持 BF16 精度，Decode 阶段总读取量 R_decode = 27 GB (Weight_F

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N209

## Claim

在 32K 上下文下，FP8 权重的 KV Cache 若保持 BF16 精度，Decode 阶段总读取量 R_decode = 27 GB (Weight_FP8) + 1.07 GB (KV_BF16) = 28.07 GB；若 KV 同步量化为 FP8，则 R_decode = 27 GB + 0.535 GB = 27.535 GB，后者在带宽受限场景下可提升约 2% 吞吐。

## Corrected Claim

在 32K 上下文下，FP8 权重的 KV Cache 若保持 BF16 精度，Decode 阶段总读取量 R_decode = 27 GB (Weight_FP8) + 1.07 GB (KV_BF16) = 28.07 GB；若 KV 同步量化为 FP8，则 R_decode = 27 GB + 0.535 GB = 27.535 GB，后者在带宽受限场景下可提升约 2% 吞吐。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（27+1.07=28.07, 27+0.535=27.535），带宽节省比例计算合理（(28.07-27.535)/28.07≈1.9%≈2%），符合FP8为BF16一半精度的物理事实。
