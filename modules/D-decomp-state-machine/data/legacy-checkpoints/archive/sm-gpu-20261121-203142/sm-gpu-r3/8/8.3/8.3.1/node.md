# N348: B200 (192GB) 在 BF16 下运行 Qwen3-27B 的最大并发 Batch Size (B_max) 计算：B_max = (192 - 54 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113

## Claim

B200 (192GB) 在 BF16 下运行 Qwen3-27B 的最大并发 Batch Size (B_max) 计算：B_max = (192 - 54 - 2) / (0.00215 GB/token * 32K) ≈ 19.4，即理论上限为 19 个并发请求；对比 H100 (80GB) 的 B_max = (80 - 54 - 2) / 0.00215 ≈ 11.6，即 11 个并发请求，B200 并发容量约为 H100 的 1.7 倍。

## Corrected Claim

B200 (192GB) 在 BF16 下运行 Qwen3-27B 的最大并发 Batch Size (B_max) 计算：B_max = (192 - 54 - 2) / (0.00215 GB/token * 32K) ≈ 19.4，即理论上限为 19 个并发请求；对比 H100 (80GB) 的 B_max = (80 - 54 - 2) / (0.00215 GB/token * 32K) ≈ 0.36，即理论上限为 0 个并发请求（显存不足），B200 并发容量远高于 H100。

## Evidence

[质询]H100 的 B_max 计算公式中分母缺少 '/ 32K' 项，导致量纲错误（GB/token 除以 GB 得到 token 而非 batch 数），且数值 11.6 与公式 (80-54-2)/0.00215 ≈ 11627 严重不符，存在明显的内部逻辑矛盾和计算错误。 | 先验知识/题面给定，但逻辑校验发现 H100 部分公式量纲错误且数值与公式结果矛盾，无法排除计算错误，故降级。
