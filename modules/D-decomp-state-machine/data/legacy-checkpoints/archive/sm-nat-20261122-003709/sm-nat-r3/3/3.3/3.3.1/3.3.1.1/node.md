# N165: 工作点1（高驻留/低更新）：假设 T_res = 50天（基于 H_static=0.95），计算 M_invalidation = 1 - exp(-0.01

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

工作点1（高驻留/低更新）：假设 T_res = 50天（基于 H_static=0.95），计算 M_invalidation = 1 - exp(-0.01 * 50) \approx 0.393，此时 D_eff = 0.607，命中率折损显著，适用于静态内容为主的场景。

## Corrected Claim

工作点1（高驻留/低更新）：假设 T_res = 50天（基于 H_static=0.95），计算 M_invalidation = 1 - exp(-0.01 * 50) \approx 0.393，此时 D_eff = 0.607，命中率折损显著，适用于静态内容为主的场景。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - exp(-0.5) ≈ 0.3934 正确，D_eff = 1 - 0.3934 = 0.6066 ≈ 0.607 正确，逻辑自洽。
