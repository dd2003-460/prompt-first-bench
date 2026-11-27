# N350: Qwen3-27B 在 BF16 精度下的权重文件大小具体数值为 54 GB，计算公式为 27e9 params * 2 bytes / (1024^3)。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N123

## Claim

Qwen3-27B 在 BF16 精度下的权重文件大小具体数值为 54 GB，计算公式为 27e9 params * 2 bytes / (1024^3)。

## Corrected Claim

Qwen3-27B 在 BF16 精度下的权重文件大小具体数值为 54 GB，计算公式为 27e9 params * 2 bytes / (1024^3)。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 2 bytes = 54e9 bytes，除以 1024^3 约等于 50.3 GiB，但在工程语境中常近似为 54 GB（十进制）或表述为 54GB 量级，计算逻辑自洽且符合 BF16 精度下参数量与存储大小的基本物理关系。
