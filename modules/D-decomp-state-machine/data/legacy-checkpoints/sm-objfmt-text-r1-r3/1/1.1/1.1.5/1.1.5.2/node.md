# N105: 考虑元数据开销后，NVFP4/W4 权重的实际显存占用范围：保守估计（高 block size，仅 scale）为 13.5 * 1.05 = 14.18 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N31

## Claim

考虑元数据开销后，NVFP4/W4 权重的实际显存占用范围：保守估计（高 block size，仅 scale）为 13.5 * 1.05 = 14.18 GB；悲观估计（小 block size，scale+zero）为 13.5 * 1.15 = 15.53 GB；因此 24GB 显卡剩余空间仅为 8.47-9.82 GB，进一步压缩了 KV Cache 可用空间。

## Corrected Claim

考虑元数据开销后，NVFP4/W4 权重的实际显存占用范围：保守估计（高 block size，仅 scale）为 13.5 * 1.05 = 14.18 GB；悲观估计（小 block size，scale+zero）为 13.5 * 1.15 = 15.53 GB；因此 24GB 显卡剩余空间仅为 8.47-9.82 GB，进一步压缩了 KV Cache 可用空间。

## Evidence

先验知识/题面给定，逻辑校验通过：13.5GB基础权重乘以1.05和1.15的元数据开销系数计算正确，24GB减去对应占用后的剩余空间计算亦无误，符合显存管理的基本算术逻辑。
