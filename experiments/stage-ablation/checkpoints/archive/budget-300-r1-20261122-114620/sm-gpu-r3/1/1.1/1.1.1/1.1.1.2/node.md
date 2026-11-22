# N141: Qwen3-27B 的注意力层（QKV/O）参数量约为 3.2B，计算公式为 64 * 4 * 4096 * 4096 * 2 / 2 (BF16 bytes)

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

Qwen3-27B 的注意力层（QKV/O）参数量约为 3.2B，计算公式为 64 * 4 * 4096 * 4096 * 2 / 2 (BF16 bytes) ≈ 6.4GB，占总显存 54.2GB 的 12%

## Corrected Claim

Qwen3-27B 的注意力层（QKV/O）参数量约为 4.3B，计算公式为 64 * 4 * 4096 * 4096 * 2 / 2 (BF16 bytes) ≈ 8.6GB，占总显存 54.2GB 的 15.8%

## Evidence

[质询]数值量级与内部逻辑矛盾：1. 参数量计算错误：64 * 4 * 4096 * 4096 = 4.29B，而非3.2B；2. 显存计算错误：4.29B参数 * 2 bytes = 8.58GB，而非6.4GB；3. 占比计算错误：8.58GB / 54.2GB ≈ 15.8%，而非12%。陈述中的数值（3.2B, 6.4GB, 12%）与公式及总显存不匹配。 | 先验知识/题面给定，逻辑校验失败：公式计算结果与陈述数值不符，存在内部矛盾。
