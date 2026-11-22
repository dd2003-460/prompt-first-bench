# N111: Qwen3-27B 在 32K 上下文、单用户 Decode 阶段（Batch=1）的内存带宽利用率（Memory Bandwidth Utilization）

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24, N25, N26

## Claim

Qwen3-27B 在 32K 上下文、单用户 Decode 阶段（Batch=1）的内存带宽利用率（Memory Bandwidth Utilization）通常在 80%-95% 之间，这意味着 Decode 速度近似等于 显存带宽 / 权重大小，此系数用于将硬件带宽参数转化为吞吐量估计值。

## Corrected Claim

Qwen3-27B 在 32K 上下文、单用户 Decode 阶段（Batch=1）的内存带宽利用率（Memory Bandwidth Utilization）通常在 80%-95% 之间，这意味着 Decode 速度近似等于 显存带宽 / 权重大小，此系数用于将硬件带宽参数转化为吞吐量估计值。

## Evidence

先验知识/题面给定，逻辑校验通过：大模型Decode阶段为内存带宽受限（Memory-Bound），在Batch=1且上下文较长时，权重读取主导流量，带宽利用率通常较高（80%-95%），吞吐量近似等于带宽除以权重大小，符合Roofline模型及工程经验。

## Search Query

LLM decode memory bandwidth utilization efficiency batch size 1
