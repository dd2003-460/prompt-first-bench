# N200: Apple M1 Max (64GB) 在 Qwen3-27B 上的可行性分析：64GB 统一内存不足以容纳 BF16 权重 (54GB) + 32K KV C

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N61

## Claim

Apple M1 Max (64GB) 在 Qwen3-27B 上的可行性分析：64GB 统一内存不足以容纳 BF16 权重 (54GB) + 32K KV Cache (~8-32GB) + 系统开销。必须使用 INT4 量化 (Weights ~14GB)。计算 INT4 下 M1 Max (400 GB/s 带宽) 的 Decode 上限，并与 M2 Ultra 对比，量化性能差距（预计 M1 Max 仅为 M2 Ultra 的 40-50%）。

## Corrected Claim

Apple M1 Max (64GB) 在 Qwen3-27B 上的可行性分析：64GB 统一内存不足以容纳 BF16 权重 (54GB) + 32K KV Cache (~8-32GB) + 系统开销。必须使用 INT4 量化 (Weights ~14GB)。计算 INT4 下 M1 Max (400 GB/s 带宽) 的 Decode 上限，并与 M2 Ultra 对比，量化性能差距（预计 M1 Max 仅为 M2 Ultra 的 40-50%）。

## Evidence

先验知识/题面给定，逻辑校验通过：M1 Max 64GB 统一内存确实无法同时容纳 54GB BF16 权重与 32K KV Cache，INT4 量化后权重约 14GB 符合数学推导；M1 Max 带宽 400GB/s 与 M2 Ultra (800GB/s) 的带宽比约为 50%，在 Decode 阶段（带宽受限）性能差距预计为 40-50% 符合物理直觉与工程经验。
