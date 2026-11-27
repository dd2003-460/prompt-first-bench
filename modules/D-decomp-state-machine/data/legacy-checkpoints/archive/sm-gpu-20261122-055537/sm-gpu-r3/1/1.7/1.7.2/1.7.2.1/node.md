# N192: CUDA Context 静态显存占用基准值：在 RTX 4090 (Ada Lovelace) 上约为 100-150 MB，在 NVIDIA L4 上约为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N57

## Claim

CUDA Context 静态显存占用基准值：在 RTX 4090 (Ada Lovelace) 上约为 100-150 MB，在 NVIDIA L4 上约为 80-120 MB；该值由驱动版本和并发上下文数量决定，通常不随模型大小变化。

## Corrected Claim

CUDA Context 静态显存占用基准值：在 RTX 4090 (Ada Lovelace) 上约为 100-150 MB，在 NVIDIA L4 上约为 80-120 MB；该值由驱动版本和并发上下文数量决定，通常不随模型大小变化。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

CUDA context memory usage overhead per context MB
