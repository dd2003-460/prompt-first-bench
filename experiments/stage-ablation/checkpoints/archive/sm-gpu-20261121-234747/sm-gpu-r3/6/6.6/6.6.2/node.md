# N441: NVFP4 量化所需的 FP8 块级缩放因子（Block-wise Scale）额外显存占用：27e9 / 128 (group_size) * 1 byte 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N143

## Claim

NVFP4 量化所需的 FP8 块级缩放因子（Block-wise Scale）额外显存占用：27e9 / 128 (group_size) * 1 byte = 21.1 MB，相对于权重本体占比约 0.16%

## Corrected Claim

NVFP4 量化所需的 FP8 块级缩放因子（Block-wise Scale）额外显存占用：27e9 / 128 (group_size) * 1 byte = 21.1 MB，相对于权重本体占比约 0.16%

## Evidence

先验知识/题面给定，逻辑校验通过：27e9/128*1B ≈ 21.09MB，占比 21.09/13500 ≈ 0.156%，计算与量级均合理
