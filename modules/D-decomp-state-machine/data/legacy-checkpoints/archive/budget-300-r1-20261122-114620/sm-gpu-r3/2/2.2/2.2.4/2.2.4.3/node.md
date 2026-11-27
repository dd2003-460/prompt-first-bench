# N200: ROCm 生态对 Qwen3-27B 的优化缺失主要体现为缺少针对 Qwen3 架构的 FlashAttention-2/3 原生内核优化，导致 Attenti

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N61

## Claim

ROCm 生态对 Qwen3-27B 的优化缺失主要体现为缺少针对 Qwen3 架构的 FlashAttention-2/3 原生内核优化，导致 Attention 计算效率比 CUDA 版本低约 20-30%，这是 MI250X 实测吞吐低于 H100 42% 的主要技术原因之一

## Corrected Claim

ROCm 生态对 Qwen3-27B 的优化存在不足，可能包括缺少针对 Qwen3 架构的高效 Attention 内核优化，导致 MI250X 实测吞吐低于 H100，但具体性能差距比例需以最新基准测试为准。

## Evidence

[质询]具体数值（20-30%效率差距、42%吞吐差距）及归因（FlashAttention内核缺失为主要原因）属于特定硬件与模型组合下的经验性实测数据，缺乏公开权威基准测试的直接支持，且不同优化策略下差距可能波动。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，无法验证具体百分比及归因准确性）

## Search Query

ROCm Qwen3 27B FlashAttention performance gap vs CUDA
