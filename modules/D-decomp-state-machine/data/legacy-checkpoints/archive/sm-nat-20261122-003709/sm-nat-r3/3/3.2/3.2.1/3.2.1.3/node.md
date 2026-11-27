# N160: T_resident 的最终数值计算：代入 T_resident = 128GB / (476.8GB/day * (1 - 0.97))，若 H_obj_LR

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N52

## Claim

T_resident 的最终数值计算：代入 T_resident = 128GB / (476.8GB/day * (1 - 0.97))，若 H_obj_LRU=0.97，则 T_resident ≈ 128 / (14.3) ≈ 8.95 天；若 H_obj_LRU=1.0（理想情况），公式分母为零，表明稳态下所有对象常驻，T_resident 趋向无穷大，此时失效模型需改用对象级更新周期而非缓存驻留时间。

## Corrected Claim

T_resident 的最终数值计算：代入 T_resident = 128GB / (476.8GB/day * (1 - 0.97))，若 H_obj_LRU=0.97，则 T_resident ≈ 128 / (14.3) ≈ 8.95 天；若 H_obj_LRU=1.0（理想情况），公式分母为零，表明稳态下所有对象常驻，T_resident 趋向无穷大，此时失效模型需改用对象级更新周期而非缓存驻留时间。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算 128 / (476.8 * 0.03) ≈ 8.95 正确；H=1.0 时分母为零导致 T 趋向无穷大的逻辑推导符合缓存驻留时间定义。
