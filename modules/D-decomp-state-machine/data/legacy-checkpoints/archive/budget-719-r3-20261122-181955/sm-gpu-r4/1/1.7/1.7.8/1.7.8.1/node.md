# N242: Qwen3-27B 的实际参数量并非 27.1 亿（2.71B），而是约 270 亿（27B），原文 N76 中‘27.1 亿’为数量级错误；修正后 BF16 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N76

## Claim

Qwen3-27B 的实际参数量并非 27.1 亿（2.71B），而是约 270 亿（27B），原文 N76 中‘27.1 亿’为数量级错误；修正后 BF16 权重内存占用确认为 27.1e9 * 2 bytes = 54.2 GB，该数值与 N82 一致，但参数量描述必须修正为 27B。

## Corrected Claim

Qwen3-27B 的实际参数量并非 27.1 亿（2.71B），而是约 270 亿（27B），原文 N76 中‘27.1 亿’为数量级错误；修正后 BF16 权重内存占用确认为 27.1e9 * 2 bytes = 54.2 GB，该数值与 N82 一致，但参数量描述必须修正为 27B。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 参数量确为 27B（270亿），27.1e9 * 2 bytes = 54.2 GB 计算正确，与 N82 一致。
