# N96: RTX 4090 运行 14.57 GB 负载时的实际内存带宽利用率约为 75-85%（受限于 L2 缓存命中率和 PCIe 延迟），因此实际推理速度上限为 6

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N20

## Claim

RTX 4090 运行 14.57 GB 负载时的实际内存带宽利用率约为 75-85%（受限于 L2 缓存命中率和 PCIe 延迟），因此实际推理速度上限为 69.2 * 0.8 ≈ 55.4 tokens/s，而非理论峰值 69.2 tokens/s。

## Corrected Claim

RTX 4090 在运行大模型推理时，实际内存带宽利用率通常低于 100%（受限于 L2 缓存命中率和 PCIe 延迟），因此实际推理速度通常低于基于理论峰值带宽计算的上限。

## Evidence

[质询]该陈述包含具体的经验性数值（75-85% 利用率、55.4 tokens/s），这些数值高度依赖于具体的模型架构、序列长度、Batch Size 以及硬件驱动状态，并非 RTX 4090 的固定物理属性或第一性原理可推导的常数。此外，'14.57 GB 负载' 这一特定数值缺乏上下文，无法验证其合理性。 | source=knowledge，逻辑上带宽利用率受限于缓存和延迟是合理的，但具体数值（75-85%）属于经验事实，缺乏通用性，且无外部来源支持，故降级为定性表述。

## Search Query

RTX 4090 LLM inference memory bandwidth utilization efficiency
