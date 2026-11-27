# N78: 用户投诉率<1%约束的操作定义：投诉率 = (Monthly Complaints / Monthly Active Users) * 100%，需监控干预后3

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N22

## Claim

用户投诉率<1%约束的操作定义：投诉率 = (Monthly Complaints / Monthly Active Users) * 100%，需监控干预后30天内的投诉数据，基线投诉率通常为 0.5-1.5% [待核验]，若基线已接近1%，则约束极难满足。

## Corrected Claim

用户投诉率<1%约束的操作定义：投诉率 = (Monthly Complaints / Monthly Active Users) * 100%，需监控干预后30天内的投诉数据。基线投诉率因业务而异，若基线已接近1%，则约束极难满足。

## Evidence

[质询]基线投诉率 0.5-1.5% 属于特定行业或业务场景的经验统计值，并非普适常数，不同业务（如电商、金融、社交）差异巨大，直接作为通用基线缺乏依据。 | source=knowledge，逻辑自洽（公式定义正确，若基线接近上限则约束确实难以满足），但具体数值范围属于经验事实，无外部来源支持，依据经验事实排除条款降级。

## Search Query

average user complaint rate in online marketplace platforms baseline
