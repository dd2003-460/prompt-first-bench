# N89: N32 中 P_stale ≈ 1e-10 的计算存在量级错误：基于 N34 修正后的 T_resident ≈ 1.55e-5 天，P_stale = u *

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N32

## Claim

N32 中 P_stale ≈ 1e-10 的计算存在量级错误：基于 N34 修正后的 T_resident ≈ 1.55e-5 天，P_stale = u * T_resident = 0.01 * 1.55e-5 = 1.55e-7，而非 1e-10；因此 F_decay = 1 - 1.55e-7 * 0.587 ≈ 0.99999991，修正自矛盾检测中 N12/N31 的数值冲突。

## Corrected Claim

N32 中 P_stale ≈ 1e-10 的计算存在量级错误：基于 N34 修正后的 T_resident ≈ 1.55e-5 天，P_stale = u * T_resident = 0.01 * 1.55e-5 = 1.55e-7，而非 1e-10；因此 F_decay = 1 - 1.55e-7 * 0.587 ≈ 0.99999991，修正自矛盾检测中 N12/N31 的数值冲突。

## Evidence

先验知识/题面给定，逻辑校验通过：计算 0.01 * 1.55e-5 = 1.55e-7 正确，F_decay 近似值 0.99999991 符合数学推导，量级合理。
