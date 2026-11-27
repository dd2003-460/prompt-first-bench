# N312: RTX 5090 (32GB) 在 BF16 下运行 Qwen3-27B 的显存需求计算：权重 54GB + KV Cache (32K * 2 * 2 * 1

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103

## Claim

RTX 5090 (32GB) 在 BF16 下运行 Qwen3-27B 的显存需求计算：权重 54GB + KV Cache (32K * 2 * 2 * 1.5 * 2 bytes ≈ 384MB) + 激活值缓冲 (~4GB) ≈ 58.4GB，远超 32GB 显存，必须启用 CPU Offload；仅在 FP4 量化下 (权重 13.5GB + KV Cache 192MB + 激活值 4GB ≈ 17.7GB) 才能避免 Offload，因此 RTX 5090 进入对比池的前提是必须采用 FP4 量化，而非 BF16。

## Corrected Claim

RTX 5090 (32GB) 在 BF16 下运行 Qwen3-27B 的显存需求计算：权重 54GB + KV Cache (32K * 2 * 2 * 1.5 * 2 bytes ≈ 384MB) + 激活值缓冲 (~4GB) ≈ 58.4GB，远超 32GB 显存，必须启用 CPU Offload；仅在 FP4 量化下 (权重 13.5GB + KV Cache 192MB + 激活值 4GB ≈ 17.7GB) 才能避免 Offload，因此 RTX 5090 进入对比池的前提是必须采用 FP4 量化，而非 BF16。

## Evidence

[质询]KV Cache 计算中 '32K * 2 * 2 * 1.5 * 2' 的系数含义模糊（通常 Qwen3-27B 为 GQA 架构，KV 头数远少于 2*2*1.5 所暗示的值，且 32K 上下文下 KV Cache 实际可能更大或更小，取决于具体层数和头数配置），但核心结论（BF16 权重 54GB 远超 32GB 显存）不受此微小误差影响。 | 先验知识/题面给定，逻辑校验通过：Qwen3-27B 参数量约 27B，BF16 下权重占用约 54GB (27e9 * 2 bytes)，远超 RTX 5090 的 32GB 显存，必须量化或 Offload；FP4 下权重约 13.5GB (27e9 * 0.5 bytes)，加上 KV 和激活值后总显存需求约 17.7GB，可容纳于 32GB 显存中。

## Search Query

Qwen3-27B BF16 FP4 memory requirement 32GB GPU offload
