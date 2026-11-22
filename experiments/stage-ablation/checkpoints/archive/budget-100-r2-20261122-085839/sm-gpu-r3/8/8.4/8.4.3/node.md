# N286: Cost_Per_Token 公式完整性验证：Amortized_Hardware_Cost 仅占 TCO 的 60%-80%（低利用率时），剩余 20%-40

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N106

## Claim

Cost_Per_Token 公式完整性验证：Amortized_Hardware_Cost 仅占 TCO 的 60%-80%（低利用率时），剩余 20%-40% 为电力、网络、维护成本。若忽略电力成本，RTX 4090 的 Cost_Per_Token 被低估 10%-15%，可能导致在 24/7 场景下错误推荐高功耗卡。

## Corrected Claim

Amortized_Hardware_Cost 通常占 TCO 的主要部分（低利用率时较高），剩余为电力、网络等运营成本。忽略电力成本会导致高功耗卡（如 RTX 4090）的 Cost_Per_Token 被显著低估，可能在 24/7 场景下导致选型偏差。

## Evidence

[质询]具体数值区间（60%-80%硬件占比、10%-15%低估幅度）属于经验性工程估算，缺乏通用标准或第一性原理推导支持，不同场景下波动较大，存在口径混淆风险。 | 先验知识/题面给定，逻辑校验通过（TCO构成逻辑自洽），但具体百分比为经验事实且无外部来源支持，依据经验事实排除条款降级。

## Search Query

TCO breakdown hardware depreciation electricity maintenance cost ratio
