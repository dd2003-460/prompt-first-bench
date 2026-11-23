# N101: 自建节点运维团队最小规模 $N_{sre}$ 的确定：基于 7x24 故障响应 SLA（如 P1 级故障 15 分钟响应），需至少配置 $N_{shifts}=

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N25

## Claim

自建节点运维团队最小规模 $N_{sre}$ 的确定：基于 7x24 故障响应 SLA（如 P1 级故障 15 分钟响应），需至少配置 $N_{shifts}=3$ 个班次，每班次 1 名 SRE，故 $N_{sre} \ge 3$；若含休假备份，实际 $N_{sre} = 4-5$ 人。

## Corrected Claim

自建节点运维团队最小规模 $N_{sre}$ 的确定：基于 7x24 故障响应 SLA（如 P1 级故障 15 分钟响应），需至少配置 $N_{shifts}=3$ 个班次，每班次 1 名 SRE，故 $N_{sre} \ge 3$；若含休假备份，实际 $N_{sre} = 4-5$ 人。

## Evidence

先验知识/题面给定，逻辑校验通过：7x24 三班倒需 3 人，加上休假备份（通常 1-2 人）得出 4-5 人符合 SRE 运维常规配置逻辑。

## Search Query

SRE on-call rotation minimum team size 7x24 SLA
