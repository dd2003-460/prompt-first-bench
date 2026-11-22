# N277: Apple Silicon 统一内存架构在 Decode 阶段存在 '内存控制器仲裁延迟'，其固定开销约为 0.5-1.0 ms/token，导致实际吞吐量比理

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N123

## Claim

Apple Silicon 统一内存架构在 Decode 阶段存在 '内存控制器仲裁延迟'，其固定开销约为 0.5-1.0 ms/token，导致实际吞吐量比理论峰值低 5-10%，即 13.7 * 0.92 ≈ 12.6 tokens/s，这与 N123 声称的 13-14 tokens/s 区间下界吻合

## Corrected Claim

Apple Silicon 统一内存架构在 Decode 阶段存在内存访问与调度相关的性能开销，导致实际吞吐量低于理论峰值，具体损失比例取决于模型规模与硬件配置，通常表现为一定程度的性能折损。

## Evidence

[质询]该陈述包含具体的经验性数值（0.5-1.0 ms/token 的固定开销、5-10% 的吞吐量损失），这些并非 Apple Silicon 架构的通用物理定律或第一性原理可推导的必然结果，而是依赖于具体模型大小、内存带宽利用率及调度策略的经验观测值。此外，将‘内存控制器仲裁延迟’直接量化为固定的 ms/token 开销并归因为唯一导致 5-10% 损失的原因，缺乏通用性，属于过度具体的经验断言。 | 来源 [1] 讨论了 Apple Silicon 统一内存上 CPU+GPU 协同执行在 Decode 阶段的机制与边界，间接支持了存在性能瓶颈的事实，但未提供具体的 0.5-1.0 ms/token 延迟数值或 5-10% 的具体损失比例；来源 [2] 仅介绍 Apple Silicon 概况，无相关性能数据。因缺乏直接数值支持，且该数值属于经验事实，故降级。

## Search Query

Apple Silicon unified memory decode latency overhead LLM inference

## Retrieval Sources

- {'url': 'https://arxiv.org/abs/2607.22785&rut=4e78971332f7c64545b8ae6d09a1ae8c118b8c376988c9f9650de20768b3d837', 'type': 'ddg', 'title': '[2607.22785] FusionML: Prefill, Not Decode - Mechanism and Boundaries ...'}
- {'url': 'https://en.wikipedia.org/wiki/Apple_silicon&rut=a5e0ce8543f123304745eecf1ef89c84b0c40abe923c0ee4def86c55ee8ab658', 'type': 'ddg', 'title': 'Apple silicon - Wikipedia'}
