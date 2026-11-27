# N346: 电网取电功率修正公式：P_grid = P_GPU_load / η_PSU，其中 P_GPU_load 为 GPU 实际负载功耗（非 TDP），η_PSU 取

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N108

## Claim

电网取电功率修正公式：P_grid = P_GPU_load / η_PSU，其中 P_GPU_load 为 GPU 实际负载功耗（非 TDP），η_PSU 取对应负载率下的效率值，用于精确计算 OpEx_energy。

## Corrected Claim

电网取电功率修正公式：P_grid = P_GPU_load / η_PSU，其中 P_GPU_load 为 GPU 实际负载功耗（非 TDP），η_PSU 取对应负载率下的效率值，用于精确计算 OpEx_energy。

## Evidence

先验知识/题面给定，逻辑校验通过：电网输入功率等于负载功率除以电源效率符合能量守恒定律，且区分实际负载与TDP、考虑负载率对效率的影响符合工程事实。

## Search Query

grid power consumption calculation PSU efficiency formula
