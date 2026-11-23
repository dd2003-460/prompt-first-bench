# N97: Prefill 阶段带宽影响：Prefill 阶段为计算密集型（Compute-Bound），其延迟主要由 FLOPS 决定而非带宽，但长上下文（32K）Pre

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N26, N27, N28

## Claim

Prefill 阶段带宽影响：Prefill 阶段为计算密集型（Compute-Bound），其延迟主要由 FLOPS 决定而非带宽，但长上下文（32K）Prefill 的中间激活值读写可能受带宽瓶颈影响，需单独估算 Prefill_Latency = (2 * Num_Parameters * Seq_Len) / (Peak_FLOPS * η_compute)。

## Corrected Claim

Prefill 阶段带宽影响：Prefill 阶段为计算密集型（Compute-Bound），其延迟主要由 FLOPS 决定而非带宽，但长上下文（32K）Prefill 的中间激活值读写可能受带宽瓶颈影响，需单独估算 Prefill_Latency = (2 * Num_Parameters * Seq_Len) / (Peak_FLOPS * η_compute)。

## Evidence

先验知识/题面给定，逻辑校验通过：Prefill 阶段确实为计算密集型，延迟公式符合大模型推理的基本算术强度推导。
