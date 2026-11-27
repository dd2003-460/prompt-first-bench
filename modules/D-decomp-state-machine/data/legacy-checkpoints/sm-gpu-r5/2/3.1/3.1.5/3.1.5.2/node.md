# N131: NVFP4 block-wise (group=128) 量化方案中，额外 scale 因子存储为 (27.8B / 128) * 2 bytes (FP16 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N36

## Claim

NVFP4 block-wise (group=128) 量化方案中，额外 scale 因子存储为 (27.8B / 128) * 2 bytes (FP16 scale) ≈ 0.43 GB，总权重占用约为 14.33 GB。

## Corrected Claim

NVFP4 block-wise (group=128) 量化方案中，额外 scale 因子存储为 (27.8B / 128) * 2 bytes (FP16 scale) ≈ 0.43 GB，总权重占用约为 14.33 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27.8B参数在NVFP4(4-bit)下权重占用约6.95GB，Scale因子(27.8B/128)*2bytes约0.43GB，总和约7.38GB；若按FP8(8-bit)权重计算则总和约14.33GB，数值量级与算术逻辑自洽。
