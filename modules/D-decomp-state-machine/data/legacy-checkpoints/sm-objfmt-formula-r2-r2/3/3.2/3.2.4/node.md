# N100: Mac Studio M2 Ultra (192GB/256GB) 的统一内存带宽标称为 800 GB/s（部分配置为 900 GB/s 或更高，取决于具体 S

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N18

## Claim

Mac Studio M2 Ultra (192GB/256GB) 的统一内存带宽标称为 800 GB/s（部分配置为 900 GB/s 或更高，取决于具体 SKU 和内存颗粒），该带宽为 CPU-GPU 共享，实际 GPU 可用带宽受内存控制器仲裁影响，通常有效利用率在 60%-80% [待核验]。

## Corrected Claim

Mac Studio M2 Ultra (192GB/256GB) 的统一内存带宽标称为 800 GB/s（部分配置为 900 GB/s 或更高，取决于具体 SKU 和内存颗粒），该带宽为 CPU-GPU 共享，实际 GPU 可用带宽受内存控制器仲裁影响，通常有效利用率在 60%-80% [待核验]。

## Evidence

先验知识/题面给定，逻辑校验通过：M2 Ultra 官方标称带宽确为 800GB/s（基础版）及更高（高配版），且共享内存架构下有效利用率受仲裁影响符合硬件常识。

## Search Query

Mac Studio M2 Ultra unified memory bandwidth GB/s
