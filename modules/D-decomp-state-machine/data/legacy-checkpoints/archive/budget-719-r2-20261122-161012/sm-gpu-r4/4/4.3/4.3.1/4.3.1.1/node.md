# N213: Qwen3-27B 在 BF16 精度下，单 token (batch=1) 的 All-Reduce 通信数据量 D_comm 修正为 8.192 KB (4

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

Qwen3-27B 在 BF16 精度下，单 token (batch=1) 的 All-Reduce 通信数据量 D_comm 修正为 8.192 KB (4096 * 2 bytes)，而非 8KB，该数值是计算通信延迟占比的基础参数。

## Corrected Claim

Qwen3-27B 在 BF16 精度下，单 token (batch=1) 的 All-Reduce 通信数据量 D_comm 修正为 8.192 KB (4096 * 2 bytes)，而非 8KB，该数值是计算通信延迟占比的基础参数。

## Evidence

先验知识/题面给定，逻辑校验通过：4096 * 2 bytes = 8192 bytes = 8.192 KB，计算正确且符合BF16精度下隐藏层维度为4096的常见配置。
