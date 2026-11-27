# N17: 多卡TCO = 硬件购置成本 × 卡数 + (总电力消耗 × 运行小时数 × 电价) + 多卡互联损耗（NVLink/PCIe带宽限制导致的效率下降），需考虑多

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N3

## Claim

多卡TCO = 硬件购置成本 × 卡数 + (总电力消耗 × 运行小时数 × 电价) + 多卡互联损耗（NVLink/PCIe带宽限制导致的效率下降），需考虑多卡同步开销。

## Corrected Claim

多卡TCO = 硬件购置成本 × 卡数 + (总电力消耗 × 运行小时数 × 电价) + 多卡互联损耗（NVLink/PCIe带宽限制导致的效率下降），需考虑多卡同步开销。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

multi-GPU TCO NVLink PCIe bandwidth efficiency loss
