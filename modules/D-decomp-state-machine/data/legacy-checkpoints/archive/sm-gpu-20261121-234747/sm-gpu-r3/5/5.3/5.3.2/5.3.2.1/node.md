# N362: 条件空间基数计算：总组合数 N_total = 4(预算区间) × 3(延迟区间) × 4(精度档位) = 48，其中预算区间为 <5k, 5k-15k, 15

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N125

## Claim

条件空间基数计算：总组合数 N_total = 4(预算区间) × 3(延迟区间) × 4(精度档位) = 48，其中预算区间为 <5k, 5k-15k, 15k-30k, >30k；延迟区间为 <100ms, 100-500ms, >500ms；精度档位为 BF16, FP8, INT8, W4/NVFP4。

## Corrected Claim

条件空间基数计算：总组合数 N_total = 4(预算区间) × 3(延迟区间) × 4(精度档位) = 48，其中预算区间为 <5k, 5k-15k, 15k-30k, >30k；延迟区间为 <100ms, 100-500ms, >500ms；精度档位为 BF16, FP8, INT8, W4/NVFP4。

## Evidence

先验知识/题面给定，逻辑校验通过：4×3×4=48，且各维度区间定义清晰无重叠，符合组合数学基本原理。
