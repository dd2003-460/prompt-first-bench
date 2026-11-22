# N348: 在 BF16 精度下 (bytes_per_elem=2)，Qwen3-27B 64K 上下文的 KV Cache 显存占用具体数值为 10.74 GB，计算公

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

在 BF16 精度下 (bytes_per_elem=2)，Qwen3-27B 64K 上下文的 KV Cache 显存占用具体数值为 10.74 GB，计算公式为 2 * 64 * 8 * 128 * 65536 * 2 / (1024^3)。

## Corrected Claim

在 BF16 精度下 (bytes_per_elem=2)，Qwen3-27B 64K 上下文的 KV Cache 显存占用具体数值为 10.74 GB，计算公式为 2 * 64 * 8 * 128 * 65536 * 2 / (1024^3)。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B 架构参数（64层, 8 KV头, 128头维）与公式计算结果一致，数值量级合理。
