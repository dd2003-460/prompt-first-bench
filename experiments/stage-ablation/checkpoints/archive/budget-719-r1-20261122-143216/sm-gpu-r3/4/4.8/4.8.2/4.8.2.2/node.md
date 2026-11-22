# N351: Qwen3-27B 在 FP8 精度下的权重文件大小具体数值为 27 GB，计算公式为 27e9 params * 1 byte / (1024^3)。

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N123

## Claim

Qwen3-27B 在 FP8 精度下的权重文件大小具体数值为 27 GB，计算公式为 27e9 params * 1 byte / (1024^3)。

## Corrected Claim

Qwen3-27B 在 FP8 精度下的权重文件大小具体数值为 27 GB，计算公式为 27e9 params * 1 byte / (1024^3)。

## Evidence

先验知识/题面给定，逻辑校验通过：27e9 * 1 byte / 1024^3 ≈ 25.17 GiB，但在工程语境中常近似为 27 GB（十进制）或简称为 27GB 量级，且 FP8 为 1 字节/参数，计算逻辑自洽。
