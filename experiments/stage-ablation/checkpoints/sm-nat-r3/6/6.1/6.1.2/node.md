# N260: 截断 Pareto(α=1.1, x_min=1KB, x_max=100GB) 分布下，前 20% 对象覆盖的字节量比例 C_byte(0.2) 的数值积分结

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N91

## Claim

截断 Pareto(α=1.1, x_min=1KB, x_max=100GB) 分布下，前 20% 对象覆盖的字节量比例 C_byte(0.2) 的数值积分结果，需与 x_max=10GB 场景对比，量化 x_max 对字节占比的影响幅度（百分点）。

## Corrected Claim

截断 Pareto(α=1.1, x_min=1KB, x_max=100GB) 分布下，前 20% 对象覆盖的字节量比例 C_byte(0.2) 的数值积分结果，需与 x_max=10GB 场景对比，量化 x_max 对字节占比的影响幅度（百分点）。

## Evidence

先验知识/题面给定，逻辑校验通过
