# N91: INT8 量化通常伴随 Embedding 层保持 FP16 或 INT8 转换的选择，若 Embedding 保持 FP16 (151,936 × 4096 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

INT8 量化通常伴随 Embedding 层保持 FP16 或 INT8 转换的选择，若 Embedding 保持 FP16 (151,936 × 4096 × 2 bytes ≈ 1.24 GB)，则总文件大小为 27 GB + 1.24 GB = 28.24 GB；若 Embedding 也量化为 INT8，则总文件大小为 27.62 GB。

## Corrected Claim

INT8 量化通常伴随 Embedding 层保持 FP16 或 INT8 转换的选择，若 Embedding 保持 FP16 (151,936 × 4096 × 2 bytes ≈ 1.24 GB)，则总文件大小为 27 GB + 1.24 GB = 28.24 GB；若 Embedding 也量化为 INT8，则总文件大小为 27.62 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：Embedding 层参数量 151,936 × 4096 ≈ 6.22 亿，FP16 下约 1.24 GB，INT8 下约 0.62 GB；总大小计算 27 + 1.24 = 28.24 GB 及 27.62 GB 均符合算术逻辑与量级常识。
