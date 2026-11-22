# N287: 合规成本 C_compliance 在高影响场景下的工作点：N_affected > 10000 且 δc > 0.05 时，C_compliance ≈ C_

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N95

## Claim

合规成本 C_compliance 在高影响场景下的工作点：N_affected > 10000 且 δc > 0.05 时，C_compliance ≈ C_notification * 20000 + C_legal * P_avg * 0.05 ≈ $1000 + 0.05 * P_avg，总成本约为 $1000 + 0.05 * P_avg，此时法律合规固定成本占比成为主导项。

## Corrected Claim

合规成本 C_compliance 在高影响场景下的工作点：N_affected > 10000 且 δc > 0.05 时，C_compliance ≈ C_notification * 20000 + C_legal * P_avg * 0.05。若 C_notification ≈ $0.05，则通知成本项约为 $1000；法律成本项取决于 P_avg 的具体量级，需明确 P_avg 的定义及典型值才能判断主导项。

## Evidence

[质询]数值量级与逻辑推导存在严重矛盾：若 C_notification 为常规通知成本（如 $0.05），则 C_notification * 20000 = $1000，此时 C_legal * P_avg * 0.05 项若 P_avg 为概率（0-1）或较小数值，其量级远小于 $1000，无法成为'主导项'；若 P_avg 极大（如 20000），则总成本远超 $1000，与结论'总成本约为 $1000'矛盾。此外，'法律合规固定成本占比成为主导项'的表述与公式中 C_legal * P_avg * 0.05 为可变项（依赖 P_avg）相悖，除非 P_avg 被定义为常数，但题干未明确。 | 先验知识/题面给定，逻辑校验未通过：公式推导与结论'总成本约为 $1000'及'固定成本主导'存在内部矛盾，无法自洽。
