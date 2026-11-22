# N245: 在 vLLM 中，Prefill 阶段的激活内存并非简单地由 B * L * d_model * n_layers 决定，而是主要取决于 Attention 计

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N79

## Claim

在 vLLM 中，Prefill 阶段的激活内存并非简单地由 B * L * d_model * n_layers 决定，而是主要取决于 Attention 计算的中间结果（Q, K, V 矩阵）和 FFN 中间层；对于 FlashAttention 实现，激活内存峰值约为 B * L * d_model * 4 (Q,K,V,O) + B * L * d_ff * 2 (FFN)，其中 d_ff 为 FFN 中间维度（Qwen3-27B 约为 11008），而非 n_layers 线性累加。

## Corrected Claim

在 vLLM 中，Prefill 阶段的激活内存受 Attention 和 FFN 中间结果影响。FlashAttention 通过避免存储 Attention 分数矩阵（S）显著降低了 Attention 部分的显存占用，使其与序列长度 L 呈线性关系而非平方关系。然而，整体激活内存峰值仍受模型层数 n_layers 影响，因为需要存储各层的输入/输出及 FFN 中间激活值用于反向传播，并非完全独立于 n_layers。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 7 column 5 (char 789)

## Search Query

vLLM FlashAttention activation memory peak calculation
