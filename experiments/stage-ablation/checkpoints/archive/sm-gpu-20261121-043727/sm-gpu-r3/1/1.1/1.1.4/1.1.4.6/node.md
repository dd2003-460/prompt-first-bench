# N117: FlashAttention 对 Prefill 阶段显存占用的影响系数：对比标准 Attention (O(N^2) 显存) 与 FlashAttention

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N42, N43, N44

## Claim

FlashAttention 对 Prefill 阶段显存占用的影响系数：对比标准 Attention (O(N^2) 显存) 与 FlashAttention (O(N) 显存)，在 32K 序列长度下，FlashAttention 将激活值显存占用从潜在的 ~128 GB (未优化) 降低至 ~2 GB 量级，因此 N44 中 '2-5 GB' 的估算仅在使用 FlashAttention 或类似 IO 感知算法时成立，若使用 naive 实现则显存需求将超出任何单卡容量

## Corrected Claim

FlashAttention 对 Prefill 阶段显存占用的影响系数：对比标准 Attention (O(N^2) 显存) 与 FlashAttention (O(N) 显存)，在 32K 序列长度下，FlashAttention 将激活值显存占用从潜在的 ~128 GB (未优化) 降低至 ~2 GB 量级，因此 N44 中 '2-5 GB' 的估算仅在使用 FlashAttention 或类似 IO 感知算法时成立，若使用 naive 实现则显存需求将超出任何单卡容量

## Evidence

先验知识/题面给定，逻辑校验通过：FlashAttention 将显存复杂度从 O(N^2) 降至 O(N)，在 32K 序列长度下，标准 Attention 的激活值显存占用确实会达到百 GB 量级（远超单卡容量），而 FlashAttention 可将其降至 GB 量级，与陈述中的数值量级和逻辑推导一致。
