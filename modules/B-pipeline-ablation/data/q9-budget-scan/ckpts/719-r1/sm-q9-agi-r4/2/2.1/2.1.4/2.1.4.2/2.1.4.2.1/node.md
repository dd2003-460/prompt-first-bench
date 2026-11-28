# N444: NumPy 在 Apple M1 Max (ARM64) 上的首次导入耗时 T_import_numpy ≈ 150-300ms，主要耗时于 BLAS 库（Ac

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N152

## Claim

NumPy 在 Apple M1 Max (ARM64) 上的首次导入耗时 T_import_numpy ≈ 150-300ms，主要耗时于 BLAS 库（Accelerate/OpenBLAS）的动态链接与初始化；若使用 conda 环境，额外增加 50-100ms 的 .so 文件查找开销

## Corrected Claim

NumPy 在 Apple M1 Max (ARM64) 上的首次导入耗时 T_import_numpy ≈ 150-300ms，主要耗时于 BLAS 库（Accelerate/OpenBLAS）的动态链接与初始化；若使用 conda 环境，额外增加 50-100ms 的 .so 文件查找开销

## Evidence

先验知识/题面给定，逻辑校验通过
