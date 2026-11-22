# N29: RTX 4090 单卡在 FP8 量化下运行 Qwen3-27B 32K 上下文的显存占用为 27GB(权重) + 9GB(KV Cache) + 2GB(激活

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

RTX 4090 单卡在 FP8 量化下运行 Qwen3-27B 32K 上下文的显存占用为 27GB(权重) + 9GB(KV Cache) + 2GB(激活/框架) ≈ 38GB，大于 24GB 物理显存，必须启用 CPU Offload 或降低上下文长度至 ~15K tokens

## Corrected Claim

RTX 4090 单卡在 FP8 量化下运行 Qwen3-27B 32K 上下文的显存占用为 27GB(权重) + 9GB(KV Cache) + 2GB(激活/框架) ≈ 38GB，大于 24GB 物理显存，必须启用 CPU Offload 或降低上下文长度至 ~15K tokens

## Evidence

[质询]KV Cache 9GB 的估算可能偏高（取决于具体实现如 FlashAttention 或 PagedAttention 的优化程度，实际可能更低），但即使 KV Cache 降至 5GB，总显存仍远超 24GB，核心结论（必须 Offload 或降上下文）不变。 | 先验知识/题面给定，逻辑校验通过：Qwen3-27B 在 FP8 下权重约 27GB，已超出 24GB 显存，加上 KV Cache 和激活值，总占用必然远超 24GB，结论成立。
