# N47: Stale Fraction 对有效命中率的非线性影响：H_eff = H_static * (1 - P_stale) + P_stale * H_reval

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N15

## Claim

Stale Fraction 对有效命中率的非线性影响：H_eff = H_static * (1 - P_stale) + P_stale * H_revalidate，其中 H_revalidate 为重新验证后的命中率；若 H_revalidate=0.9（即 10% 概率内容已变需回源），则 H_eff = H_static * (1 - 0.1 * P_stale)；在 P_stale=0.005 时，H_eff = H_static * 0.9995，即命中率下降 0.05 个百分点，折损倍数约为 0.9995 倍。

## Corrected Claim

Stale Fraction 对有效命中率的非线性影响：H_eff = H_static * (1 - P_stale) + P_stale * H_revalidate，其中 H_revalidate 为重新验证后的命中率；若 H_revalidate=0.9（即 10% 概率内容已变需回源），则 H_eff = H_static * (1 - 0.1 * P_stale)；在 P_stale=0.005 时，H_eff = H_static * 0.9995，即命中率下降 0.05 个百分点，折损倍数约为 0.9995 倍。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导 H_eff = H_static * (1 - P_stale) + P_stale * 0.9 化简为 H_static * (1 - 0.1 * P_stale) 正确；代入 P_stale=0.005 得系数 0.9995，即下降 0.05%，计算无误。
