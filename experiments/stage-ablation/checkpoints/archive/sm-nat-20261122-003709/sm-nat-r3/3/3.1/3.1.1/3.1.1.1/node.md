# N150: 工作点1（高覆盖率/低精度）：假设缓存覆盖前 90% 的流量对象（K≈10,000），此时 H_obj_max ≈ 0.90，M_capacity = 1 - 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N49

## Claim

工作点1（高覆盖率/低精度）：假设缓存覆盖前 90% 的流量对象（K≈10,000），此时 H_obj_max ≈ 0.90，M_capacity = 1 - 0.90 = 0.10（10%），适用于对象大小分布均匀且热点集中的场景。

## Corrected Claim

工作点1（高覆盖率/低精度）：假设缓存覆盖前 90% 的流量对象（K≈10,000），此时 H_obj_max ≈ 0.90，M_capacity = 1 - 0.90 = 0.10（10%），适用于对象大小分布均匀且热点集中的场景。

## Evidence

先验知识/题面给定，逻辑校验通过：M_capacity = 1 - H_obj_max 符合定义，数值计算 1-0.90=0.10 正确，场景描述逻辑自洽。
