# N204: Qwen3-27B 在 NVFP4 量化下的权重文件大小为 13.5 GB，计算公式为：Params (27e9) * Bytes_per_param (0.5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N67

## Claim

Qwen3-27B 在 NVFP4 量化下的权重文件大小为 13.5 GB，计算公式为：Params (27e9) * Bytes_per_param (0.5) / 1e9 = 13.5 GB。

## Corrected Claim

Qwen3-27B 在 NVFP4 量化下的权重文件大小为 13.5 GB，计算公式为：Params (27e9) * Bytes_per_param (0.5) / 1e9 = 13.5 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 0.5 / 1e9 = 13.5，计算无误且符合NVFP4量化原理
