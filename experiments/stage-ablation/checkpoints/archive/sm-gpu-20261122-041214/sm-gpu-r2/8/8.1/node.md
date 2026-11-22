# N158: Cost_Per_Token 公式中 CapEx 项的具体构成：CapEx = (GPU_Unit_Price * N_GPUs) + (Motherboard

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N46

## Claim

Cost_Per_Token 公式中 CapEx 项的具体构成：CapEx = (GPU_Unit_Price * N_GPUs) + (Motherboard_Cost + PSU_Cost + Chassis_Cost)。对于单卡方案，基础设施成本约 $500-$1000；对于双卡消费级方案，需增加 $200-$500 的散热/结构增强成本。此值需代入 N27 和 N29 的具体数值。

## Corrected Claim

Cost_Per_Token 公式中 CapEx 项的具体构成：CapEx = (GPU_Unit_Price * N_GPUs) + (Motherboard_Cost + PSU_Cost + Chassis_Cost)。对于单卡方案，基础设施成本约 $500-$1000；对于双卡消费级方案，需增加 $200-$500 的散热/结构增强成本。此值需代入 N27 和 N29 的具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过
