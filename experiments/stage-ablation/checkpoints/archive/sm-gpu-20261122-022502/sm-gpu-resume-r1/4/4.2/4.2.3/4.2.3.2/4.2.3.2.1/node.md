# N820: 4x RTX 4090 运行 Qwen3-27B (FP16) 的显存可行性验证：总权重 54GB + 4x 48GB 显存 = 192GB 总量，单卡 48G

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N254, N255, N256

## Claim

4x RTX 4090 运行 Qwen3-27B (FP16) 的显存可行性验证：总权重 54GB + 4x 48GB 显存 = 192GB 总量，单卡 48GB 无法容纳 54GB 权重，需启用 Tensor Parallelism (TP=4) 或 Pipeline Parallelism。若 TP=4，每卡权重 13.5GB，KV Cache 每卡 3.145GB (32K ctx)，单卡剩余 31.355GB。结论：4x 4090 在 32K ctx 下显存充足，但 N254 中‘性能更低’的 claim 需修正为‘吞吐受限于 PCIe 瓶颈而非显存’。

## Corrected Claim

4x RTX 4090 (24GB) 运行 Qwen3-27B (FP16) 的显存可行性验证：总权重 54GB + 4x 24GB 显存 = 96GB 总量。若 TP=4，每卡权重 13.5GB，KV Cache 每卡 3.145GB (32K ctx)，单卡剩余约 7.355GB。结论：4x 4090 在 32K ctx 下显存极度紧张，可能因激活值溢出导致 OOM，需启用量化或减小 Batch Size；N254 中‘性能更低’的 claim 主要受限于 PCIe 瓶颈及显存带宽，而非单纯显存容量不足。

## Evidence

[质询]RTX 4090 的标准显存规格为 24GB，而非陈述中假设的 48GB。若按 24GB 计算，4 卡总显存 96GB，扣除 54GB 权重后仅剩 42GB 用于 KV Cache 和激活值，在 32K 上下文长度下，单卡 KV Cache 需求（约 3.1GB）虽可容纳，但剩余空间（约 17GB/卡）对于大模型推理的激活值（Activations）和临时缓冲区可能非常紧张，甚至不足，因此‘显存充足’的结论基于错误的硬件规格假设。 | 经验事实，逻辑自洽但缺来源支持；且核心硬件参数（RTX 4090 显存大小）与公认事实（24GB）不符，导致推导基础错误。

## Search Query

Qwen3-27B FP16 memory footprint 4x RTX 4090 tensor parallelism
