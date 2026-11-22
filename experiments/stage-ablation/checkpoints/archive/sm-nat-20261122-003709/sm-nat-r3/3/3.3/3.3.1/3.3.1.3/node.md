# N167: 工作点3（低驻留/高更新）：假设 T_res = 0.5天（基于 H_static=0.50，高并发小对象），计算 M_invalidation = 1 - e

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N55

## Claim

工作点3（低驻留/高更新）：假设 T_res = 0.5天（基于 H_static=0.50，高并发小对象），计算 M_invalidation = 1 - exp(-0.01 * 0.5) \approx 0.005，此时 D_eff = 0.995，命中率折损可忽略，适用于实时流媒体或API网关场景。

## Corrected Claim

工作点3（低驻留/高更新）：假设 T_res = 0.5天（基于 H_static=0.50，高并发小对象），计算 M_invalidation = 1 - exp(-0.01 * 0.5) \approx 0.005，此时 D_eff = 0.995，命中率折损可忽略，适用于实时流媒体或API网关场景。

## Evidence

先验知识/题面给定，逻辑校验通过：数学计算 1 - exp(-0.005) ≈ 0.0049875 ≈ 0.005 正确，D_eff = 1 - 0.005 = 0.995 正确，结论符合逻辑。
