# N218: vLLM 0.5.x 与 llama.cpp b4000+ 在 RTX 4090 上运行 Qwen3-27B FP8 的吞吐量差异约为 15-25% (vLLM

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N87

## Claim

vLLM 0.5.x 与 llama.cpp b4000+ 在 RTX 4090 上运行 Qwen3-27B FP8 的吞吐量差异约为 15-25% (vLLM 通常更高)，主要源于 vLLM 的 PagedAttention 优化及 CUDA Graph 捕获效率；若使用 llama.cpp，需额外启用 --mlock 和 --threads 参数以匹配 vLLM 性能，否则吞吐量下降 > 30%。

## Corrected Claim

vLLM 0.5.x 与 llama.cpp b4000+ 在 RTX 4090 上运行 Qwen3-27B FP8 时，vLLM 通常具有更高的吞吐量，主要得益于 PagedAttention 优化及 CUDA Graph 捕获效率；若使用 llama.cpp，需合理配置线程数及内存锁定参数以优化性能，否则可能显著落后于 vLLM。

## Evidence

[质询]具体数值区间（15-25%、>30%）及特定参数组合（--mlock/--threads）缺乏通用基准测试支持，属于高度依赖具体配置的经验性断言，易受上下文长度、批处理大小等变量影响，存在以偏概全风险。 | 先验知识/题面给定，逻辑校验通过：vLLM 的 PagedAttention 和 CUDA Graph 确为性能优势来源，llama.cpp 需调优参数以匹配性能符合工程直觉，但具体百分比差异缺乏通用基准支持，故降级为定性表述。
