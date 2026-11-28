# N31: NVFP4/W4 精度下静态权重显存占用计算为 27,000,000,000 * 0.5 bytes = 13.5 GB，实际部署中因 Block-wise Q

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7, N8, N9

## Claim

NVFP4/W4 精度下静态权重显存占用计算为 27,000,000,000 * 0.5 bytes = 13.5 GB，实际部署中因 Block-wise Quantization 的 Scale/Zero-point 元数据开销会增加约 2-5% 的额外显存

## Corrected Claim

NVFP4/W4 精度下静态权重显存占用计算为 27,000,000,000 * 0.5 bytes = 13.5 GB，实际部署中因 Block-wise Quantization 的 Scale/Zero-point 元数据开销会增加约 2-5% 的额外显存

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数*0.5字节=13.5GB计算正确，Block-wise量化元数据开销2-5%符合工程常识
