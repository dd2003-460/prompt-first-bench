# N49: 计算纯容量未命中率 M_capacity，公式为 M_capacity = 1 - H_obj_max，其中 H_obj_max 为缓存容量 C=128GB 能

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

计算纯容量未命中率 M_capacity，公式为 M_capacity = 1 - H_obj_max，其中 H_obj_max 为缓存容量 C=128GB 能覆盖的最大对象级命中率，需基于 Zipf(β=0.9) 分布累积频率计算，假设对象大小与热度独立或已修正 ρ 后的有效覆盖对象数 K_eff。

## Corrected Claim

计算纯容量未命中率 M_capacity，公式为 M_capacity = 1 - H_obj_max，其中 H_obj_max 为缓存容量 C=128GB 能覆盖的最大对象级命中率，需基于 Zipf(β=0.9) 分布累积频率计算，假设对象大小与热度独立或已修正 ρ 后的有效覆盖对象数 K_eff。

## Evidence

先验知识/题面给定，逻辑校验通过：纯容量未命中率定义为1减去最大对象级命中率，符合缓存理论中基于Zipf分布计算累积频率覆盖率的逻辑，量纲与定义自洽。
