# N125: 带宽瓶颈的边界条件：当 seq_len < 4K 时，Prefill 阶段是 Compute-Bound，带宽不再是主导因素；当 seq_len > 32K 时

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

带宽瓶颈的边界条件：当 seq_len < 4K 时，Prefill 阶段是 Compute-Bound，带宽不再是主导因素；当 seq_len > 32K 时，KV Cache 大小超过 L2 缓存 (RTX 4090: 72MB, RTX 3090: 60MB)，导致频繁内存访问，实际吞吐可能低于理论值 30-50% [待核验：需查 LLM 推理中 L2 缓存命中率对吞吐的影响]

## Corrected Claim

带宽瓶颈的边界条件：通常当 seq_len 较短（如 < 4K）时，Prefill 阶段倾向于 Compute-Bound；当 seq_len 较长（如 > 32K）且模型规模较大时，KV Cache 可能超过 L2 缓存容量（如 RTX 4090 的 72MB），导致内存带宽成为瓶颈，实际吞吐可能显著低于理论峰值。具体阈值和性能损失比例取决于模型架构、Batch Size 及硬件配置。

## Evidence

[质询]具体阈值（4K/32K）和性能损失比例（30-50%）高度依赖于模型架构（如注意力头数、隐藏层维度）、硬件具体配置及软件栈优化，并非普适的物理常数；此外，RTX 4090 的 L2 缓存大小通常被引用为 72MB，但不同批次或具体 SKU 可能存在差异，且 KV Cache 是否完全溢出 L2 还取决于 Batch Size 和 Precision，直接断言 'seq_len > 32K 时 KV Cache 大小超过 L2' 忽略了 Batch Size 为 1 时的具体计算细节（例如 Llama-2 70B 在 32K 长度下 KV Cache 远超 72MB，但 Llama-2 7B 则远小于 72MB，因此该陈述隐含了特定大模型假设但未明示）。 | 先验知识/题面给定，逻辑校验通过。虽然逻辑自洽（长序列确实导致 KV Cache 增大并可能溢出 L2，短序列 Prefill 确实计算密集），但具体的数值阈值（4K, 32K）和性能损失幅度（30-50%）属于经验性工程参数，且缺乏针对特定模型和硬件组合的通用性证明，故降级为定性表述。

## Search Query

LLM inference L2 cache hit rate long context performance
