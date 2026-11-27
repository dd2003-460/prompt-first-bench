# N99: N23 中声称 A100 40GB SXM4 支持 FP8 峰值 624 TFLOPS 是错误的，修正自矛盾检测：A100 (Ampere) 架构不支持原生 F

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N23

## Claim

N23 中声称 A100 40GB SXM4 支持 FP8 峰值 624 TFLOPS 是错误的，修正自矛盾检测：A100 (Ampere) 架构不支持原生 FP8 计算，FP8 仅在 Hopper (H100/H200) 架构中引入，A100 的 FP8 性能应标记为 [不支持原生FP8]，其 INT8 1248 TOPS 为有效峰值。

## Corrected Claim

N23 中声称 A100 40GB SXM4 支持 FP8 峰值 624 TFLOPS 是错误的，修正自矛盾检测：A100 (Ampere) 架构不支持原生 FP8 计算，FP8 仅在 Hopper (H100/H200) 架构中引入，A100 的 FP8 性能应标记为 [不支持原生FP8]，其 INT8 1248 TOPS 为有效峰值。

## Evidence

先验知识/题面给定，逻辑校验通过：A100基于Ampere架构，确实不支持原生FP8（FP8由Hopper架构引入），其INT8峰值约为1248 TOPS，陈述符合硬件事实。

## Search Query

A100 FP8 support Ampere architecture
