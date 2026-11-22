# N246: Qwen3-27B 在 32K 上下文 Prefill 阶段的计算量 (FLOPs) = 2 * 27.1e9 * 32768 ≈ 1.78e15 FLOPs 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N93

## Claim

Qwen3-27B 在 32K 上下文 Prefill 阶段的计算量 (FLOPs) = 2 * 27.1e9 * 32768 ≈ 1.78e15 FLOPs (1.78 PFLOPs)，此为计算 M3 Ultra 与 RTX 4090 理论 Prefill 延迟差异的基础分子。

## Corrected Claim

Qwen3-27B 在 32K 上下文 Prefill 阶段的计算量 (FLOPs) = 2 * 27.1e9 * 32768 ≈ 1.78e15 FLOPs (1.78 PFLOPs)，此为计算 M3 Ultra 与 RTX 4090 理论 Prefill 延迟差异的基础分子。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 2 * N * L 符合 Transformer Prefill 阶段计算量估算标准，数值计算 2 * 27.1e9 * 32768 ≈ 1.778e15 准确无误。
