# N219: 单卡方案 3 年电力成本计算公式：Electricity_Cost_3y = (GPU_TDP + System_Overhead_W) × 24h × 365

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N69

## Claim

单卡方案 3 年电力成本计算公式：Electricity_Cost_3y = (GPU_TDP + System_Overhead_W) × 24h × 365d × 3y × Electricity_Rate ($/kWh)，其中 System_Overhead_W 为 CPU/内存/风扇等系统基础功耗，通常取值 100W-150W

## Corrected Claim

单卡方案 3 年电力成本计算公式：Electricity_Cost_3y = (GPU_TDP + System_Overhead_W) × 24h × 365d × 3y × Electricity_Rate ($/kWh)，其中 System_Overhead_W 为 CPU/内存/风扇等系统基础功耗，通常取值 100W-150W

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（W×h=Wh，换算kWh后乘以$/kWh得$），系统基础功耗100W-150W符合常规服务器/工作站经验值。
