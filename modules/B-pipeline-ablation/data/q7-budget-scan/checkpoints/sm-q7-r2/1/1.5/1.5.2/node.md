# N52: EC(4,2) 纠删码组配置下的有效容量计算：EC(4,2) 意味着 4 个数据块 + 2 个校验块，共 6 块为一组，每组有效数据量为 4 块。若单组物理容量

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N10

## Claim

EC(4,2) 纠删码组配置下的有效容量计算：EC(4,2) 意味着 4 个数据块 + 2 个校验块，共 6 块为一组，每组有效数据量为 4 块。若单组物理容量为 6*16TB=96TB，则有效数据量为 4*16TB=64TB，转换系数为 96/64 = 1.5

## Corrected Claim

EC(4,2) 纠删码组配置下的有效容量计算：EC(4,2) 意味着 4 个数据块 + 2 个校验块，共 6 块为一组，每组有效数据量为 4 块。若单组物理容量为 6*16TB=96TB，则有效数据量为 4*16TB=64TB，转换系数为 96/64 = 1.5

## Evidence

先验知识/题面给定，逻辑校验通过：EC(4,2)定义明确，容量计算 6*16=96 和 4*16=64 正确，比值 1.5 符合纠删码冗余系数定义。

## Search Query

erasure coding ec 4 2 storage efficiency
