# N401: Apple M4 Max显存溢出的临界条件：在BF16精度下，若Batch=2且Seq_len=32K，总显存需求≈54 + 2*16.8 + 10 = 97.

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N143

## Claim

Apple M4 Max显存溢出的临界条件：在BF16精度下，若Batch=2且Seq_len=32K，总显存需求≈54 + 2*16.8 + 10 = 97.6GB，超过可用上限96GB，导致OOM；此时必须降低精度至INT8或减少Batch/Seq_len。

## Corrected Claim

Apple M4 Max 在 BF16 精度下，Batch=2 且 Seq_len=32K 时，显存需求接近或超过 96GB 上限，可能导致 OOM，建议降低精度或减少 Batch/Seq_len。

## Evidence

[质询]数值计算存在内部矛盾：54 + 2*16.8 + 10 = 97.6 的算术结果应为 97.6，但 54+33.6+10=97.6 是正确的。然而，M4 Max 的内存带宽和容量限制下，96GB 是统一内存上限，但 97.6GB 是否真的导致 OOM 取决于系统预留内存（通常 macOS 会保留部分内存给系统），且 BF16 下 32K 序列的 KV Cache 计算是否准确（16.8GB 每 batch 是否合理需验证）。 | 先验知识/题面给定，逻辑校验通过，但数值细节（如 16.8GB 的 KV Cache 估算）缺乏外部来源支持，且系统预留内存可能影响实际 OOM 阈值。
