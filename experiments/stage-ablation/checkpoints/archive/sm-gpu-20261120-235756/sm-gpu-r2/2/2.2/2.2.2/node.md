# N59: MoE 架构下有效权重读取量 = (N_experts × bits_per_weight / 8) × (N_active_experts / N_total

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N14

## Claim

MoE 架构下有效权重读取量 = (N_experts × bits_per_weight / 8) × (N_active_experts / N_total_experts)，对于 Qwen3-27B (3.3B active params)，在 BF16 下有效权重读取量约为 6.6 GB/token，而非全量 54.36 GB，显著降低对带宽的需求。

## Corrected Claim

MoE 架构下有效权重读取量 = (N_experts × bits_per_weight / 8) × (N_active_experts / N_total_experts)，对于 Qwen3-27B (3.3B active params)，在 BF16 下有效权重读取量约为 6.6 GB/token，而非全量 54.36 GB，显著降低对带宽的需求。

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B总参数量约27B，BF16下全量权重约54GB；激活参数3.3B，对应权重约6.6GB，计算逻辑自洽且符合MoE稀疏激活原理。

## Search Query

Qwen3-27B MoE active parameters inference memory bandwidth
