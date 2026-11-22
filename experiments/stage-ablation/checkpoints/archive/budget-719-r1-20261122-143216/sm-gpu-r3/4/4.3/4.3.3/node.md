# N108: Qwen3-27B 在 32K 上下文下的激活值缓冲显存占用量，基于 vLLM 框架的 PagedAttention 优化，预期占用量在 1-2 GB 之间

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N23

## Claim

Qwen3-27B 在 32K 上下文下的激活值缓冲显存占用量，基于 vLLM 框架的 PagedAttention 优化，预期占用量在 1-2 GB 之间

## Corrected Claim

Qwen3-27B 在 32K 上下文下，基于 vLLM 框架的 PagedAttention 优化，其 KV Cache 及激活值显存占用量取决于并发数和精度，单请求 KV Cache 占用通常在数百 MB 至 1GB 级别，整体缓冲显存占用需结合具体负载评估。

## Evidence

[质询]数值量级存疑：对于 27B 参数的模型，即使使用 PagedAttention，KV Cache 的显存占用通常与上下文长度和 Batch Size 强相关。在 32K 上下文下，单个请求的 KV Cache 占用可能接近或超过 1GB（取决于层数、头数、head_dim 和精度），若涉及多并发或激活值（Activations）本身，1-2GB 的估计可能偏低或偏高，且‘激活值缓冲’与‘KV Cache’概念易混淆，缺乏具体 Batch Size 和精度假设，导致数值缺乏严谨性。 | source=knowledge，逻辑上 PagedAttention 确实优化了显存碎片，但 1-2GB 的具体数值依赖于未给出的 Batch Size 和精度参数，属于经验估算，缺乏直接来源支持，故降级。
