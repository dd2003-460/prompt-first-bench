# N277: LFU 频率阈值 f_threshold 的基准值：在 β=0.9 热度分布下，f_threshold ≈ Z * (N_cache)^{β-1}，其中 Z 为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N97

## Claim

LFU 频率阈值 f_threshold 的基准值：在 β=0.9 热度分布下，f_threshold ≈ Z * (N_cache)^{β-1}，其中 Z 为归一化常数，该阈值决定了 LFU 保留对象的频率下限。

## Corrected Claim

LFU 频率阈值 f_threshold 的基准值：在 β=0.9 热度分布下，f_threshold ≈ Z * (N_cache)^{β-1}，其中 Z 为归一化常数，该阈值决定了 LFU 保留对象的频率下限。

## Evidence

先验知识/题面给定，逻辑校验通过
