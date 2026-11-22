# N614: Qwen3-27B 在 INT4 量化下的模型文件大小约为 14.5 GB（27B * 0.5 bytes），在 M2 Ultra 80GB 统一内存中，扣除系

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N188, N189, N190

## Claim

Qwen3-27B 在 INT4 量化下的模型文件大小约为 14.5 GB（27B * 0.5 bytes），在 M2 Ultra 80GB 统一内存中，扣除系统开销（约 10-15 GB）后，剩余可用内存约 60-65 GB，足以容纳模型权重及 32K 上下文所需的 KV Cache（32K tokens * 27B layers * hidden_dim * 2 bytes ≈ 10-15 GB），因此容量约束非瓶颈，瓶颈完全在于计算/带宽。

## Corrected Claim

Qwen3-27B 在 INT4 量化下模型文件大小约为 14.5 GB。在 M2 Ultra 80GB 统一内存中，扣除系统开销后剩余约 60-65 GB。KV Cache 大小取决于层数（约 64 层）、头数及隐藏维度，32K 上下文下的 KV Cache 通常在几 GB 到十几 GB 之间（具体取决于精度和架构细节），总内存需求远低于可用内存，因此容量约束非瓶颈，瓶颈在于计算/带宽。

## Evidence

[质询]KV Cache 估算公式存在严重逻辑错误：公式中错误地引入了 '27B layers'（参数量）作为层数，实际上 Qwen3-27B 的层数约为 64 层，而非 270 亿层。此外，KV Cache 大小与 hidden_dim 和 num_heads 相关，而非直接乘以总参数量。虽然最终结论（容量非瓶颈）可能正确，但推导过程中的数值量级和逻辑存在硬伤。 | 先验知识/题面给定，但逻辑校验发现 KV Cache 计算公式错误（混淆了参数量与层数），导致推导过程不成立，尽管最终定性结论（内存充足）在工程经验上大致合理，但具体数值推导不可信。

## Search Query

Qwen3-27B INT4 file size KV cache memory requirement 32k context
