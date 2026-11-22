# N328: L40S 在 BF16 精度下运行 Qwen3-27B 的实测 Decode 吞吐量基准值为 30 tokens/s，误差范围 ±5%，基于 vLLM 0.4.

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

L40S 在 BF16 精度下运行 Qwen3-27B 的实测 Decode 吞吐量基准值为 30 tokens/s，误差范围 ±5%，基于 vLLM 0.4.1 版本及 CUDA 12.1 环境

## Corrected Claim

L40S 在 BF16 精度下运行 Qwen3-27B 的 Decode 吞吐量约为 30 tokens/s（基于 vLLM 0.4.1 及 CUDA 12.1 环境的估算/未验证基准）

## Evidence

[质询]该陈述包含具体的硬件型号（L40S）、软件版本（vLLM 0.4.1）、CUDA版本及精确的性能基准值（30 tokens/s ±5%），属于典型的经验事实。由于缺乏任何外部来源支持，且无法通过第一性原理推导出具体的吞吐量数值，存在数值不准确或环境配置偏差的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

L40S Qwen3-27B BF16 vLLM throughput tokens/s benchmark
