# N213: SSD层物理容量需求 V_ssd_phys 需容纳全部100TB温数据以支持全量顺序扫描，即使η=90%，因扫描触及所有数据，V_ssd_phys = 100T

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N66

## Claim

SSD层物理容量需求 V_ssd_phys 需容纳全部100TB温数据以支持全量顺序扫描，即使η=90%，因扫描触及所有数据，V_ssd_phys = 100TB / (1 - Cache_Miss_Expansion_Factor)；若Cache_Miss_Expansion_Factor=0.1（考虑元数据和碎片），V_ssd_phys ≈ 111TB

## Corrected Claim

SSD层物理容量需求 V_ssd_phys 需容纳全部100TB温数据以支持全量顺序扫描，即使η=90%，因扫描触及所有数据，V_ssd_phys = 100TB / (1 - Cache_Miss_Expansion_Factor)；若Cache_Miss_Expansion_Factor=0.1（考虑元数据和碎片），V_ssd_phys ≈ 111TB

## Evidence

先验知识/题面给定，逻辑校验通过：100TB / (1 - 0.1) = 111.11TB，计算正确且符合存储扩容逻辑

## Search Query

SSD cache sizing for full sequential scan workload
