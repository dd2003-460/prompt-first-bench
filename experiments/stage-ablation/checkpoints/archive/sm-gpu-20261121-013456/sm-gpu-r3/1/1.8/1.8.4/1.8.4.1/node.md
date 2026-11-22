# N186: INT4 权重显存占用计算：27B 参数 * 0.5 bytes/param (AWQ/GPTQ) = 13.5 GB

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N74

## Claim

INT4 权重显存占用计算：27B 参数 * 0.5 bytes/param (AWQ/GPTQ) = 13.5 GB

## Corrected Claim

INT4 权重显存占用计算：27B 参数 * 0.5 bytes/param (AWQ/GPTQ) = 13.5 GB

## Evidence

先验知识/题面给定，逻辑校验通过：INT4 量化下每参数占用 0.5 字节（4 bits），27B 参数乘以 0.5 bytes/param 等于 13.5 GB，计算无误且符合 AWQ/GPTQ 等 4-bit 量化方案的显存占用规律。
