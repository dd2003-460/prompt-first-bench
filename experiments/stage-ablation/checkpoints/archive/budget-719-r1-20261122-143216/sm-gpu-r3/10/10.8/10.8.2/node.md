# N414: 等效 TCO 的完整计算公式：TCO_equiv = (Cost_hardware + Cost_power_3y + Cost_cooling_3y) / (

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N146

## Claim

等效 TCO 的完整计算公式：TCO_equiv = (Cost_hardware + Cost_power_3y + Cost_cooling_3y) / (Throughput_Pcie * (1 - Maintenance_Factor))，其中 Maintenance_Factor 包含驱动兼容性和部署调试的人力成本，该公式用于对比 2×4090 与 1×H100 的最终性价比。

## Corrected Claim

等效 TCO 的完整计算公式：TCO_equiv = (Cost_hardware + Cost_power_3y + Cost_cooling_3y) / (Throughput_Pcie * (1 - Maintenance_Factor))，其中 Maintenance_Factor 包含驱动兼容性和部署调试的人力成本，该公式用于对比 2×4090 与 1×H100 的最终性价比。

## Evidence

先验知识/题面给定，逻辑校验通过
