# N42: NVFP4/W4量化下的权重显存占用：27.2B params * 0.5 bytes/param = 13.6GB（假设4-bit权重，无额外索引开销）

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N9

## Claim

NVFP4/W4量化下的权重显存占用：27.2B params * 0.5 bytes/param = 13.6GB（假设4-bit权重，无额外索引开销）

## Corrected Claim

NVFP4/W4量化下的权重显存占用：27.2B params * 0.5 bytes/param = 13.6GB（假设4-bit权重，无额外索引开销）

## Evidence

先验知识/题面给定，逻辑校验通过：27.2B * 0.5 bytes = 13.6GB，计算无误且符合4-bit量化显存占用估算逻辑
