# N317: llama.cpp 在 RTX 4090 上运行 Qwen3-27B (BF16) 时，若未启用 CUDA Graph 或 Batch Size=1 的特定优化

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113, N114, N115

## Claim

llama.cpp 在 RTX 4090 上运行 Qwen3-27B (BF16) 时，若未启用 CUDA Graph 或 Batch Size=1 的特定优化路径，其 CPU-GPU 同步开销（CPU-GPU Sync Overhead）约占 Decode 总时间的 8%-12%，而 vLLM 通过异步调度将此比例降至 <2%，这是两者在消费卡上性能差距的主要构成部分之一。

## Corrected Claim

llama.cpp 在 RTX 4090 上运行 Qwen3-27B (BF16) 时，若未启用特定优化，CPU-GPU 同步开销会显著影响 Decode 性能；vLLM 通过异步调度优化了此部分开销，从而在消费级显卡上展现出更好的吞吐性能。

## Evidence

[质询]具体数值（8%-12% vs <2%）缺乏公开基准测试支持，且将性能差距主要归因于同步开销可能忽略了算子融合、内存带宽利用率等其他关键因素，存在过度归因风险。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源）

## Search Query

llama.cpp CPU GPU sync overhead vs vLLM async scheduling decode latency breakdown
