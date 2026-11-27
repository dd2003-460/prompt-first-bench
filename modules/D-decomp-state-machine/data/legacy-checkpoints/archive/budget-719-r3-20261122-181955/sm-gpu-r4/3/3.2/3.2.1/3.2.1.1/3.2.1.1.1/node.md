# N790: 工作点 1 (高性低成 - vLLM + CUDA Graphs)：在 vLLM 框架下启用 CUDA Graphs 和 PagedAttention，CPU-

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N282

## Claim

工作点 1 (高性低成 - vLLM + CUDA Graphs)：在 vLLM 框架下启用 CUDA Graphs 和 PagedAttention，CPU-GPU 数据拷贝时间优化至 ~2ms (通过 Pin Memory)，调度器延迟降至 ~0.5ms，框架初始化开销摊销后忽略不计；总 Latency_overhead ≈ 2.5ms。此配置下，TTFT 主要受 Prefill 计算时间支配，开销占比 < 2% (假设 Prefill 300ms)。

## Corrected Claim

工作点 1 (高性低成 - vLLM + CUDA Graphs)：在 vLLM 框架下启用 CUDA Graphs 和 PagedAttention，通过 Pin Memory 优化 CPU-GPU 数据拷贝时间，降低调度器延迟，框架初始化开销摊销后忽略不计；总 Latency_overhead 显著降低。此配置下，TTFT 主要受 Prefill 计算时间支配，开销占比极低。

## Evidence

[质询]具体数值（如2ms, 0.5ms, 2.5ms）属于特定硬件和负载下的经验测量值，无法从第一性原理推导，且缺乏来源支持其准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM CUDA Graphs latency overhead CPU GPU copy time benchmark ms
