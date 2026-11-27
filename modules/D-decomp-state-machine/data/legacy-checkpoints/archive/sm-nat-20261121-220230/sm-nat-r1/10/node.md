# N30: LRU 稳态字节命中率下界的精确推导需结合 Belady's MIN 算法近似。在 Pareto(α=1.1, β=0.9) 且 ρ=-0.3 下，理论下界 H

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

LRU 稳态字节命中率下界的精确推导需结合 Belady's MIN 算法近似。在 Pareto(α=1.1, β=0.9) 且 ρ=-0.3 下，理论下界 H_lower ≈ 1 - (1 - C_norm)^{1/α_eff}，其中 α_eff 是考虑相关性后的有效尾指数。若 C_norm=0.119，α_eff≈1.05，则 H_lower ≈ 1 - (0.881)^{0.952} ≈ 0.12。此数值需通过蒙特卡洛仿真验证，而非仅凭解析公式。

## Corrected Claim

LRU 稳态字节命中率下界的精确推导需结合 Belady's MIN 算法近似。在 Pareto(α=1.1, β=0.9) 且 ρ=-0.3 下，理论下界 H_lower ≈ 1 - (1 - C_norm)^{1/α_eff}，其中 α_eff 是考虑相关性后的有效尾指数。若 C_norm=0.119，α_eff≈1.05，则 H_lower ≈ 1 - (0.881)^{0.952} ≈ 0.12。此数值需通过蒙特卡洛仿真验证，而非仅凭解析公式。

## Evidence

检索失败: no sources from any channel (all 5 failed)
