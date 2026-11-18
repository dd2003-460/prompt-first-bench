# N20: 关键性能指标定义：Tokens/second (生成速度), Time-to-first-token (TTFT), 显存带宽 (GB/s), 计算吞吐量 (T

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N4

## Claim

关键性能指标定义：Tokens/second (生成速度), Time-to-first-token (TTFT), 显存带宽 (GB/s), 计算吞吐量 (TFLOPS)；对于 27B 模型，显存带宽通常是瓶颈而非计算能力，因此 HBM/DDR 带宽比 FLOPS 更重要

## Corrected Claim

关键性能指标定义：Tokens/second (生成速度), Time-to-first-token (TTFT), 显存带宽 (GB/s), 计算吞吐量 (TFLOPS)；对于 27B 模型，显存带宽通常是瓶颈而非计算能力，因此 HBM/DDR 带宽比 FLOPS 更重要

## Evidence

先验知识/题面给定，逻辑校验通过：对于27B参数量的大语言模型，推理阶段（尤其是自回归生成）主要受限于显存带宽（Memory-Bandwidth Bound），而非计算能力（Compute-Bound），因此HBM/DDR带宽比FLOPS更关键，符合硬件架构基本原理。

## Search Query

LLM inference bottleneck memory bandwidth vs compute
