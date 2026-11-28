# N39: V100-SXM2 的 HBM2 显存带宽为 900 GB/s，而 A100/H100 分别为 1.5 TB/s 和 3.35 TB/s；在 FP8/FP16 

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N6, N7, N8

## Claim

V100-SXM2 的 HBM2 显存带宽为 900 GB/s，而 A100/H100 分别为 1.5 TB/s 和 3.35 TB/s；在 FP8/FP16 模拟推理中，Memory-Bound 操作的延迟与带宽成反比，V100 的理论峰值吞吐仅为 A100 的 60%

## Corrected Claim

V100-SXM2 的 HBM2 显存带宽为 900 GB/s，而 A100/H100 分别为 1.5 TB/s 和 3.35 TB/s；在 Memory-Bound 操作中，延迟与带宽成反比，V100 的显存带宽仅为 A100 的 60%，但受限于计算能力和缺乏原生 FP8 支持，其实际推理吞吐远低于此比例。

## Evidence

[质询]陈述中关于V100与A100在FP8/FP16模拟推理下理论峰值吞吐比为60%的结论缺乏严谨推导。虽然HBM2带宽（900GB/s vs 1.5TB/s）确实约为60%，但实际推理吞吐受计算能力（FLOPS）、内存容量及架构特性共同影响。V100不支持原生FP8，需软件模拟，其计算效率远低于A100的原生FP8支持，导致实际或理论峰值吞吐比通常远低于60%（往往接近10%-20%甚至更低，取决于具体算子）。将带宽比直接等同于吞吐比忽略了计算瓶颈和精度支持差异，属于过度简化。 | 先验知识/题面给定，逻辑校验发现内部矛盾：带宽比不等于吞吐比，且V100无原生FP8支持，直接断言吞吐为A100的60%违背硬件架构常识。

## Search Query

V100 SXM2 memory bandwidth GB/s vs A100 H100
