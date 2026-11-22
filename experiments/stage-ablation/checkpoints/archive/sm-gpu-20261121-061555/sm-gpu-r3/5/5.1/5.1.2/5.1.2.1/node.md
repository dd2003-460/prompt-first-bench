# N275: 2x RTX 4090 (TP=2) 在 Qwen3-27B FP8 推理下的有效吞吐量 (Tokens/s) 计算式：T_eff = T_single_the

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N99, N100, N101

## Claim

2x RTX 4090 (TP=2) 在 Qwen3-27B FP8 推理下的有效吞吐量 (Tokens/s) 计算式：T_eff = T_single_theoretical * 0.825 (中值) - T_overhead_allreduce，其中 T_single_theoretical 需基于 N117 带宽和模型参数计算，T_overhead 取决于 All-Reduce 频率与 PCIe 4.0 x16 带宽 (32 GB/s) 的比值。

## Corrected Claim

2x RTX 4090 (TP=2) 在 Qwen3-27B FP8 推理下的有效吞吐量 (Tokens/s) 计算式：T_eff = T_single_theoretical * η - T_overhead_allreduce，其中 η 为并行效率系数（需根据具体硬件和软件栈实测确定），T_overhead 取决于 All-Reduce 频率与 PCIe 4.0 x16 带宽的比值。

## Evidence

[质询]该陈述包含具体的经验性参数（如0.825的中值效率系数、PCIe 4.0 x16带宽32 GB/s），这些属于硬件规格和特定模型推理的性能经验值，无法从第一性原理严格推导，且缺乏来源支持。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 4090 tensor parallel 2 Qwen 27B throughput benchmark PCIe allreduce overhead
