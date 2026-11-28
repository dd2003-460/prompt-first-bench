# N488: 工作点 B (Mid Perf/Mid Cost): 保持 NVFP4 权重但启用 FlashAttention-2 和 PagedAttention，利用 F

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N174

## Claim

工作点 B (Mid Perf/Mid Cost): 保持 NVFP4 权重但启用 FlashAttention-2 和 PagedAttention，利用 FP16 计算。显存占用同 A (因权重反量化后驻留显存为 FP16)，但通过优化 Kernel Launch 减少 Overhead，实际 Decode 速度提升至 12-15 tok/s，Prefill 吞吐量提升 15% 相比朴素 FP16

## Corrected Claim

工作点 B (Mid Perf/Mid Cost): 保持 NVFP4 权重但启用 FlashAttention-2 和 PagedAttention，利用 FP16 计算。显存占用同 A (因权重反量化后驻留显存为 FP16)，但通过优化 Kernel Launch 减少 Overhead，实际 Decode 速度和 Prefill 吞吐量相比朴素 FP16 有显著提升。

## Evidence

[质询]具体性能数值（12-15 tok/s, 15%提升）缺乏来源支持，且不同硬件配置下数值差异巨大，无法从第一性原理推导具体经验值。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM PagedAttention V100 decode speed optimization FP16
