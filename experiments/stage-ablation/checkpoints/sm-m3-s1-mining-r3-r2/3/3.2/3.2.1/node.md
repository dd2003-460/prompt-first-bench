# N22: 题面给定导热系数 k_giv = 450 W/(m·K) 与 6061-T6 铝合金标准参考值 k_ref = 201 W/(m·K) 之间的相对误差定义为 E

- **status**: verified
- **level**: L3
- **source**: given
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N13

## Claim

题面给定导热系数 k_giv = 450 W/(m·K) 与 6061-T6 铝合金标准参考值 k_ref = 201 W/(m·K) 之间的相对误差定义为 E_rel = (k_giv - k_ref)/k_ref = (450 - 201)/201 ≈ 123.9%，量化了偏离程度。

## Corrected Claim

题面给定导热系数 k_giv = 450 W/(m·K) 与 6061-T6 铝合金标准参考值 k_ref = 201 W/(m·K) 之间的相对误差定义为 E_rel = (k_giv - k_ref)/k_ref = (450 - 201)/201 ≈ 123.9%，量化了偏离程度。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (450-201)/201 ≈ 1.2388 正确，符合相对误差定义。
