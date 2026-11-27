# N208: 时间窗口对齐：计算 P_active 时，分子和分母必须限定在同一时间窗口（如 48h 或 7d）内，若分子包含历史降价而分母仅含近期降价，会导致 P_acti

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N66

## Claim

时间窗口对齐：计算 P_active 时，分子和分母必须限定在同一时间窗口（如 48h 或 7d）内，若分子包含历史降价而分母仅含近期降价，会导致 P_active 失真，需确保时间戳一致性。

## Corrected Claim

时间窗口对齐：计算 P_active 时，分子和分母必须限定在同一时间窗口（如 48h 或 7d）内，若分子包含历史降价而分母仅含近期降价，会导致 P_active 失真，需确保时间戳一致性。

## Evidence

先验知识/题面给定，逻辑校验通过：概率或比率计算中分子分母的时间窗口一致性是基本统计原则，逻辑自洽且无矛盾。

## Search Query

time window alignment for behavioral metric calculation
