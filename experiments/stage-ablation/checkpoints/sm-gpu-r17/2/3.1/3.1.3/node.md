# N34: FP8 权重占用空间计算：27.8B * 1 byte = 27.8 GB，假设所有层均支持 FP8 量化且无额外 scale 因子开销

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

FP8 权重占用空间计算：27.8B * 1 byte = 27.8 GB，假设所有层均支持 FP8 量化且无额外 scale 因子开销

## Corrected Claim

FP8 权重占用空间计算：27.8B * 1 byte = 27.8 GB，假设所有层均支持 FP8 量化且无额外 scale 因子开销

## Evidence

先验知识/题面给定，逻辑校验通过：27.8B参数在FP8（1字节/参数）下占用空间确为27.8GB，计算逻辑自洽且量级合理。
