# N169: 边界条件：当 T_shift << 1/λ 时，f_stale ≈ 1 - λ*T_shift，此时 LFU 退化为静态缓存，需计算在 T_shift=1 天、

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N58, N59, N60

## Claim

边界条件：当 T_shift << 1/λ 时，f_stale ≈ 1 - λ*T_shift，此时 LFU 退化为静态缓存，需计算在 T_shift=1 天、λ=0.1 时 f_stale=0.9 对应的命中率下界 H_min。

## Corrected Claim

边界条件：当 T_shift << 1/λ 时，f_stale ≈ 1 - λ*T_shift，此时 LFU 退化为静态缓存，需计算在 T_shift=1 天、λ=0.1 时 f_stale=0.9 对应的命中率下界 H_min。

## Evidence

先验知识/题面给定，逻辑校验通过：T_shift=1, λ=0.1 满足 T_shift << 1/λ (1 << 10) 的近似条件，代入公式 f_stale ≈ 1 - 0.1*1 = 0.9 计算正确，逻辑自洽。
