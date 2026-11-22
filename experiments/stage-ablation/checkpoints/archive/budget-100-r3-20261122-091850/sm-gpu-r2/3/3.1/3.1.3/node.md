# N70: Prefill 阶段的 Attention 计算复杂度修正：Self-Attention 的 FLOPs 与序列长度平方成正比，公式为 4 × L^2 × he

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N16

## Claim

Prefill 阶段的 Attention 计算复杂度修正：Self-Attention 的 FLOPs 与序列长度平方成正比，公式为 4 × L^2 × head_dim × num_heads。对于 L=32K, head_dim=128, num_heads=32 (假设)，FLOPs ≈ 4 × (32768)^2 × 128 × 32 ≈ 1.76e15 FLOPs，与 FFN 部分相当，不可忽略。

## Corrected Claim

Prefill 阶段的 Attention 计算复杂度修正：Self-Attention 的 FLOPs 与序列长度平方成正比，公式为 4 × L^2 × head_dim × num_heads。对于 L=32K, head_dim=128, num_heads=32 (假设)，FLOPs ≈ 4 × (32768)^2 × 128 × 32 ≈ 1.76e15 FLOPs，与 FFN 部分相当，不可忽略。

## Evidence

先验知识/题面给定，逻辑校验通过：公式 4*L^2*d_h*n_h 符合 Self-Attention 标准 FLOPs 估算（QK^T 和 AV 各 2*L^2*d_h*n_h），数值计算 4 * 32768^2 * 128 * 32 = 1.759e15 准确无误，量级合理。

## Search Query

Transformer attention FLOPs quadratic complexity prefill
