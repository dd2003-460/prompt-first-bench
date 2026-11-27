# N349: 2×RTX 4090 W4 精度下 Decode 阶段的理论峰值吞吐为 2 * (1008 GB/s / 13.5 GB) ≈ 149 Tokens/s (理想

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N125

## Claim

2×RTX 4090 W4 精度下 Decode 阶段的理论峰值吞吐为 2 * (1008 GB/s / 13.5 GB) ≈ 149 Tokens/s (理想线性扩展)，若实测为 25-30 Tokens/s，则并行效率损耗高达 80-83%，主要归因于 W4 量化算子在 CUDA 内核中的非原生支持导致的计算利用率低下及 PCIe 同步延迟，而非单纯的带宽限制。

## Corrected Claim

2×RTX 4090 W4 精度下 Decode 阶段的理论峰值吞吐约为 149 Tokens/s (基于 1008 GB/s 带宽和 13.5 GB 模型大小估算)。若实测为 25-30 Tokens/s，则并行效率损耗高达 80-83%。此损耗可能归因于 W4 量化算子的计算效率、PCIe 同步延迟及内存访问模式等多种因素，而非单一原因。

## Evidence

[质询]该陈述包含具体的硬件性能参数（RTX 4090带宽、W4模型大小）及特定的性能损耗归因（CUDA内核非原生支持 vs PCIe延迟），属于经验事实。虽然逻辑推导（149 vs 25-30 -> 80%+损耗）在数学上自洽，但缺乏外部来源支持其具体的数值前提和归因结论，且'非原生支持'这一归因可能过于绝对（现代CUDA生态对W4已有较好支持，瓶颈可能更复杂）。 | 经验事实，逻辑自洽但缺来源支持。数学计算 2*(1008/13.5)≈149 正确，效率损耗 (149-27.5)/149≈81% 计算正确，但具体硬件参数和归因无来源验证。

## Search Query

RTX 4090 W4 quantization tensor parallelism efficiency loss llama.cpp vLLM
