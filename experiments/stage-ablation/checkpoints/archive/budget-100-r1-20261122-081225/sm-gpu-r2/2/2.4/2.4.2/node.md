# N93: NVFP4 量化下，Embedding 层通常不被量化（保持 BF16 或 FP16），因为低比特量化对词嵌入的语义保持影响较大，若 Embedding 保持 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

NVFP4 量化下，Embedding 层通常不被量化（保持 BF16 或 FP16），因为低比特量化对词嵌入的语义保持影响较大，若 Embedding 保持 BF16 (1.24 GB)，则总文件大小为 13.5 GB + 1.24 GB = 14.74 GB；若 Embedding 量化为 NVFP4，则总文件大小为 14.16 GB。

## Corrected Claim

NVFP4 量化下，Embedding 层通常不被量化（保持 BF16 或 FP16），因为低比特量化对词嵌入的语义保持影响较大，若 Embedding 保持 BF16 (1.24 GB)，则总文件大小为 13.5 GB + 1.24 GB = 14.74 GB；若 Embedding 量化为 NVFP4，则总文件大小为 14.16 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算 13.5 + 1.24 = 14.74 正确；Embedding 层因语义敏感性通常保持高精度（BF16/FP16）符合工程惯例；NVFP4 量化后体积减小符合低比特量化原理。
