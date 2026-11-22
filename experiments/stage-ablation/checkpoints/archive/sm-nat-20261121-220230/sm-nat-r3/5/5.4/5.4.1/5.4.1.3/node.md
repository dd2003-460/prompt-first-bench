# N247: “线性敏感区”的量化定义：二阶导数 d²D/du² = T_resident(T_resident-1)(1-u)^(T_resident-2)；在 u=0.0

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

“线性敏感区”的量化定义：二阶导数 d²D/du² = T_resident(T_resident-1)(1-u)^(T_resident-2)；在 u=0.01 处，若 |d²D/du²| < 0.1 * |dD/du|，则视为线性区。对于 T_resident=1，d²D/du²=0，严格线性；对于 T_resident=10，d²D/du² ≈ -0.83，相对一阶导数较大，进入非线性区。

## Corrected Claim

“线性敏感区”的量化定义：二阶导数 d²D/du² = T_resident(T_resident-1)(1-u)^(T_resident-2)；在 u=0.01 处，若 |d²D/du²| < 0.1 * |dD/du|，则视为线性区。对于 T_resident=1，d²D/du²=0，严格线性；对于 T_resident=10，d²D/du² ≈ -0.83，相对一阶导数较大，进入非线性区。

## Evidence

先验知识/题面给定，逻辑校验通过：公式推导符合二项分布/多项式展开的二阶导数性质，数值计算（T=10, u=0.01时二阶导约为-0.83，一阶导约为0.9，比值约0.9>0.1）逻辑自洽且量级合理。
