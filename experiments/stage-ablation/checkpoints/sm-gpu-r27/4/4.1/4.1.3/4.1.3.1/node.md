# N174: Qwen3-27B 在 INT4 量化下的权重显存占用：27B 参数 * 0.5 bytes/param = 13.5 GB，加上 CUDA 上下文开销（约 0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N56

## Claim

Qwen3-27B 在 INT4 量化下的权重显存占用：27B 参数 * 0.5 bytes/param = 13.5 GB，加上 CUDA 上下文开销（约 0.5-1 GB），总权重占用约 14-14.5 GB

## Corrected Claim

Qwen3-27B 在 INT4 量化下的权重显存占用：27B 参数 * 0.5 bytes/param = 13.5 GB，加上 CUDA 上下文开销（约 0.5-1 GB），总权重占用约 14-14.5 GB

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数在INT4（4-bit）下每参数占0.5字节，计算得13.5GB，加上CUDA上下文开销后总量级合理。
