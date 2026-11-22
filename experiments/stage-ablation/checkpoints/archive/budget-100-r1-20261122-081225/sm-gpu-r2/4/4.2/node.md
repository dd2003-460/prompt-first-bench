# N41: 在 32K 上下文、W4A8 量化下，Qwen3-27B 的 KV Cache 显存占用为 13.82 GB（计算式：13.82 = 27.65 × 0.5），

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4, N5

## Claim

在 32K 上下文、W4A8 量化下，Qwen3-27B 的 KV Cache 显存占用为 13.82 GB（计算式：13.82 = 27.65 × 0.5），加上权重 13.5 GB，总显存需求为 27.32 GB。

## Corrected Claim

在 32K 上下文、W4A8 量化下，Qwen3-27B 的 KV Cache 显存占用为 13.82 GB（计算式：13.82 = 27.65 × 0.5），加上权重 13.5 GB，总显存需求为 27.32 GB。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache 占用 13.82 GB 与权重 13.5 GB 相加等于 27.32 GB，算术自洽；W4A8 量化下权重体积约为 FP16 的 1/4，27B 模型权重 13.5 GB 符合量级预期（27B * 0.5 bytes ≈ 13.5 GB），KV Cache 占用 13.82 GB 在 32K 上下文下亦属合理范围。
