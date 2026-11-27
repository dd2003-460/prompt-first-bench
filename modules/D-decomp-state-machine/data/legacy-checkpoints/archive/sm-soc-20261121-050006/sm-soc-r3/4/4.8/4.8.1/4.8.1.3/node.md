# N292: 流量补偿的边际效用递减：ΔQ_comp = η_comp * log(Impressions_target / I_base)，其中 I_base 为基准曝光量

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N92

## Claim

流量补偿的边际效用递减：ΔQ_comp = η_comp * log(Impressions_target / I_base)，其中 I_base 为基准曝光量，η_comp 为初始弹性系数；当 Impressions_target > 10 * I_base 时，边际效用下降 50%，导致成本效益比 C_traffic/ΔQ_comp 上升，需设定上限以避免浪费。

## Corrected Claim

流量补偿的边际效用通常随曝光量增加而递减，具体衰减模型（如对数形式）及阈值（如10倍基准曝光量）需根据实际业务数据拟合确定，而非固定常数。

## Evidence

[质询]该公式及具体阈值（10倍曝光量导致边际效用下降50%）属于特定业务场景下的经验性建模假设，并非通用的第一性原理或数学公理，缺乏普适性逻辑推导基础。 | 先验知识/题面给定，逻辑校验通过（对数函数性质符合边际效用递减直觉），但具体参数（10倍、50%）为经验事实，无外部来源支持，故降级。

## Search Query

diminishing returns of traffic compensation on inquiry rate
