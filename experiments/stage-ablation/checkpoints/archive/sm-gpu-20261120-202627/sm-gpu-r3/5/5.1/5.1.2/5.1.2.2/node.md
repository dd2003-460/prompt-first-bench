# N371: 2× RTX 4090 在持续高负载下的实际负载因子 (Load_Factor) 修正：由于 LLM 推理包含计算密集的 Prefill 阶段和带宽密集的 De

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N117

## Claim

2× RTX 4090 在持续高负载下的实际负载因子 (Load_Factor) 修正：由于 LLM 推理包含计算密集的 Prefill 阶段和带宽密集的 Decode 阶段，平均功耗通常低于峰值 TDP，典型 Load_Factor 范围 [0.8, 0.95]，需根据 Batch Size 和上下文长度分布进行加权平均计算。

## Corrected Claim

2× RTX 4090 在持续高负载下的实际负载因子 (Load_Factor) 修正：由于 LLM 推理包含计算密集的 Prefill 阶段和带宽密集的 Decode 阶段，平均功耗通常低于峰值 TDP，典型 Load_Factor 范围 [0.8, 0.95]，需根据 Batch Size 和上下文长度分布进行加权平均计算。

## Evidence

先验知识/题面给定，逻辑校验通过：LLM推理中Prefill（计算密集）与Decode（带宽密集）混合负载导致平均功耗低于峰值TDP，0.8-0.95的负载因子范围符合工程经验与物理直觉。
