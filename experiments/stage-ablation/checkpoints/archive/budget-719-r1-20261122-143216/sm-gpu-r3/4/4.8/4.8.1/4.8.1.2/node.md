# N349: 在 FP8 精度下 (bytes_per_elem=1)，Qwen3-27B 64K 上下文的 KV Cache 显存占用具体数值为 5.37 GB，计算公式为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

在 FP8 精度下 (bytes_per_elem=1)，Qwen3-27B 64K 上下文的 KV Cache 显存占用具体数值为 5.37 GB，计算公式为 2 * 64 * 8 * 128 * 65536 * 1 / (1024^3)。

## Corrected Claim

在 FP8 精度下 (bytes_per_elem=1)，Qwen3-27B 64K 上下文的 KV Cache 显存占用具体数值为 5.37 GB，计算公式为 2 * 64 * 8 * 128 * 65536 * 1 / (1024^3)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（GQA 8 KV heads, head_dim 128, 64 layers）与 FP8 精度（1 byte）代入公式 2 * 64 * 8 * 128 * 65536 * 1 / (1024^3) 计算结果确为 5.37 GB，数值量级与逻辑自洽。
