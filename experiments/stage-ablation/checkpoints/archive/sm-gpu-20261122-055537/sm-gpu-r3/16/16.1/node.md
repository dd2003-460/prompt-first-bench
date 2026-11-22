# N403: P99 延迟与显存带宽的非线性关系模型：在 LLM 解码阶段，P99 延迟主要由 KV Cache 读取时间决定。若带宽 B < 500 GB/s，且 KV C

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N127

## Claim

P99 延迟与显存带宽的非线性关系模型：在 LLM 解码阶段，P99 延迟主要由 KV Cache 读取时间决定。若带宽 B < 500 GB/s，且 KV Cache 大小 S > 10GB，则单 token 延迟 T > S/B。例如，L4 (336 GB/s) 在 32K 上下文下 KV Cache 约 10GB，单 token 延迟 > 10/0.336 ≈ 29.7ms，若 batch_size=1，P99 延迟可能因内存碎片和调度开销超过 500ms，若并发>4，排队延迟将指数级增长，导致 P99 > 2s。

## Corrected Claim

在 LLM 解码阶段，P99 延迟受 KV Cache 读取时间显著影响。若带宽 B < 500 GB/s 且 KV Cache 大小 S > 10GB，单 token 理论最小延迟 T_min ≈ S/B（例如 L4 336 GB/s 下约 30ms）。实际 P99 延迟会因内存碎片、调度开销及并发排队效应显著高于此下限，在高并发场景下可能达到数百毫秒甚至秒级，但具体数值取决于系统实现与负载模型，不宜断言为严格的指数级增长。

## Evidence

[质询]陈述中关于并发>4时P99延迟“指数级增长”且“>2s”的断言缺乏严谨的排队论支持，通常在高并发下延迟随负载呈线性或超线性增长，而非严格的指数级；此外，L4 GPU在32K上下文下KV Cache是否精确为10GB取决于具体模型架构（如层数、头数、精度），该数值为经验估算而非绝对事实。 | source=knowledge，逻辑校验通过：单token延迟下限 S/B 计算正确（10GB/336GB/s ≈ 29.7ms），符合物理直觉；但并发下的具体延迟数值（>2s）及“指数级”描述属于经验性推断，缺乏第一性原理严格推导，故降级为定性表述。

## Search Query

LLM inference latency bandwidth bound KV cache size
