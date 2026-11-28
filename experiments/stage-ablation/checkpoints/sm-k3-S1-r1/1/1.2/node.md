# N9: Qwen3-27B在NVFP4量化下的模型权重占用显存约为13.5GB（27e9 params * 0.5 bytes/param），剩余约46.5GB显存用于

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1

## Claim

Qwen3-27B在NVFP4量化下的模型权重占用显存约为13.5GB（27e9 params * 0.5 bytes/param），剩余约46.5GB显存用于KV Cache和激活值。

## Corrected Claim

Qwen3-27B在NVFP4量化下的模型权重占用显存约为13.5GB（27e9 params * 0.5 bytes/param），剩余约46.5GB显存用于KV Cache和激活值。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 0.5 = 13.5GB，80 - 13.5 = 46.5GB，计算无误且符合NVFP4量化定义。
