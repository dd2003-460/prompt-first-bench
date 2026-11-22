# N222: 激活值 (Activation) 显存占用的精确计算：激活值大小 = batch_size * seq_len * hidden_size * num_acti

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N101

## Claim

激活值 (Activation) 显存占用的精确计算：激活值大小 = batch_size * seq_len * hidden_size * num_active_layers * bytes_per_element。对于 Qwen3-27B (hidden=4096, batch=1, seq=32768, BF16)，峰值激活占用约为 1.3GB (32768 * 4096 * 2 bytes)，而非 N131 中估算的 2.5GB；需修正总显存预算中的激活项，从而重新计算 RTX 5090 的可行性余量。

## Corrected Claim

在特定推理优化策略下（如启用 FlashAttention 且仅计算核心线性层激活），Qwen3-27B (hidden=4096, batch=1, seq=32768, BF16) 的核心激活占用约为 1.3GB (32768 * 4096 * 2 bytes)，但总显存占用还需包含 KV Cache 及中间层激活，具体数值取决于推理引擎实现。

## Evidence

[质询]激活值显存占用并非仅由 batch_size * seq_len * hidden_size 决定，而是强烈依赖于推理引擎的优化策略（如 FlashAttention 是否启用、是否使用 KV Cache 分离、是否进行激活重计算等）。在标准 Transformer 推理中，若未使用 FlashAttention，中间激活值（如 Attention 矩阵）可能高达 O(N^2) 量级，远超 1.3GB；若使用 FlashAttention，则主要占用为 KV Cache 和当前层激活，数值会显著低于 1.3GB。该陈述将复杂的工程实现简化为单一公式，且未说明具体推理框架假设，导致数值缺乏普适性。 | 先验知识/题面给定，逻辑校验通过。虽然公式简化了实际推理中的激活存储机制（忽略了 KV Cache 和中间层激活的复杂分布），但在特定假设下（如仅计算单层线性层激活且忽略 KV Cache 或假设其不计入此特定项）量级合理。由于缺乏外部来源支持具体推理框架下的精确数值，且该数值高度依赖工程实现细节，故降级为定性表述。

## Search Query

Transformer activation memory calculation formula batch size sequence length hidden size
