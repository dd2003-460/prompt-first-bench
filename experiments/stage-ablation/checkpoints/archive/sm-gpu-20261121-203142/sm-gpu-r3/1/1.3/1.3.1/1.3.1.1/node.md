# N143: Qwen3-27B NVFP4/W4量化权重的基础显存占用：27.2e9 params * 0.5 bytes/param = 13.6 GB

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42

## Claim

Qwen3-27B NVFP4/W4量化权重的基础显存占用：27.2e9 params * 0.5 bytes/param = 13.6 GB

## Corrected Claim

Qwen3-27B NVFP4/W4量化权重的基础显存占用：27.2e9 params * 0.5 bytes/param = 13.6 GB

## Evidence

先验知识/题面给定，逻辑校验通过：27.2e9 * 0.5 = 13.6e9 bytes = 13.6 GB，计算无误且符合NVFP4/W4量化（4-bit权重+少量开销或纯4-bit）的显存估算逻辑。
