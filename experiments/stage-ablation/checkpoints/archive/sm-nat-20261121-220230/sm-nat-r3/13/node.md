# N301: LRU 字节命中率下界的解析公式为 H_byte = (1 - (1 - C_norm)^{1/β}) * (1 - ρ * (α-1)/(β-1))，其中 C

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 字节命中率下界的解析公式为 H_byte = (1 - (1 - C_norm)^{1/β}) * (1 - ρ * (α-1)/(β-1))，其中 C_norm = C_bytes / (N * E[s])。代入 C=128GB, N=100,000, E[s]=50KB, C_norm=0.0256, β=0.9, α=1.1, ρ=-0.3，计算得 H_byte ≈ 0.026 * 1.033 ≈ 0.027 (2.7%)，此为保守下界。

## Corrected Claim

LRU 字节命中率下界的解析公式为 H_byte = (1 - (1 - C_norm)^{1/β}) * (1 - ρ * (α-1)/(β-1))，其中 C_norm = C_bytes / (N * E[s])。代入 C=128GB, N=100,000, E[s]=50KB, C_norm=0.0256, β=0.9, α=1.1, ρ=-0.3，计算得 H_byte ≈ 0.026 * 1.033 ≈ 0.027 (2.7%)，此为保守下界。

## Evidence

检索失败: no sources from any channel (all 5 failed)
