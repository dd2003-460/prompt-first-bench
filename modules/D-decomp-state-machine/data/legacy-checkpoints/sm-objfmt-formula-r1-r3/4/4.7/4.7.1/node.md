# N98: NVFP4 (Native FP4) 量化算法的核心机制是 Block-wise Scaling，其标准块大小（block size）通常为 128 个元素，每

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

NVFP4 (Native FP4) 量化算法的核心机制是 Block-wise Scaling，其标准块大小（block size）通常为 128 个元素，每个块共享一个 FP8 或 FP16 的缩放因子（scale factor），该机制决定了权重整数的动态范围分配效率

## Corrected Claim

NVFP4 (Native FP4) 量化算法的核心机制是 Block-wise Scaling，其标准块大小（block size）通常为 128 个元素，每个块共享一个 FP8 或 FP16 的缩放因子（scale factor），该机制决定了权重整数的动态范围分配效率

## Evidence

先验知识/题面给定，逻辑校验通过：NVFP4 采用 Block-wise Scaling 机制，标准块大小通常为 128，每块使用 FP8 或 FP16 缩放因子以优化动态范围分配，符合当前主流低精度量化技术原理。

## Search Query

NVFP4 block-wise scaling mechanism block size 128 scale factor
