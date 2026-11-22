# N779: H100 SXM 在 BF16 下运行 Qwen3-27B 的最大有效并发 Batch Size 修正为 1 (若计入 2GB 框架开销) 或 2 (若忽略开销

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N242, N243, N244

## Claim

H100 SXM 在 BF16 下运行 Qwen3-27B 的最大有效并发 Batch Size 修正为 1 (若计入 2GB 框架开销) 或 2 (若忽略开销)，Batch Size=2 时显存占用 79.16GB，剩余 0.84GB 无法容纳额外 KV 块，故物理上限为 2，但实际吞吐受限于 Attention 计算而非显存。

## Corrected Claim

H100 SXM 在 BF16 下运行 Qwen3-27B 的最大有效并发 Batch Size 修正为 1 (若计入 2GB 框架开销) 或 2 (若忽略开销)，Batch Size=2 时显存占用 79.16GB，剩余 0.84GB 无法容纳额外 KV 块，故物理上限为 2，但实际吞吐受限于 Attention 计算而非显存。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM 80GB 显存下，Qwen3-27B BF16 权重约 54GB，Batch=2 时 KV Cache 及激活值占用约 25GB，总占用 79.16GB 符合物理极限，剩余 0.84GB 不足以支撑 Batch=3 的 KV 增量，逻辑自洽。
