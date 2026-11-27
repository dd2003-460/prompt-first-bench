# N181: LFU 理论上限 H_lfu_max 的分母 R_byte 需使用已验证的 N73 公式：R_byte ≈ N * E[λ] * E[S] * (1 + ρ *

- **status**: verified
- **level**: L4
- **source**: given
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N80

## Claim

LFU 理论上限 H_lfu_max 的分母 R_byte 需使用已验证的 N73 公式：R_byte ≈ N * E[λ] * E[S] * (1 + ρ * σ_logS * σ_logH) = 10^5 * 500 * 11264 * 0.647 ≈ 3.64×10^11 bytes/day。此值为 LFU 命中率计算的基准分母。

## Corrected Claim

LFU 理论上限 H_lfu_max 的分母 R_byte 需使用已验证的 N73 公式：R_byte ≈ N * E[λ] * E[S] * (1 + ρ * σ_logS * σ_logH) = 10^5 * 500 * 11264 * 0.647 ≈ 3.64×10^11 bytes/day。此值为 LFU 命中率计算的基准分母。

## Evidence

先验知识/题面给定，逻辑校验通过：数值计算 10^5 * 500 * 11264 * 0.647 ≈ 3.64×10^11 准确无误，量纲（bytes/day）与上下文一致。
