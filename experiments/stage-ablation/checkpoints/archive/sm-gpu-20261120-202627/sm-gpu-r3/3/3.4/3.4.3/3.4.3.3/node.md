# N298: 1x A100 80GB 方案在 BF16 下的总显存需求 = 权重 (54 GB) + KV Cache (33.55 GB) + 激活/开销 (5-10 G

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N81

## Claim

1x A100 80GB 方案在 BF16 下的总显存需求 = 权重 (54 GB) + KV Cache (33.55 GB) + 激活/开销 (5-10 GB) = 92.55 - 97.55 GB。该值显著超过 A100 80GB 的单卡显存上限，因此 1x A100 80GB 在 BF16 精度下无法运行 32K 上下文的 Qwen3-27B，除非采用 KV Cache 量化 (如 FP8/INT8) 或分页注意力 (PagedAttention) 优化，但即使优化后，权重 54GB + 最小 KV Cache 仍可能超出 80GB 限制，需重新评估可行性。

## Corrected Claim

1x A100 80GB 方案在 BF16 下的总显存需求 = 权重 (54 GB) + KV Cache (33.55 GB) + 激活/开销 (5-10 GB) = 92.55 - 97.55 GB。该值显著超过 A100 80GB 的单卡显存上限，因此 1x A100 80GB 在 BF16 精度下无法运行 32K 上下文的 Qwen3-27B，除非采用 KV Cache 量化 (如 FP8/INT8) 或分页注意力 (PagedAttention) 优化，但即使优化后，权重 54GB + 最小 KV Cache 仍可能超出 80GB 限制，需重新评估可行性。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B在BF16下权重约54GB，32K上下文KV Cache约33.55GB，加上激活开销总需求约92-97GB，确实超过A100 80GB单卡显存上限，结论合理。
