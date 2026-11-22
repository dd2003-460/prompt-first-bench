# N263: C_infra 的量化公式展开：C_infra = (P_gpu × T_hours) / COP_effective × E_price，其中 COP_eff

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N86

## Claim

C_infra 的量化公式展开：C_infra = (P_gpu × T_hours) / COP_effective × E_price，其中 COP_effective 是决定基础设施成本的核心变量，需根据散热方案确定具体数值。

## Corrected Claim

C_infra 的量化公式展开：C_infra = (P_gpu × T_hours) / COP_effective × E_price，其中 COP_effective 是决定基础设施成本的核心变量，需根据散热方案确定具体数值。

## Evidence

先验知识/题面给定，逻辑校验通过：公式量纲正确（功率×时间/能效比×单价=成本），COP作为散热效率核心变量符合物理直觉。
