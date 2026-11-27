# N649: H100 SXM 80GB 在 32K 上下文 BF16 推理下的有效 KV Cache 容量计算：总显存 80GB - BF16 权重 54GB - 框架/激

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N230

## Claim

H100 SXM 80GB 在 32K 上下文 BF16 推理下的有效 KV Cache 容量计算：总显存 80GB - BF16 权重 54GB - 框架/激活开销 2GB = 24GB 可用 KV Cache；基于 Qwen3-27B 单 token KV 256KB (N369)，最大并发请求数 = 24GB / 8GB = 3 个（与 A100 80GB 相同，但 H100 带宽更高，延迟更低）。

## Corrected Claim

H100 SXM 80GB 在 32K 上下文 BF16 推理下，若单请求 KV Cache 占用约为 8GB（基于特定模型架构假设），则最大并发请求数约为 3 个；实际并发数取决于模型具体的 KV Cache 大小（如是否采用 GQA/MQA 优化）。

## Evidence

[质询]数值量级与内部逻辑存在严重矛盾：1. 24GB 可用显存除以 8GB/请求，数学结果应为 3，但陈述中隐含的推导逻辑或对比基准可能存在混淆（通常 24/8=3 是整数，但需确认 8GB 是否准确对应 32K 上下文；若单请求 KV 为 256KB/token * 32K tokens = 8GB，则 24GB/8GB=3 在算术上成立，但需验证 256KB/token 对于 Qwen3-27B 是否准确。Qwen3-27B 若为 27B 参数，层数和头数决定 KV 大小。假设 27B 模型，KV cache 大小通常远小于 256KB/token 除非上下文极长或模型结构特殊。更关键的攻击点是：H100 SXM 80GB 的显存带宽和计算能力远高于 A100，虽然 KV 容量受显存限制可能相同（如果显存占用结构相似），但陈述中‘最大并发请求数 = 24GB / 8GB = 3 个’这一结论依赖于‘单请求占用 8GB’这一前提。若单请求 KV 实际远小于 8GB（例如 32K 上下文下，27B 模型 KV 可能仅为几 GB 或更少，取决于 GQA/MQA 结构），则并发数会被严重低估。此外，‘与 A100 80GB 相同’这一比较忽略了 H100 可能支持 FP8 或其他优化，或者 A100 的框架开销不同。最核心的逻辑漏洞在于：24GB / 8GB = 3 是算术正确的，但‘单请求 8GB’这一经验参数对于 32K 上下文的 27B 模型是否合理存疑。通常 27B 模型在 32K 上下文下的 KV Cache 不会高达 8GB（除非是纯 MHA 且无优化，但即使如此，27B 的 KV 大小通常在 1-4GB 范围，具体取决于层数和头数。例如，若 27B 有 40 层，每层 KV 大小取决于 hidden size 和 head count。若 hidden=4096, heads=32, kv_heads=32 (MHA), 则每 token KV = 2 * 40 * 32 * 4096 * 2 bytes (BF16) = 2 * 40 * 32 * 4096 * 2 = 20,971,520 bytes ≈ 20MB/token。32K tokens * 20MB = 640GB，这显然不对。重新计算：KV cache per token = 2 (K and V) * num_layers * num_kv_heads * head_dim * dtype_size. 假设 Qwen3-27B 类似 Llama 结构，num_layers=40, num_kv_heads=8 (GQA), head_dim=128. 则 per token = 2 * 40 * 8 * 128 * 2 bytes = 163,840 bytes ≈ 160KB/token. 32K tokens * 160KB = 5GB. 若 num_kv_heads=32 (MHA), 则 per token = 2 * 40 * 32 * 128 * 2 = 655,360 bytes ≈ 640KB/token. 32K * 640KB = 20GB. 因此，8GB 的估计可能偏低或偏高，取决于具体架构。但陈述中引用了 N369 的 256KB/token，若该引用准确，则 32K * 256KB = 8GB 是算术正确的。然而，256KB/token 对于 27B 模型来说是一个具体的经验值，若该值不准确，则结论错误。由于 source 为 knowledge，且无外部来源验证 N369 的准确性，且 256KB/token 这一数值对于 27B 模型在 32K 上下文下的合理性存在不确定性（可能因 GQA 而更小），故存在经验事实不准确的风险。 | 先验知识/题面给定，逻辑校验通过（算术 24/8=3 成立），但单请求 KV 大小 8GB 依赖于未验证的经验参数 N369，存在经验事实不准确的风险，故降级。
