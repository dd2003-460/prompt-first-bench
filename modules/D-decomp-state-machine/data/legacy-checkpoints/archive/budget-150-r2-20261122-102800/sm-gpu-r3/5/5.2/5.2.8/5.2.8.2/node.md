# N305: 修正后的年电力成本公式：Annual_Electricity_Cost = (GPU_TDP + System_Overhead) * 24 * 365 * E

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N118

## Claim

修正后的年电力成本公式：Annual_Electricity_Cost = (GPU_TDP + System_Overhead) * 24 * 365 * Electricity_Rate * Utilization_Factor。其中 System_Overhead 约为 100W（CPU/内存/风扇），Utilization_Factor 取 0.15（交互式）或 0.9（批量）。

## Corrected Claim

修正后的年电力成本公式：Annual_Electricity_Cost = (GPU_TDP + System_Overhead) * 24 * 365 * Electricity_Rate * Utilization_Factor。其中 System_Overhead 约为 100W（CPU/内存/风扇），Utilization_Factor 取 0.15（交互式）或 0.9（批量）。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

server electricity cost calculation duty cycle formula
